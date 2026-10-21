#!../login/loggedin /bin/csh -f
if($?PATH_INFO) then
	setenv device "$PATH_INFO:t"
endif
can --redirect --organisation='$USER_ORGANISATION' viewdevice
if($status) exit 0

if($?UNLOCK) then
	can --redirect --device='$device' unlock
	if($status) exit 0
	setenv MSG `message --device="$device" --command=unlock`
	if("$MSG" != "") goto done
	redirect editdevice.cgi
	exit 0
endif

if($?OOSALL) then
	can --redirect --site='$USER_SITE' admin
	if($status) exit 0
	sql "$DB" 'UPDATE device SET outofservice="true",poke=NOW() WHERE outofservice="false" AND organisation="$USER_ORGANISATION" AND site="$USER_SITE" AND excludeall<>"true"'
        message --poke
	redirect editdevice.cgi
	exit 0
endif
if($?ISALL) then
	can --redirect --site='$USER_SITE' admin
	if($status) exit 0
	sql "$DB" 'UPDATE device SET outofservice="false",poke=NOW() WHERE outofservice="true" AND organisation="$USER_ORGANISATION" AND site="$USER_SITE" AND excludeall<>"true"'
        message --poke
	redirect editdevice.cgi
	exit 0
endif
if($?UPGRADEALL) then
	can --redirect --site='$USER_SITE' editdevice
	if($status) exit 0
	sql "$DB" 'UPDATE device SET upgrade=NOW() WHERE upgrade is NULL AND organisation="$USER_ORGANISATION" AND site="$USER_SITE" AND excludeall<>"true"'
        message --poke
	redirect editdevice.cgi
	exit 0
endif
if($?UPGRADE) then
	can --redirect --device='$device' editdevice
	if($status) exit 0
	sql "$DB" 'UPDATE device SET upgrade=NOW() WHERE device="$device"'
	setenv BUILD_SUFFIX `sql "$DB" 'SELECT build_suffix FROM device WHERE device="$device"'`
	setenv MSG `message --device="$device" --command=upgrade '"'"/SS$BUILD_SUFFIX.bin"'"'`
	if("$MSG" != "") goto done
	redirect editdevice.cgi
	exit 0
endif
if($?RESTART) then
	can --redirect --device='$device' editdevice
	if($status) exit 0
	setenv MSG `message --device="$device" --command=restart`
	if("$MSG" != "") goto done
	redirect editdevice.cgi
	exit 0
endif
if($?DELETE && "$USER_ADMIN" == "true" || $?FACTORY) then
	can --redirect --device='$device' editdevice
	if($status) exit 0
	if(! $?SURE) then
		setenv MSG "确定吗？请勾选最后的复选框确认"
		goto done
	endif
	if($?FACTORY)	then
		setenv MSG `message --device="$device" --command=factory '"'"$device"'SS"'`
		if($status) goto done
	else
		setenv MSG `message --device="$device" --command=restart`
	endif
	sql "$DB" 'UPDATE device SET site=NULL WHERE device="$device"'
	sql "$DB" 'UPDATE device SET poke=NOW() WHERE site=$site'
        message --poke
	redirect editdevice.cgi
	exit 0
