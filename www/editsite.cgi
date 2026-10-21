#!../login/loggedin /bin/csh -f
unset user # csh
if(! $?PATH_INFO) setenv PATH_INFO /$USER_SITE
setenv site "$PATH_INFO:t"
can --redirect --site=$site editsite
if($status) exit 0
source ../setcan
can --site=$site admin
setenv NOTADMIN $status
if($?DELETE) then
	if(! $?SURE) then
		setenv MSG "请勾选删除按钮旁的复选框确认"
		goto done
	endif
	setenv C `sql -ct "$DB" 'UPDATE user SET site=NULL WHERE site=$site' 'DELETE FROM site WHERE site=$site'`
	if($status || "$C" == "" || "$C" == "0") then
		setenv MSG "正在使用中，无法删除"
		goto done
	endif
	../login/redirect / 已删除
	exit 0
endif
if($?sitename) then
	if($site == 0) then
		setenv site `sql -i "$DB" 'INSERT INTO site SET organisation=$USER_ORGANISATION,site=0'`
		sql "$DB" 'INSERT INTO access SET organisation=$USER_ORGANISATION,site="$site",accessname="默认权限"'
		sql "$DB" 'INSERT INTO area SET organisation=$USER_ORGANISATION,site=$site,area="A",areaname="主楼"'
		sql "$DB" 'UPDATE user SET organisation=$USER_ORGANISATION,site=$site WHERE user="$USER_ID"'
		setenv aid `makeaid --site="$site"`
	endif
	if(! $?nomesh) setenv nomesh false
	if(! $?iotstatesystem) setenv iotstatesystem false
	if(! $?ioteventarm) setenv ioteventarm false
	if(! $?meshlr) setenv meshlr false
	if(! $?debug) setenv debug false
	if($?root) then
		if("$root" == "") unsetenv root
	endif
	sqlwrite -qon "$DB" site sitename wifissid wifipass wifichan iottopic iothost nomesh smsuser smspass smsfrom sms2user sms2pass sms2from toothost tootbearer armcancel armdelay alarmdelay alarmhold mqttdied debug rollover iotstatesystem ioteventarm smsarm smsarmfail smsdisarm smscancel smsalarm smspanic smsfire engineer smsnumber hookoffline hookfob hookfobdeny hookalarm hookfire hookpanic hookwarning hooktamper hookfault hooktrigger hookinhibit hookarm hookstrong hookdisarm hookarmfail hookopen hookforced hooknotclosed hooknotopen hookpropped hookwrongpin meshlr wifibssid root hookoffline emailfrom hookarm hookstrong hookdisarm hookopen hookarmfail hookforced hookpropped hookwrongpin
	sql "$DB" 'UPDATE device SET poke=NOW() WHERE site=$site'
	message --poke
	redirect /
	exit 0
