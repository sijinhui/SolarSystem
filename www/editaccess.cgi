#!../login/loggedin /bin/csh -f
can --redirect --site="$USER_SITE" editaccess
if($status) exit 0

source ../setcan
setenv days "sun mon tue wed thu fri sat"

if($?DELETE) then
	if(! $?SURE) then
		setenv MSG "确定吗？请勾选删除按钮旁的复选框确认"
		goto edit
	endif
	can --redirect --access="$access" admin
	if($status) exit 0
	setenv C `sql -c "$DB" 'DELETE FROM access WHERE access=$access'`
	if("$C" == "" || "$C" == "0") then
                setenv MSG "正在使用中，无法删除"
                goto done
        endif
        redirect editaccess.cgi
        exit 0
endif
if($?access) then
	if("$access" == 0) then
		setenv access `sql -i "$DB" 'INSERT INTO access SET organisation=$USER_ORGANISATION,site=$USER_SITE'`
	endif
	can --redirect --access="$access" editaccess
	if($status) exit 0
	setenv allow "accessname clock log count armlate commit enter arm disarm strong prop expiry"
	foreach day ($days)
		setenv allow "$allow ${day}from ${day}to"
	end
	if(! $?clock) setenv clock false
	if(! $?override) setenv override false
	if(! $?log) setenv log false
	if(! $?count) setenv count false
	if(! $?commit) setenv commit false
	if(! $?armlate) setenv armlate false
	if($?ADMINORGANISATION) setenv allow "$allow override"
	sqlwrite -qon "$DB" access $allow
	redirect editaccess.cgi
	exit 0
endif

if(! $?PATH_INFO) then
list:
xmlsql -C -d "$DB" head.html - foot.html << 'END'
<h1>🔐 权限组管理</h1>
<table style='white-space:nowrap'>
<tr><th>权限组</th><th>备注</th><th>有效期</th><th>周日</th><th>周一</th><th>周二</th><th>周三</th><th>周四</th><th>周五</th><th>周六</th><th>进门</th><th>布防</th><th>强制布防</th><th>撤防</th><th>撑门</th></tr>
<sql table=access where="site=$USER_SITE">
<tr>
<td><output name=accessname missing="未命名" blank="未命名" href="editaccess.cgi/$access"></td>
<td>
<if override=true><b>无条件开门</b></if>
<if armlate=true>允许非工作时间布防</if>
<if clock=true>无时钟时忽略时段</if>
<if log=true>门卡记录日志</if>
<if count=true>门卡计数</if>
<if commit=true>门卡提交</if>
</td>
<td><if expiry=0>不自动过期</if><if else><output name=expiry> 天后自动过期</if></td>
<for space day="$days">
<td><output type="%H:%M" name=${day}from>-<output name=${day}to type=%H:%M></td>
</for>
<td><output name=enter></td>
<td><output name=arm></td>
<td><output name=strong></td>
<td><output name=disarm></td>
<td><output name=prop></td>
</tr>
</sql>
</table>
<p><a href="/editaccess.cgi/0">新建权限组</a></p>
'END'
exit 0
endif

setenv access "$PATH_INFO:t"
edit:
xmlsql -C -d "$DB" head.html - foot.html << 'END'
<h1>权限组</h1>
<form method=post action=/editaccess.cgi>
<sql table=access key=access><input name=access type=hidden>
<table>
<tr><td>名称</td><td><input name=accessname size=40 autofocus></td></tr>
<tr><td><input type=checkbox id=clock name=clock value=true></td><td><label for=clock>设备时钟未校准时忽略时段限制。</label></td></tr>
<tr><td><input type=checkbox id=log name=log value=true></td><td><label for=log>尝试将通行记录写入门卡。</label></td></tr>
<tr><td><input type=checkbox id=count name=count value=true></td><td><label for=count>尝试在门卡上计数通行次数。</label></td></tr>
<tr><td><input type=checkbox id=commit name=commit value=true></td><td><label for=commit>先提交门卡写入（日志/计数）再放行（较慢）。</label></td></tr>
<tr><td><input type=checkbox id=armlate name=armlate value=true></td><td><label for=armlate>允许在非工作时间布防。</label></td></tr>
<IF ADMINORGANISATION><tr><td><input type=checkbox id=override name=override value=true></td><td><label for=override>任何情况下都开门。</label></td></tr></if>
<tr><td>自动过期</td><td><input name=expiry size=3> 天</td></tr>
<for space day="$days">
<tr><td><output name=day sun=周日 mon=周一 tue=周二 wed=周三 thu=周四 fri=周五 sat=周六></td><td><input name="${day}from" type=time>-<input name="${day}to" type=time></td></tr>
</for>
</table>
<table>
<set tags="enter arm strong disarm prop">
<tr><th></th>
<for SPACE T="$tags"><th><output name=T enter="进门" arm="布防" strong="强制布防" disarm="撤防" prop="撑门"></th></for>
<th>防区</th>
</tr>
<sql table=area where="site=$USER_SITE">
<tr>
<th><output name=tag></th>
<for SPACE T="$tags"><td><input name="$T" type=checkbox value="$tag"></td></for>
<td><output name=areaname></td>
</tr>
</sql>
</table>

<input type=submit value="保存"><if ADMINORGANISATION><input type=submit name=DELETE Value="删除"><input name=SURE type=checkbox title='勾选以确认删除'></if>
</sql>
</form>
'END'