endif
if($?devicename) then # save
	can --redirect --device='$device' editdevice
	if($status) exit 0
	setenv wassite `sql "$DB" 'SELECT site FROM device WHERE device="$device"'`
	if("$site" != "$wassite") then
		setenv aid `sql "$DB" 'SELECT aid FROM aid WHERE site=$site ORDER BY aid LIMIT 1'`
	endif
	if($?pcb) then
		setenv rgb `sql "$DB" 'SELECT IF(ledr="-","false","true") FROM pcb WHERE pcb=$pcb'`
		setenv nfc `sql "$DB" 'SELECT IF(nfctx="-","false","true") FROM pcb WHERE pcb=$pcb'`
		setenv gps `sql "$DB" 'SELECT IF(gpstx="-","false","true") FROM pcb WHERE pcb=$pcb'`
		setenv keypad `sql "$DB" 'SELECT IF(keypadtx="-","false","true") FROM pcb WHERE pcb=$pcb'`
	endif
	if(! $?outofservice) setenv outofservice false
	if(! $?excludeall) setenv excludeall false
	if(! $?nfcadmin) setenv nfcadmin false
	if(! $?nfctrusted) setenv nfctrusted false
	if(! $?door) setenv door false
	if(! $?doorexitarm) setenv doorexitarm false
	if(! $?doorexitdisarm) setenv doorexitdisarm false
	if(! $?doordebug) setenv doordebug false
	if(! $?doorcatch) setenv doorcatch false
	if(! $?iotstatedoor) setenv iotstatedoor false
	if(! $?iotstateinput) setenv iotstateinput false
	if(! $?iotstateoutput) setenv iotstateoutput false
	if(! $?iotkeypad) setenv iotkeypad false
	if(! $?iotgps) setenv iotgps false
	if(! $?ioteventfob) setenv ioteventfob false
	if(! $?keypadpinarm) setenv keypadpinarm false
	setenv allow "devicename timer1 areaenter areastrong areadeadlock areaarm areadisarm areabell arealed areakeypad areakeyarm areakeystrong areakeydisarm nfc gps rgb nfcadmin door doorexitarm doorexitdisarm aid site iotstatedoor iotstateinput iotstateoutput ioteventfob iotkeypad iotgps doorunlock doorlock dooropen doorclose doorprop doorexit doordebounce keypadidle keypadpin keypadpinarm keypad pcb dooriotopen dooriotlock dooriotunlock dooriotdead dooriotundead excludeall outofservice doordebug doorcatch nfcidle"
	if("$USER_ADMIN" == "true") setenv allow "$allow nfctrusted"
	sqlwrite -qon "$DB" device $allow
	sql "$DB" 'UPDATE device SET poke=NOW() WHERE site=$site'
	if("$site" != "$wassite") then
		sql "$DB" 'UPDATE device SET poke=NOW() WHERE site=$wassite'
	endif
        message --poke
	redirect editdevice.cgi
	exit 0