endif
done:
xmlsql -C -d "$DB" head.html - foot.html << 'END'
<h1><if site=0>🆕 </if>🏘 站点管理</h1>
<form method=post>
<sql table=site key=site>
<table>
<tr><td>名称</td><td><input name=sitename size=40 autofocus></td></tr>
<tr><td>WiFi 名称</td><td><input name=wifissid size=40 value="SolarSystem"></td></tr>
<tr><td>WiFi 密码</td><td><input name=wifipass size=40 value="security"></td></tr>
<tr><td>WiFi 信道</td><td><select name=wifichan><option value=0>自动</option><FOR SPACE C="1 2 3 4 5 6 7 8 9 10 11 12 13"><option value=$C><output name=C></option></FOR></select>
<input name=wifibssid size=12 maxlength=12 placeholder="BSSID（十六进制）">
</td></tr>
<tr><td>Mesh 组网</td><td>
<if not nomesh=true>
根节点：<select name=root><option value=''>无</option><sql table=device where="site=$site"><option value="$device"><output name=devicename></option></sql></select>
<input name=meshlr type=checkbox value=true id=meshlr title="WiFi 远距离（LR）模式"><label for=meshlr>LR</label>
</if>
<input type=checkbox id=nomesh name=nomesh value=true><label for=nomesh>不使用 Mesh</label>
</td><tr>
<tr><td>IoT MQTT</td><td><input name=iothost size=40></td></tr>
<tr><td>IoT 主题</td><td><input name=iottopic size=16>（用于 state/SS/.../system 消息）</td></tr>
<tr><td>IoT 日志</td><td>
<input type=checkbox id=iotstatesystem name=iotstatesystem value=true><label for=iotstatesystem>系统</label>
<input type=checkbox id=ioteventarm name=ioteventarm value=true><label for=ioteventarm>布防/触发/撤防</label>
</td></tr>
<tr><td>自动轮换</td><td><input name=rollover size=3> 天（多少天后自动轮换密钥）</td></tr>
<tr><td><input type=checkbox id=debug name=debug value=true></td><td><label for=debug>调试模式（输出更多日志）。</label></td></tr>
<tr><td>布防取消</td><td><input name=armcancel size=3> 秒（超过此时间未完成布防则取消）</td></tr>
<tr><td>布防延时</td><td><input name=armdelay size=3> 秒（延迟多久后生效布防）</td></tr>
<tr><td>报警延时</td><td><input name=alarmdelay size=3> 秒（触发后延迟多久报警）</td></tr>
<tr><td>报警保持</td><td><input name=alarmhold size=3> 秒（最后一次触发后持续报警多久）</td></tr>
<tr><td>MQTT 重启</td><td><input name=mqttdied size=3> 秒（连不上 MQTT 多久后重启设备）</td></tr>
<tr><td colspan=2><hr></td></tr>
<tr><td colspan=2>事件通知设置</td></tr>
<tr><td>Bearer 令牌</td><td><input type=password name=hookbearer size=40 placeholder="Web 回调时发送">（用于 Web 回调）</td></tr>
<tr><td>发件邮箱</td><td><input name=emailfrom size=40>（用于邮件通知）</td></tr>
<tr><td>短信用户名</td><td><input name=smsuser size=40>（用于短信通知）</td></tr>
<tr><td>短信密码</td><td><input type=password name=smspass size=40></td></tr>
<tr><td>短信发送号码</td><td><input name=smsfrom size=20 maxlength=20> （需运营商支持）</td></tr>
<tr><td>备用短信用户名</td><td><input name=sms2user size=40>（用于以 * 开头号码的短信通知）</td></tr>
<tr><td>短信密码</td><td><input type=password name=sms2pass size=40></td></tr>
<tr><td>短信发送号码</td><td><input name=sms2from size=20 maxlength=20> （需运营商支持）</td></tr>
<tr><td>Toot 服务器</td><td><input name=toothost size=50> Mastodon 主机</td></tr>
<tr><td>Toot 令牌</td><td><input type=password name=tootbearer size=50> 认证用</td></tr>
<tr><td colspan=2><hr></td></tr>
<tr><td colspan=2>事件通知（可填 https:// 地址用 JSON POST 推送、邮箱地址、手机号发短信；手机号前加 * 则用备用短信通道，例如可为报警设置特殊提示音）</td></tr>
<tr><td>离线事件</td><td><input name=hookoffline size=80 placeholder="https://... / 邮箱 / 手机号"></td></tr>
<tr><td>刷卡事件</td><td><input name=hookfob size=80 placeholder="https://... / 邮箱 / 手机号"></td></tr>
<tr><td>刷卡拒绝事件</td><td><input name=hookfobdeny size=80 placeholder="https://... / 邮箱 / 手机号"></td></tr>
<tr><td>报警事件</td><td><input name=hookalarm size=80 placeholder="https://... / 邮箱 / 手机号"></td></tr>
<tr><td>火警事件</td><td><input name=hookfire size=80 placeholder="https://... / 邮箱 / 手机号"></td></tr>
<tr><td>紧急求助事件</td><td><input name=hookpanic size=80 placeholder="https://... / 邮箱 / 手机号"></td></tr>
<tr><td>警告事件</td><td><input name=hookwarning size=80 placeholder="https://... / 邮箱 / 手机号"></td></tr>
<tr><td>防拆事件</td><td><input name=hooktamper size=80 placeholder="https://... / 邮箱 / 手机号"></td></tr>
<tr><td>故障事件</td><td><input name=hookfault size=80 placeholder="https://... / 邮箱 / 手机号"></td></tr>
<tr><td>触发事件</td><td><input name=hooktrigger size=80 placeholder="https://... / 邮箱 / 手机号"></td></tr>
<tr><td>屏蔽事件</td><td><input name=hookinhibit size=80 placeholder="https://... / 邮箱 / 手机号"></td></tr>
<tr><td>布防事件</td><td><input name=hookarm size=80 placeholder="https://... / 邮箱 / 手机号"></td></tr>
<tr><td>强制布防事件</td><td><input name=hookstrong size=80 placeholder="https://... / 邮箱 / 手机号"></td></tr>
<tr><td>撤防事件</td><td><input name=hookdisarm size=80 placeholder="https://... / 邮箱 / 手机号"></td></tr>
<tr><td>布防失败事件</td><td><input name=hookarmfail size=80 placeholder="https://... / 邮箱 / 手机号"></td></tr>
<tr><td>开门事件</td><td><input name=hookopen size=80 placeholder="https://... / 邮箱 / 手机号"></td></tr>
<tr><td>强行开门事件</td><td><input name=hookforced size=80 placeholder="https://... / 邮箱 / 手机号"></td></tr>
<tr><td>未开门事件</td><td><input name=hooknotopen size=80 placeholder="https://... / 邮箱 / 手机号"></td></tr>
<tr><td>未关门事件</td><td><input name=hooknotclosed size=80 placeholder="https://... / 邮箱 / 手机号"> （即未授权撑门）</td></tr>
<tr><td>撑门事件</td><td><input name=hookpropped size=80 placeholder="https://... / 邮箱 / 手机号"> （即授权撑门）</td></tr>
<tr><td>密码错误事件</td><td><input name=hookwrongpin size=80 placeholder="https://... / 邮箱 / 手机号"> （键盘）</td></tr>
<tr><td colspan=2><hr></td></tr>
<tr><td>短信接收号码</td><td><input name=smsnumber size=20 maxlength=20>（按下表勾选的防区发送短信）</td></tr>
</table>
<table>
<set tags="engineer smsarm smsarmfail smsdisarm smscancel smsalarm smspanic smsfire">
<tr><th></th>
<for SPACE T="$tags"><th><output name=T engineer="工程模式" smsarm="短信:布防" smsarmfail="短信:布防失败" smsdisarm="短信:撤防" smscancel="短信:取消" smsalarm="短信:报警" smspanic="短信:紧急" smsfire="短信:火警"></th></for>
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
</sql>
<input type=submit value="保存">
<IF NOT site=0 USER_ADMIN=true><input type=submit value="删除" name=DELETE><input type=checkbox name=SURE title='勾选以确认删除'></IF>
</form>
</sql>
'END'
