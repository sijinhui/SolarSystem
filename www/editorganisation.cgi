#!../login/loggedin /bin/csh -f
unset user # csh
setenv organisation "$PATH_INFO:t"
can --redirect --organisation=$organisation editorganisation
if($status) exit 0
source ../setcan
can --organisation=$organisation admin
setenv NOTADMIN $status
if($?DELETE) then
	if(! $?SURE) then
		setenv MSG "确定吗？请勾选删除按钮旁的复选框确认"
		goto done
	endif
	setenv C `sql -c "$DB" 'DELETE FROM organisation WHERE organisation=$organisation'`
	if("$C" == "" || "$C" == "0") then
		setenv MSG "正在使用中，无法删除，请先删除该组织下的内容"
		goto done
	endif
	redirect / 已删除
	exit 0
endif
if($?organisationname) then
	if($organisation == 0) then
		setenv organisation `sql -i "$DB" 'INSERT INTO organisation SET organisation=0'`
		setenv site `sql -i "$DB" 'INSERT INTO site SET sitename="主楼",organisation=$organisation,wifissid="SolarSystem",wifipass="security"'`
		sql "$DB" 'INSERT INTO access SET organisation=$organisation,site="$site",accessname="默认权限"'
		sql "$DB" 'INSERT INTO area SET organisation=$organisation,site=$site,tag="A",areaname="主楼"'
		setenv aid `makeaid --site="$site"`
		sqlwrite -qon "$DB" organisation organisationname
		redirect "editorganisation.cgi/$organisation"
		exit 0
	endif
	sqlwrite -o "$DB" organisation organisationname
	redirect /
	exit 0
endif
done:
xmlsql -C -d "$DB" head.html - foot.html << 'END'
<h1><if organisation=0>🆕 </if>🏢 组织</h1>
<form method=post>
<sql table=organisation key=organisation>
<table>
<tr><td>名称</td><td><input name=organisationname size=40 autofocus></td></tr>
</table>
</sql>
<input type=submit value="保存">
<IF NOT organisation=0 USER_ADMIN=true><input type=submit value="删除" name=DELETE><input type=checkbox name=SURE title='勾选以确认删除'></IF>
</form>
</sql>
'END'
