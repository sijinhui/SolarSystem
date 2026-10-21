#!../login/logincheck --query /bin/csh -f
setenv USERNAME `weblink --check`
if($status) then
	setenv MSG "抱歉，该链接无效或已过期"
	source login.cgi
	exit 0
endif
setenv C `sql -c "$DB" 'INSERT IGNORE INTO user SET email="$USERNAME"'`
dologin --force --redirect
