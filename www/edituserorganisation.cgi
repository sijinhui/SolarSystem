#!../login/loggedin /bin/csh -f
unset user # clash
can --redirect --organisation='$USER_ORGANISATION' edituser
if($status) exit 0
source ../setcan
# save
if($?userorganisationname) then
	if($status) exit 0
	setenv allow "userorganisationname"
	if(! $?admin) setenv admin false
	if(! $?caneditorganisation) setenv caneditorganisation false
	if(! $?caneditaccess) setenv caneditaccess false
	if(! $?caneditsite) setenv caneditsite false
	if(! $?caneditdevice) setenv caneditdevice false
	if(! $?canviewdevice) setenv canviewdevice false
	if(! $?caneditfob) setenv caneditfob false
	if(! $?canadoptfob) setenv canadoptfob false
	if(! $?canedituser) setenv canedituser false
	if(! $?caneditarea) setenv caneditarea false
	if(! $?canarm) setenv canarm false
	if(! $?canstrong) setenv canstrong false
	if(! $?candisarm) setenv candisarm false
	if(! $?canunlock) setenv canunlock false
	if(! $?canviewlog) setenv canviewlog false
	if(! $?canapi) setenv canapi false
	if(! $?apiexpires) setenv apiexpires false
	if(! $?apiarm) setenv apiarm false
	if(! $?apistrong) setenv apistrong false
	if(! $?apidisarm) setenv apidisarm false
	if($?ADMINORGANISATION) setenv allow "$allow admin"
	if($?CANEDITORGANISATION) setenv allow "$allow caneditorganisation"
	if($?CANEDITACCESS) setenv allow "$allow caneditaccess"
	if($?CANEDITSITE) setenv allow "$allow caneditsite"
	if($?CANEDITDEVICE) setenv allow "$allow caneditdevice"
	if($?CANVIEWDEVICE) setenv allow "$allow canviewdevice"
	if($?CANEDITFOB) setenv allow "$allow caneditfob"
	if($?CANADOPTFOB) setenv allow "$allow canadoptfob"
	if($?CANEDITUSER) setenv allow "$allow canedituser"
	if($?CANEDITAREA) setenv allow "$allow caneditarea"
	if($?CANARM) setenv allow "$allow canarm"
	if($?CANSTRONG) setenv allow "$allow canstrong"
	if($?CANDISARM) setenv allow "$allow candisarm"
	if($?CANUNLOCK) setenv allow "$allow canunlock"
	if($?CANVIEWLOG) setenv allow "$allow canviewlog"
	if($?CANAPI) setenv allow "$allow canapi apiexpires apiarm apistrong apidisarm"
	sqlwrite -qon "$DB" userorganisation $allow
endif
if($?DELETE) then
	if(! $?SURE) then
		setenv MSG "请勾选删除按钮旁的复选框确认"
		goto edit
	endif
	sql "$DB" 'DELETE FROM userorganisation WHERE user=$user AND organisation=$USER_ORGANISATION'
endif
if($?NEW) then
	setenv user `sql "$DB" 'SELECT user FROM user WHERE email="$NEW"'`
	if("$user" == "" || "$user" == NULL) then
		setenv MSG "未找到该用户，请先让对方注册"
		goto list
	endif
	sql "$DB" 'INSERT INTO userorganisation SET organisation=$USER_ORGANISATION,user=$user'
	redirect "edituserorganisation.cgi/$user"
	exit 0
