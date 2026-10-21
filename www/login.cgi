#!../login/logincheck --query /bin/csh -f
if($?FORGOT || $?NEW) then
	if("$USERNAME" == "") then
		redirect login.cgi "请填写邮箱地址"
		exit 0
	endif
	setenv LINK `weblink --make='$USERNAME'`
	if($?NEW) then
	email --subject="新用户注册" --to="$USERNAME" --name="$SERVER_NAME" --from="noreply@$SERVER_NAME" << END
您申请了创建新用户账号。
请点击以下链接继续：

${ENVCGI_SERVER}register.cgi?$LINK
END
	else
	email --subject="找回密码" --to="$USERNAME" --name="$SERVER_NAME" --from="noreply@$SERVER_NAME" << END
您申请了重置密码。
请点击以下链接继续：

${ENVCGI_SERVER}forgot.cgi?$LINK
END
	endif
	setenv MSG "已向 $USERNAME 发送邮件，请查收并点击邮件中的链接"
	if("$PASSWORD" != "") setenv MSG "$MSG。点击链接后需要设置密码。"
	redirect login.cgi "$MSG"
	exit 0
endif
if($?PASSWORD) then
	dologin --redirect
	exit 0
endif
done:
xmlsql -C -d "$DB" head.html - foot.html << 'END'
<form method=post action=login.cgi>
	<table>
		<tr><td>邮箱</td><td><input autocomplete="username" size=40 type=email name=USERNAME autofocus></td></tr>
		<tr><td>密码</td><td><input autocomplete="current-password" size=40 type=password name=PASSWORD></td></td>
	</table>
	<input type=submit value="登录" name=LOGIN>
	<input type=submit value="忘记密码" name=FORGOT>
	<input type=submit value="注册新用户" name=NEW>
</form>
'END'
