#!../login/loggedin /bin/csh -f
if($?PATH_INFO) then
	setenv device "$PATH_INFO:h:t"
	setenv gpio "$PATH_INFO:t"
endif
can --redirect --device='$device' editdevice
if($status) exit 0
source ../types
source ../setcan

if($?type) then
	if(! $?invert) setenv invert false
	if(! $?hold) setenv hold 0
	if(! $?pulse) setenv pulse 0
	if(! $?func) setenv func ""
	sqlwrite -qon "$DB" devicegpio device gpio func type invert name hold pulse $STATELIST
	sql "$DB" 'UPDATE device SET poke=NOW() WHERE device="$device"'
	message --poke
	redirect "editdevice.cgi/$device"
	exit 0
endif

done:
sql "$DB" 'INSERT IGNORE INTO devicegpio SET device="$device",gpio="$gpio"'
xmlsql -C -d "$DB" head.html - foot.html << 'END'
<h1>🔬 GPIO 配置</h1>
<form method=post action="/editgpio.cgi"><input name=devicegpio type=hidden>
<sql table=area where="site=$USER_SITE"><IF AREAS><SET AREAS="$AREAS "></IF><SET AREAS="$AREAS$area"></sql>
<sql table="devicegpio LEFT JOIN device USING (device) LEFT JOIN gpio ON (devicegpio.gpio=gpio.gpio)" WHERE="devicegpio.device='$device' AND devicegpio.gpio=$gpio">
<input name=device type=hidden><input name=gpio type=hidden>
<table>
<tr><td>设备</td><td><output name=devicename blank="未命名" missing="未命名"></td></tr>
<tr><td>PCB</td><td><sql table=pcb where="pcb=$pcb"><output name=pcbname></sql></td></tr>
<tr><td>GPIO</td><td><output name=pin $GPIONUMOUT></td></tr>
<if not type=-><tr><td>名称</td><td><input name=name size=10 autofocus></td></tr></if>
<if type=*I><tr><td>保持</td><td><input name=hold size=3> 毫秒（默认 100 毫秒）</td></tr></if>
<if type=*O><tr><td>脉冲</td><td><input name=pulse size=3> ×0.1 秒，正数为脉冲接通，负数为脉冲断开</td></tr></if>
<tr><td>类型</td><td><output name=io $GPIOIOOUT>:<if io=I><select name=type><include var=GPIOTYPEPICKI></select></if><if io=O><select name=type><include var=GPIOTYPEPICKO></select></if><if io=IO><select name=type><include var=GPIOTYPEPICK></select></if></td></tr>
<If not type=-*><tr><td><label for=invert>反相</label></td><td><input id=invert name=invert type=checkbox value=true> （未反相时，关为 <i><output name=value0></i>，开为 <i><output name=value1></i>）</td></tr></if>
<if type=*I><tr><td>功能</td><td><include var=GPIOFUNCSETI></td></tr></if>
<if type=*O><tr><td>功能</td><td><include var=GPIOFUNCSETO></td></tr></if>
</table>
<if not type=*P not type=*->
<if type=*O><set SL="$STATELISTO"></if><if else><set SL="$STATELISTI"></if>
<table>
<tr><th></th><for space STATE="$SL"><th><output name=STATE engineer="工程模式" faulted="故障" tampered="防拆" alarmed="曾报警" armed="已布防" prearm="预布防" prealarm="预报警" alarm="报警" doorbell="门铃" warning="警告" fault="故障输入" access="通行" presence="有人" tamper="防拆输入" fire="火警" panic="紧急求助" arm="布防" strong="强制布防" disarm="撤防"></th></for><th>防区</th></tr>
<sql table=area where="site=$USER_SITE" order=tag>
<tr>
<th><output name=tag></th>
<for space STATE="$SL"><td><input type=checkbox name="$STATE" value="$tag"></td></for>
<td><output name=areaname></td>
</sql>
</for>
</tr>
</table>
</if>
</sql>
<input type=submit value="保存">
</form>
'END'
