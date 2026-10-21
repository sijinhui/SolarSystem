#!../login/logincheck --query /bin/csh -f
setenv USERNAME `weblink --check`
if($status) then
	setenv MSG "抱歉，该链接无效或已过期"
	source login.cgi
	exit 0
endif
sql "$DB" 'UPDATE user SET hash=NULL WHERE email="$USERNAME"'
dologin --redirect --force

