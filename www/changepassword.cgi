#!../login/loggedin --query /bin/csh -f
setenv Z `sql "$DB" 'SELECT COUNT(*) FROM user WHERE user="$USER_ID" AND hash IS NULL'`
if($?NEWPASSWORD) then
	if("$Z" == 1) then
		setenv MSG `changepassword --force`
	else
		setenv MSG `changepassword`
	endif
	if(! $status) then
		redirect edituser.cgi
		exit 0
	endif
	unsetenv OLDPASSWORD
	unsetenv NEWPASSWORD
endif
setenv NEWPASSWORD `password`
xmlsql -C -d "$DB" head.html - foot.html << 'END'
<p>系统为您生成了一个建议的新密码，您也可以自行输入。</p>
<form method=post action=changepassword.cgi>
	<table>
		<IF Z=0><tr><td>原密码</td><td><input autocomplete="current-password" size=40 type=password name=OLDPASSWORD autofocus></td></tr></if>
		<tr><td>新密码</td><td><input autocomplete="new-password" size=40 name=NEWPASSWORD></td></td>
	</table>
	<input type=submit value="修改" name=CHANGE>
</form>
'END'
