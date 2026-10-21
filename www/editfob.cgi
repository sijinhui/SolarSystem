#!../login/loggedin /bin/csh -f
can --redirect --organisation='$USER_ORGANISATION' --site='$USER_SITE' editfob
if($status) exit 0
source ../setcan

if($?DELETE) then
	sql "$DB" 'DELETE FROM fobaid WHERE fob="$fob" AND aid IN (SELECT aid from aid WHERE organisation="$USER_ORGANISATION")'
	sql "$DB" 'DELETE FROM foborganisation WHERE fob="$fob" AND organisation="$USER_ORGANISATION"'
	redirect /
	exit 0
endif

if($?expires) then
	set aids=(`printenv aids|sed 's/[^0-9A-F	]//g'`)
	foreach a ($aids)
		setenv A "$a"
		can --redirect --aid="$A" editfob
		if($status) exit 0
		setenv access `printenv "access$A"`
		if("$access" == "") then
			setenv C `sql -c "$DB" 'DELETE FROM fobaid WHERE fob="$fob" AND aid="$A"'`
		else
			setenv C `sql -c "$DB" 'INSERT IGNORE INTO fobaid SET fob="$fob",aid="$A"'`
			sql "$DB" 'UPDATE fobaid SET access=$access WHERE fob="$fob" AND aid="$A"'
		endif
	end
	setenv organisation "$USER_ORGANISATION"
	setenv allow "fobname fobsms expires fobdata"
	if($?BLOCK) setenv blocked "`date +'%F %T'`"
	if($?BLOCK) setenv allow "$allow confirmed"
	if($?UNBLOCK||$?BLOCK) then
		setenv allow "$allow blocked"
		sql "$DB" 'UPDATE device SET device.poke=NOW() WHERE organisation="$USER_ORGANISATION"'
	endif
	setenv expires "${expires}Z"
	if("$expires" == "Z") unsetenv expires
	sqlwrite -qon "$DB" foborganisation fob organisation $allow
	message --poke
	redirect editfob.cgi
	exit 0
endif
if(! $?PATH_INFO) then
list:
setenv XMLSQLDEBUG
xmlsql -C -d "$DB" head.html - foot.html << 'END'
<h1>🔑 门卡</h1>
<table>
<set last>
<sql table="foborganisation LEFT JOIN fobaid USING (fob) LEFT JOIN aid USING (aid)" group="fob" order="max(lastused) DESC,max(adopted) DESC,fob DESC" where="foborganisation.organisation=$USER_ORGANISATION">
<sql table="foborganisation LEFT JOIN fobaid USING (fob) LEFT JOIN aid USING (aid) LEFT JOIN fob USING (fob) LEFT JOIN site USING (site) LEFT JOIN access USING (access)" where="foborganisation.organisation=$USER_ORGANISATION AND (aid.site IS NULL OR aid.site=$USER_SITE) AND fob.fob='$fob'" order="aid">
<if not found><set found=1><tr>
<th>门卡</th>
<th>剩余空间</th>
<th>名称</th>
<th>手机</th>
<th>最近使用</th>
<th>有效期</th>
<th colspan=2>备注</th>
</tr></if>
<tr>
<if last="$fob"><td colspan=4></if>
<if else><set last="$fob">
<td><output name=fob href="editfob.cgi/$fob"></td>
<td align=right><if mem><output name=mem></if></td>
<td><output name=fobname></td>
<td><output name=fobsms></td>
</if>
<td align=right><output name=lastused type=recent></td>
<td align=right><output name=expires type=recent></td>
<td>
<if site><output name=sitename>: <output name=aidname> (<output name=accessname missing="?">)</if><if else>无权限</if>
</td>
<if ver="$ver2" or ver="$ver3"><td><b>旧密钥 <tt><output name=ver></tt></b></td></if>
<if ver not ver="$ver1" not ver="$ver2" not ver="$ver3"><td><b>已废弃密钥 <tt><output name=ver></tt></b></td></if>
<if not ver><td><i>密钥版本未知</i></td></if>
<if blocked><td><b>已禁用</b></td></if>
</tr>
</sql>
</sql>
</table>
<if found><set found></if><if else><p>未找到门卡</p></if>
'END'
exit 0
endif

edit:
setenv fob "$PATH_INFO:t"
setenv OK `sql "$DB" 'SELECT COUNT(*) FROM fob WHERE fob="$fob"'`
if("$OK" == 0 || "$OK" == "" || "$OK" == NULL) then
	setenv MSG "抱歉，未找到该门卡，请确认已初始化"
	goto list
endif
xmlsql -C -d "$DB" head.html - foot.html << 'END'
<h1>🔑 门卡 <output name=fob></h1>
<if fob CANVIEWLOG><p><a href="/log.cgi/$fob">查看日志</a></p></if>
<form method=post action=/editfob.cgi><input name=fob type=hidden>
<sql table="foborganisation LEFT JOIN fob using (fob)" where="fob='$fob' AND organisation=$USER_ORGANISATION">
<table>
<tr><td>名称</td><td colspan=6><input name=fobname size=15 maxlength=15 autofocus></td></tr>
<tr><td>手机</td><td colspan=6><input name=fobsms size=15 maxlength=15></td></tr>
<tr><td>有效期</td><td colspan=6><input name=expires id=expires type=datetime-local><input type=button onclick='document.getElementById("expires").value="";' value="永不过期"></td></tr>
<tr><td>用户数据</td><td colspan=6><textarea name=fobdata placeholder=JSON cols=100></textarea></td></tr>
<if capacity><tr><td>容量</td><td><output name=capacity> 字节</td></tr></if>
<if mem><tr><td>剩余</td><td><output name=mem> 字节</td></tr></if>
<if blocked><tr><td>禁用</td><td>已于 <output name=blocked> 禁用 <if blocked and confirmed>（<output name=confirmed> 已确认）</if></td></tr></if>
<tr><th>站点</th><th>权限组</th><th>绑定时间</th><th>当日首次</th><th>最近使用</th><th>AID</th><th>密钥</th></tr>
<sql table="fobaid LEFT JOIN aid USING (aid) LEFT JOIN site USING (site)" where="fob='$fob' AND aid.organisation=$USER_ORGANISATION" order=sitename,aidname><set "access$aid"="$access">
<tr>
<td><input type=hidden name=aids value="$aid"><output name=sitename></td>
<td><select name="access$aid"><option value=''>无权限</option><sql table=access where="site=$site"><option value="$access"><output name=accessname></option></sql></select></td><td align=right><output name=adopted type=recent></td><td align=right><output name=firstinday type=recent></td><td align=right><output name=lastused type=recent></td><td><output name=aidname></td><td><tt><output name=ver></tt></td>
</tr>
</sql>
</table>
<input type=submit value="保存"><if blocked><input type=SUBMIT name=UNBLOCK Value="解除禁用"></if><if else><input type=SUBMIT name=BLOCK Value="禁用"></if>
<input type=submit name="DELETE" value="删除">
</sql>
</form>
'END'


