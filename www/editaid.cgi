#!../login/loggedin /bin/csh -f
if($?PATH_INFO) then
	setenv site "$PATH_INFO:t"
else
	setenv site "$USER_SITE"
endif
can --redirect --site='$site' admin
if($status) exit 0
source ../setcan

if($?aids || $?NEW) then #save
        set aids=(`printenv aids|sed 's/[^0-9A-F	]//g'`)
	foreach a ($aids)
		setenv A "$a"
		setenv D `printenv "NAME$A"`
		setenv R `printenv "ROLLOVER$A"`
		if("$D" == "") then
			sql "$DB" 'DELETE FROM aid WHERE site=$site AND aid="$A"'
		else
			sql "$DB" 'INSERT IGNORE INTO aid SET organisation=$USER_ORGANISATION,site=$site,aid="$A",aidname="$D"'
			sql "$DB" 'UPDATE aid SET aidname="$D" WHERE organisation=$USER_ORGANISATION AND site=$site AND aid="$A"'
		endif
		if("$R" != "") then
			setenv MSG `message --rollover="$A"`
		endif
	end
	if($?USER_ADMIN) then
		if("$NEW" != "") then
			setenv A `makeaid --site=$site --name="$NEW"`
		endif
	endif
	redirect / 已更新
	exit 0
endif

xmlsql -C -d "$DB" head.html - foot.html << 'END'
<sql table=site where="site=$site">
<h1>🔢 AID 管理：<output name=sitename></h1>
<p>如需划分独立的安全区域，可以添加更多 AID，但通常没有必要。</p>
<form method=post>
<table>
<tr><th>AID</th><th>密钥</th><th>门卡</th></tr>
<sql table=aid WHERE="site=$site">
<tr>
<td><input type=hidden name=aids value="$aid"><input name="NAME$aid" size=20 value="$aidname"></td>
<td title="密钥轮换"><tt><output name=ver1date type="%F"> <b><output name=ver1></b></tt><input type=checkbox name="ROLLOVER$aid" id="ROLLOVER$aid"><label for="ROLLOVER$aid">
<if ver2><br><tt><output name=ver2date type="%F"> <output name=ver2></tt></if>
<if ver3><br><tt><output name=ver3date type="%F"> <output name=ver3></tt></if>
</label></td>
<td>
<sql table='fobaid' where='ver IS NOT NULL AND aid="$aid"' group='ver' select='ver,count(*) AS N' order='if(ver="$ver1",1,if(ver="$ver2",2,if(ver="$ver3",3,4)))'>
<tt><output name=ver></tt> <output name=N><if ver="$ver1"> 当前</if><if ver="$ver2" or ver="$ver3"> 旧</if><if not ver="$ver1" not ver="$ver2" not ver="$ver3">（已废弃）</if><br>
</sql>
</td>
</tr>
</sql>
<if USER_ADMIN=true><tr><td><input name=NEW placeholder="新 AID 名称"></td><td colspan=2>新建 AID</td></tr></if>
</table>
<input type=submit value="保存">
<if not USER_ADMIN=true><p>如需新增 AID，请联系系统管理员。</p></if>
</form>
</sql>
<p>每个 AID 有一个当前密钥，以及最多两个旧密钥（各有一个随机两位编号）。门卡在使用时会自动更新到当前密钥。你可以随时勾选复选框进行密钥轮换生成新密钥，但所有门卡都需要在之后刷一次才能完成更新。如果某张门卡的密钥已经过旧（不是当前密钥或两个备用密钥之一），则必须重新绑定才能使用。</p>
'END'
