#!../login/loggedin --query /bin/csh -f
if(! $?USER_ORGANISATION && "$USER_ADMIN" == false) then
        setenv C `sql "$DB" 'SELECT COUNT(*) FROM userorganisation WHERE user=$USER_ID'`
        if("$C" == 1) then
                setenv USER_ORGANISATION `sql "$DB" 'SELECT organisation FROM userorganisation WHERE user=$USER_ID'`
                sql "$DB" 'UPDATE user SET organisation=$USER_ORGANISATION WHERE user="$USER_ID"'
        endif
endif
if($?USER_ORGANISATION && ! $?USER_SITE) then
        setenv C `sql "$DB" 'SELECT COUNT(*) FROM site WHERE organisation=$USER_ORGANISATION'`
        if("$C" == 1) then
                setenv USER_SITE `sql "$DB" 'SELECT site FROM site WHERE organisation=$USER_ORGANISATION'`
                sql "$DB" 'UPDATE user SET site=$USER_SITE WHERE user="$USER_ID"'
        endif
endif
source ../setcan
xmlsql -C -d "$DB" head.html - foot.html << 'END'
<p>SolarSystem 门禁云服务 <output name=VERSION></p>
<ul>
<if USER_ADMIN=true><li><a href="editorganisation.cgi/0">🆕 新建组织</a></li><br></if>
<if USER_ORGANISATION AND CANEDITORGANISATION><li><a href="editorganisation.cgi/$USER_ORGANISATION">🏢 编辑组织</a></li></if>
<if USER_ORGANISATION AND CANEDITUSER><li><a href="edituserorganisation.cgi">📇 用户管理</a></li></if>
<hr>
<if USER_ORGANISATION AND USER_ADMIN=true><li><a href="editsite.cgi/0">🆕 新建站点</a></li><br></if>
<if USER_SITE CANEDITSITE><li><a href="editsite.cgi/$USER_SITE">🏘 站点管理</a></li></if>
<if USER_SITE CANEDITAREA><li><a href="editarea.cgi/$USER_SITE">🔠 防区管理</a></li></if>
<if USER_ORGANISATION AND ADMINORGANISATION><li><a href="editaid.cgi/$USER_SITE">🔢 AID 管理</a></li></if>
<if USER_SITE CANARM><li><a href="arm.cgi/$USER_SITE">🔔 布防</a></li></if>
<if USER_SITE CANDISARM><li><a href="disarm.cgi/$USER_SITE">🔕 撤防</a></li></if>
<if USER_SITE CANVIEWLOG><li><a href="log.cgi">🗒 日志</a></li></if>
<hr>
<if USER_ADMIN=true><sql table=device where="online is not null AND nfctrusted='true'" limit=1><li><a href="provisionfob.cgi">🆕 初始化新门卡</a></li><br></sql></if>
<if USER_ORGANISATION AND CANEDITACCESS><li><a href="editaccess.cgi">🔐 权限组管理</a></li></if>
<if USER_SITE CANEDITFOB><li><a href="editfob.cgi">🔑 门卡管理</a></li></if>
<if USER_SITE CANADOPTFOB><li><a href="adoptfob.cgi">🙋 绑定门卡</a></li></if>
<hr>
<if USER_ADMIN=true><li><a href="editpcb.cgi">🔬 PCB 模板管理</a></li><br></if>
<if USER_SITE CANEDITDEVICE><li><a href="editdevice.cgi">🪛 设备管理</a></li></if>
<if ELSE USER_SITE CANVIEWDEVICE><li><a href="editdevice.cgi">查看设备</a></li></if>
</ul>
<IF USER_ADMIN=true>
<table>
<sql select="pending.*,device.device AS D,device.online AS O,device.devicename" table="pending LEFT JOIN device ON (pending=device)" order="pending.online DESC" WHERE="pending.online<NOW()"><set found=1>
<tr>
<td><output name=pending href="provisiondevice.cgi/$+pending"></td>
<td><output name=address></td>
<td><output name=online></td>
<td><output name=version></td>
<td><output name=flash></td>
<td>
<if authenticated=true><b>设备已通过认证。</b><br></if>
<if secureboot=false><b>未启用安全启动。</b><br></if>
<if encryptednvs=false><b>NVS 未加密。</b><br></if>
<if O><b>该设备已作为已认证设备在线</b><br></if>
<if D NOT O><b>该设备之前已在使用（<output name=devicename>），将被替换。</b><br></if>
</td>
</tr>
</sql>
</table>
</IF>
'END'