endif
list:
if(! $?PATH_INFO) then
xmlsql -C -d "$DB" head.html - foot.html << 'END'
<h1>📇 用户管理</h1>
<form method=post style='inline'>
<table>
<sql select="*,user.admin AS A" table="userorganisation LEFT JOIN user USING (user)" WHERE="userorganisation.organisation=$USER_ORGANISATION"><set found=1>
<tr>
<td>
<if A=true><b>系统管理员</b></if>
<if admin=true>管理员</if>
<if canapi=true>API</if>
</td>
<td><output name=email href="/edituserorganisation.cgi/$user"></td>
<td><output name=username></td>
<td><output name=userorganisationname></td>
</tr>
</sql>
<tr>
<td><input type=submit value="添加用户"></td>
<td colspan=3><input name=NEW type=email size=40 placeholder="用户的邮箱地址" autofocus></td>
</tr>
</table>
</form>
<if not found><p>未找到用户</p></if>
'END'
exit 0
endif
# edit class
setenv user "$PATH_INFO:t"
edit:
xmlsql -C -d "$DB" head.html - foot.html << 'END'
<h1>📇 编辑用户</h1>
<sql table="userorganisation LEFT JOIN user USING (user)"  where="user=$user AND userorganisation.organisation=$USER_ORGANISATION">
<form method=post action="/edituserorganisation.cgi"><input type=hidden name=user><input type=hidden name=organisation>
<table>
<tr><td>姓名</td><td><output name=username></td></tr>
<tr><td>邮箱</td><td><output name=email></td></tr>
<tr><td>职位</td><td><input name=userorganisationname size=40 autofocus></td></tr>
<if ADMINORGANISATION><tr><td><input type=checkbox id=admin name=admin value=true></td><td><label for=admin>组织管理员（拥有以下全部权限）</label></td></tr></if>
<if CANEDITORGANISATION><tr><td><input type=checkbox id=caneditorganisation name=caneditorganisation value=true></td><td><label for=caneditorganisation>可编辑组织</label></td></tr></if>
<if CANEDITACCESS><tr><td><input type=checkbox id=caneditaccess name=caneditaccess value=true></td><td><label for=caneditaccess>可编辑权限组</label></td></tr></if>
<if CANEDITSITE><tr><td><input type=checkbox id=caneditsite name=caneditsite value=true></td><td><label for=caneditsite>可编辑站点</label></td></tr></if>
<if CANEDITDEVICE><tr><td><input type=checkbox id=caneditdevice name=caneditdevice value=true></td><td><label for=caneditdevice>可编辑设备</label></td></tr></if>
<if CANVIEWDEVICE><tr><td><input type=checkbox id=canviewdevice name=canviewdevice value=true></td><td><label for=canviewdevice>可查看设备</label></td></tr></if>
<if CANEDITFOB><tr><td><input type=checkbox id=caneditfob name=caneditfob value=true></td><td><label for=caneditfob>可编辑门卡</label></td></tr></if>
<if CANADOPTFOB><tr><td><input type=checkbox id=canadoptfob name=canadoptfob value=true></td><td><label for=canadoptfob>可绑定门卡</label></td></tr></if>
<if CANEDITUSER><tr><td><input type=checkbox id=canedituser name=canedituser value=true></td><td><label for=canedituser>可编辑用户</label></td></tr></if>
<if CANEDITAREA><tr><td><input type=checkbox id=caneditarea name=caneditarea value=true></td><td><label for=caneditarea>可编辑防区</label></td></tr></if>
<if CANARM><tr><td><input type=checkbox id=canarm name=canarm value=true></td><td><label for=canarm>可布防</label></td></tr></if>
<if CANSTRONG><tr><td><input type=checkbox id=canstrong name=canstrong value=true></td><td><label for=canstrong>可强制布防</label></td></tr></if>
<if CANDISARM><tr><td><input type=checkbox id=candisarm name=candisarm value=true></td><td><label for=candisarm>可撤防</label></td></tr></if>
<if CANUNLOCK><tr><td><input type=checkbox id=canunlock name=canunlock value=true></td><td><label for=canunlock>可开门</label></td></tr></if>
<if CANVIEWLOG><tr><td><input type=checkbox id=canviewlog name=canviewlog value=true></td><td><label for=canviewlog>可查看日志</label></td></tr></if>
<if CANAPI><tr><td><input type=checkbox id=canapi name=canapi value=true></td><td><label for=canapi>可使用 API</label></td></tr></if>
<if CANAPI canapi=true><tr><td><input type=checkbox id=apiexpires name=apiexpires value=true></td><td><label for=apiexpires>可通过 API 设置门卡有效期</label></td></tr></if>
<if CANAPI canapi=true><tr><td><input type=checkbox id=apiarm name=apiarm value=true></td><td><label for=apiarm>可通过 API 布防</label></td></tr></if>
<if CANAPI canapi=true><tr><td><input type=checkbox id=apistrong name=apistrong value=true></td><td><label for=apistrong>可通过 API 强制布防</label></td></tr></if>
<if CANAPI canapi=true><tr><td><input type=checkbox id=apidisarm name=apidisarm value=true></td><td><label for=apidisarm>可通过 API 撤防</label></td></tr></if>
</table>
<input type=submit value="保存">
<input type=submit name=DELETE value="删除"><input type=checkbox name=SURE title='勾选以确认删除'>
</form>
</sql>
'END'
