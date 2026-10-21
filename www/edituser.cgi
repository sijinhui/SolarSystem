#!../login/loggedin --query /bin/csh -f
unset user # clash with csh variable, duh
if(! $?user) setenv user "$USER_ID"	# Edit self
can --redirect --user="$user" edituser
if($status) exit 0
source ../setcan
if($?email) then # save
	# update other fields... not email
	sqlwrite -qon "$DB" user user="$user" user username
	# check email change as special handling
	setenv was `sql "$DB" 'SELECT email FROM user WHERE user=$user'`
	if("$email" != "$was") then
		setenv LINK `weblink --make="$email"."$user"`
		email --subject="修改邮箱地址" --to="$email" --name="$SERVER_NAME" --from=noreply@"$SERVER_NAME" << END
您申请将邮箱地址从 $was 修改为本邮箱。

请点击以下链接确认修改：

${ENVCGI_SERVER}changeemail.cgi?$LINK
END
		email --subject="修改邮箱地址" --to="$was" --name="$SERVER_NAME" --from=noreply@"$SERVER_NAME" << END
您申请将邮箱地址修改为 $email。

确认链接已发送到新邮箱，
请登录该邮箱并点击链接完成修改。
END
		redirect / "确认邮件已发送至 $email，请查收并点击链接。"
		exit 0
	endif
	echo "Location: $ENVCGI_SERVER?MSG=Updated"
	echo ""
	exit 0
endif
xmlsql -C -d "$DB" head.html - foot.html << 'END'
<h1>📇 个人信息</h1>
<sql table=user where="user=$user">
<form method=post><input type=hidden name=user>
<table>
<tr><td>邮箱</td><td><input name=email type=email size=40></td></tr>
<tr><td>姓名</td><td><input name=username size=40 autofocus></td></tr>
</table>
<input type=submit value="保存">
</form>
</sql>
<a href="/changepassword.cgi">修改密码</a>
'END'
