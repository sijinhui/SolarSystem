#!../login/logincheck --query /bin/csh -f
setenv LINK `weblink --check`
if($status) then
        setenv FAIL "抱歉，该链接无效或已过期"
        source login.cgi
        exit 0
endif
unset user
setenv user "$LINK:e"
setenv USERNAME "$LINK:r"
setenv C `sql -c "$DB" 'UPDATE user SET email="$USERNAME" WHERE user=$user'`
if($status || "$C" == 0) then
	redirect login.cgi "无法更新邮箱"
	exit 0
endif
dologin --force --silent
if($status) then
	redirect login.cgi
else
	redirect / 已更新
endif