endif
done:
source ../types
source ../setcan
xmlsql -C -d "$DB" head.html - foot.html << 'END'
<h1>🪛 设备管理 <output name=VERSION></h1>
<if device CANVIEWLOG><p><a href="/log.cgi/$device">查看日志</a></p></if>
<if not device CANVIEWDEVICE>
<table>
<tr>
<th>设备</th>
<th>在线</th>
<th>连接</th>
<th>版本</th>
<th>PCB</th>
<th>Flash</th>
<th>内存</th>
<th>SPI</th>
<th>备注</th></tr>
<sql table="site" where="site=$USER_SITE"><set root="$root"></sql>
<sql table="device" where="site=$USER_SITE" select="max(version) AS V,max(build) AS B"><set V="$V"><set B="$B"></sql>
<sql table="device LEFT JOIN pcb USING (pcb) LEFT JOIN device AS device2 ON (device.via=device2.device) LEFT JOIN device AS device3 ON (conv(device.bssid,16,10)=conv(device3.device,16,10)+1)" order="if(device.device='$root',0,1),device.outofservice,device.devicename" WHERE="device.site=$USER_SITE" select="device.*,pcb.pcbname,device2.devicename AS VIA,device3.devicename AS PARENT"><set found=1>
<set s="">
<if outofservice=false><if lastonline><set s="background:green;"><if not via><set s="background:lightgreen;"></if></if><if not online><set s="background:yellow;"></if></if>
<if outofservice=true><if lastonline><set s="background:lightblue;"></if><if not online><set s="background:blue;"></if></if>
<tr style="$s">
<td title="$device"><IF CANEDITDEVICE><output href="/editdevice.cgi/$device" name=devicename blank="未命名" missing="未命名"></if><if else><output name=devicename></if></td>
<td align=right><if online><tt title="上线时间"><output name=boot missing="刚刚" type=recent></if><if else><tt title="最后在线"><output name=lastonline missing="从未" type=recent></tt></if></td>
<td><if online><if via><i>经由</i> <if PARENT NOT PARENT="$VIA"><output name=PARENT> &amp; </if><output name=VIA></if><if else><tt title="BSSID#channel"><output name=bssid>#<output name=chan></tt> <i title="WiFi 名称"><output name=ssid></i></if></if><if else><i title="离线原因"><output name=offlinereason></i></if></td>
<td><if upgrade><if online OR outofservice=false><i style='background:cyan;'>升级 <output name=progress 0=已开始 missing=已排队></i><br></if></if><set s="background:red;"><if version="$V"><set s="background:green;"></if><tt style="$s"><output name=version><output name=build_suffix></tt></td>
<td><output name=pcbname></td>
<td align=right><output name=flash type=mebi replace .00="" .0Mi="Mi">B</td>
<td align=right><output name=mem type=mebi replace .00="" .0Mi="Mi">B</td>
<td align=right><if spi=0>-</if><if else><output name=spi type=mebi replace .00="" .0Mi="Mi">B</if></td>
<td>
<if excludeall=true>*</if>
<if outofservice=true>停用中</if>
<if else>
<if online door=true CANUNLOCK><form style="display:inline;" method=post><input type=hidden name=device><input type=submit name=UNLOCK value="开门"></form></if>
<if door=true>门控 </if><if gps=true>GPS </if><if nfc=true>NFC 读卡器 </if><if nfcadmin=true>（管理）</if><if nfctrusted=true><b>（受信任）</b></if>
</if>
<if online not via><output name=address></if>
<if USER_ADMIN=true><i title='重启原因'><output name=rst missing='' 0='' 1='上电' 2='' 3='' 4='程序崩溃' 5='中断看门狗' 6='任务看门狗' 7='看门狗复位' 8='深度睡眠' 9='欠压' 10='SDIO 复位' 11='USB 复位'></i></IF>
</td>
</tr>
</sql>
</table>
<if found>
<if CANEDITDEVICE><form method=post style="display:inline-block;"><input name=UPGRADEALL value="全部升级" type=submit></form></if>
<if USER_ADMIN=true><form method=post style="display:inline-block;"><input name=OOSALL value="全部停用" type=submit></form></if>
<if USER_ADMIN=true><form method=post style="display:inline-block;"><input name=ISALL value="全部启用" type=submit></form></if>
</if><if else><p>未找到设备。</p></if>
</if><if else CANEDITDEVICE>
<form method=post action=/editdevice.cgi><input type=hidden name=device>
<sql table="device LEFT JOIN pcb USING (pcb)" KEY=device>
<table>
<tr><td><input type=checkbox id=outofservice name=outofservice value=true></td><td colspan=2><label for=outofservice>停用（建议升级前先停用，升级更快）</label></td></tr>
<tr><td><input type=checkbox id=excludeall name=excludeall value=true></td><td colspan=2><label for=excludeall>不受「全部」按钮影响</label></td></tr>
<tr><td>PCB</td><td colspan=2><select name=pcb><sql table=pcb order=pcbname><option value="$pcb"><output name=pcbname></option></sql></select></td></tr>
<tr><td>名称</td><td colspan=2><input name=devicename size=20 maxlength=20 autofocus></td></tr>
<if keypad=true><tr><td>键盘待机文字</td><td colspan=2><input name=keypadidle size=16 maxlength=16 autofocus></td></tr></if>
<if keypad=true><tr><td>键盘密码</td><td colspan=2><input name=keypadpin size=16 maxlength=16 autofocus> 用于撤防， <input type=checkbox id=keypadpinarm name=keypadpinarm value=true><label for=keypadpinarm> 也用于布防</label></td></tr></if>
<tr><td>站点</td><td colspan=2><select name=site><sql table=site where="organisation=$USER_ORGANISATION"><option value='$site'><output name=sitename></option></sql></select></td></tr>
<sql table=site where="site=$site">
<if not iothost="">
<tr><td>IoT (<output name=iothost>)</td><td colspan=2>
<input id=iotstateinput name=iotstateinput value=true type=checkbox><label for=iotstateinput>输入</label>
<input id=iotstateoutput name=iotstateoutput value=true type=checkbox><label for=iotstateoutput>输出</label>
<if door=true><input id=iotstatedoor name=iotstatedoor value=true type=checkbox><label for=iotstatedoor>门状态</label></if>
<if door=true><input id=doordebug name=doordebug value=true type=checkbox><label for=doordebug>门调试</label></if>
<if nfc=true><input id=ioteventfob name=ioteventfob value=true type=checkbox><label for=ioteventfob>门卡事件</label></if>
<if keypad=true><input id=iotkeypad name=iotkeypad value=true type=checkbox><label for=iotkeypad>键盘事件</label></if>
<if gps=true><input id=iotgps name=iotgps value=true type=checkbox><label for=iotgps>GPS 事件</label></if>
</td>
</if>
</sql>
<if nfc=true><tr><td>AID</td><td colspan=2><select name=aid><sql table=aid where="site=$site"><option value="$aid"><output name=aidname></option></sql></select></td></tr></if>
<tr><td>在线</td><td colspan=2><if online><output name=online></if><if else>最后在线 <output name=lastonline missing="从未"></if><if upgrade>（已安排升级）</if></td></tr>
<tr><td>版本</td><td colspan=2><output name=version></td></tr>
<tr><td>定时器1</td><td><input name=timer1 type=time> 时钟已校准时作为定时逻辑输入</td></tr>
<sql table=pcb where="pcb=$pcb">
<tr><td><input type=checkbox id=door name=door value=true></td><td colspan=2><label for=door>门控<if door=true>（时间填 0 使用默认值，填 -1 强制不计时）</if></label></td></tr>
<if door=true><tr><td><input size=5 id=doorunlock name=doorunlock>ms</td><td colspan=2><label for=doorunlock>开锁计时（EL56X 锁填 -1）</label></td></tr></if>
<if door=true><tr><td><input size=5 id=doorlock name=doorlock>ms</td><td colspan=2><label for=doorlock>上锁计时</label></td></tr></if>
<if door=true><tr><td><input size=5 id=doordebounce name=doordebounce>ms</td><td colspan=2><label for=doordebounce>上锁防抖计时</label></td></tr></if>
<if door=true><tr><td><input size=5 id=dooropen name=dooropen>ms</td><td colspan=2><label for=dooropen>等待开门计时</label></td></tr></if>
<if door=true><tr><td><input size=5 id=doorclose name=doorclose>ms</td><td colspan=2><label for=doorclose>等待关门计时</label></td></tr></if>
<if door=true><tr><td><input size=5 id=doorprop name=doorprop>ms</td><td colspan=2><label for=doorprop>门未授权撑开计时</label></td></tr></if>
<if door=true><tr><td><input size=5 id=doorexit name=doorexit>ms</td><td colspan=2><label for=doorexit>出门按钮长按计时</label></td></tr></if>
<if door=true><tr><td><input type=checkbox id=doorexitdisarm name=doorexitdisarm value=true></td><td colspan=2><label for=doorexitdisarm>出门按钮撤防</label></td></tr></if>
<if door=true><tr><td><input type=checkbox id=doorexitarm name=doorexitarm value=true></td><td colspan=2><label for=doorexitarm>长按出门按钮布防</label></td></tr></if>
<if door=true><tr><td><input type=checkbox id=doorcatch name=doorcatch value=true></td><td colspan=2><label for=doorcatch>门扣模式（开门后立即重新上锁）</label></td></tr></if>
<if door=true><tr><td>上锁时 IoT 消息</td><td colspan=2><input name=dooriotlock></td></tr></if>
<if door=true><tr><td>反锁时 IoT 消息</td><td colspan=2><input name=dooriotdead></td></tr></if>
<if door=true><tr><td>解除反锁时 IoT 消息</td><td colspan=2><input name=dooriotundead></td></tr></if>
<if door=true><tr><td>开锁时 IoT 消息</td><td colspan=2><input name=dooriotunlock></td></tr></if>
<if door=true><tr><td>开门时 IoT 消息</td><td colspan=2><input name=dooriotopen></td></tr></if>
<if nfc=true><tr><td>NFC 指示灯待机</td><td colspan=2><input name=nfcidle size=3> 秒（0 为常亮）</td></tr></if>
<if nfc=true><tr><td><input type=checkbox id=nfcadmin name=nfcadmin value=true></td><td colspan=2><label for=nfcadmin>管理用 NFC 读卡器</label></td></tr></if>
<if USER_ADMIN=true nfc=true><tr><td><input type=checkbox id=nfctrusted name=nfctrusted value=true></td><td colspan=2><label for=nfctrusted>受信任 NFC 读卡器</label></td></tr></if>
</sql>
<sql select="device.device,gpio.*,devicegpio.*" table="device JOIN gpio USING (pcb) LEFT JOIN devicegpio ON (devicegpio.device=device.device AND devicegpio.gpio=gpio.gpio)" WHERE="device.device='$device'" order=initname>
<tr><td><output name=name href="/editgpio.cgi/$device/$gpio" blank="GPIO" missing="GPIO"><if not name="$initname"> (<output name=initname>)</if></td>
<if type><td><if type=*-><i>未使用</i></if><if else><b><output name=type $GPIOTYPEOUT> <if type=*I><i><output name=func replace $GPIOFUNCOUTI></i></if><if type=*O><i><output name=func $GPIOFUNCOUTO></i></if> (<output name=invert false="$value1" true="$value0"><if not pulse=0 AND type=*O> <eval #=1 s="$pulse/10"><output name=s>s</if><if not hold=0 AND type=*I> <output name=hold>ms</if>)</b></td><td><for space S="$STATELIST"><if not "$S"=''> <output name=S engineer="工程模式" faulted="故障" tampered="防拆" alarmed="曾报警" armed="已布防" prearm="预布防" prealarm="预报警" alarm="报警" doorbell="门铃" warning="警告" fault="故障输入" access="通行" presence="有人" tamper="防拆输入" fire="火警" panic="紧急求助" arm="布防" strong="强制布防" disarm="撤防"> (<output name="$S">)</if></for></if></td></if>
<if not type><td><b><output name=io $GPIOIOOUT></td><td><i>未定义</i></td></if>
</tr>
</sql>
</table>
<if rgb=true><set tags="$tags led"></if>
<if keypad=true><set tags="$tags keypad keyarm keystrong keydisarm"></if>
<if nfc=true><set tags="$tags deadlock enter arm strong disarm"></if>
<if tags>
<table>
<tr><th></th>
<for SPACE T="$tags"><if not T=""><th><output name=T led="指示灯" keypad="键盘" keyarm="键盘布防" keystrong="键盘强制布防" keydisarm="键盘撤防" deadlock="反锁" enter="进门" arm="布防" strong="强制布防" disarm="撤防"></th></if></for>
<th>防区</th>
</tr>
<sql table=area where="site=$USER_SITE">
<tr>
<th><output name=tag></th>
<for SPACE T="$tags"><if not T=""><td><input name="area$T" type=checkbox value="$tag"></td></if></for>
<td><output name=areaname></td>
</tr>
</sql>
</table>
</if>
<if nfc=true><p>布防/撤防/强制布防：门卡权限覆盖其中任一防区即可。进门/撑门：门卡权限需覆盖全部「进门」防区。任一「反锁」防区处于布防状态时门会反锁。</p></if>
<input type=submit value="保存">
<if online><input type=submit value="重启" name=RESTART></if>
<if not upgrade><input type=submit value="升级" name=UPGRADE></if>
<if USER_ADMIN=true><input type=submit value="删除" name=DELETE></if>
<if online><input type=submit value="恢复出厂" name=FACTORY></if>
<input type=checkbox name=SURE title='勾选以确认操作'>
</sql>
</form>
</if>
'END'
