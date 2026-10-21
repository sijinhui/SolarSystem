#!../login/loggedin /bin/csh -f
can --redirect --site='$USER_SITE' admin
if($status) exit 0
source ../setcan
if(! $?PATH_INFO) then
	redirect /
	exit 0
endif
setenv device "$PATH_INFO:t"
if(`sql "$DB" 'SELECT count(*) FROM pending WHERE pending="$device"'` == 0 && `sql "$DB" 'SELECT count(*) FROM device WHERE device="$device"'` == 0) then
	redirect / "设备 $device 不在线"
	exit 0
endif

if($?DEPORT) then
	setenv MSG `message --pending="$device" --deport="$deport"`
	if(! $status) then
		redirect / 已迁出
		exit 0
	endif
endif
if($?PROVISION) then
	if("$pcb" == 0) then
		setenv MSG "请选择要使用的 PCB 模板"
		goto done
	endif
	if("$aid" == "") then
		setenv MSG "请选择 AID"
	endif
	setenv authenticated `sql "$DB" 'SELECT authenticated FROM pending WHERE pending="$device"'`

	../sstool --provision-device="$device" --aid="$aid" --device-name="$devicename" --copy-device="$copydevice" --pcb="$pcb"

	message --poke
	if("$authenticated" == "true") then
		setenv MSG `message --pending="$device" --command="restart"`
	else
		setenv MSG `message --pending="$device" --provision --pending="$device" --aid="$aid"`
	endif
	if(! $status) then
		redirect / 已开通
		exit 0
	endif
endif
done:
setenv pcb `sql "$DB" 'SELECT pcb FROM device WHERE device="$device"'`
setenv devicename `sql "$DB" 'SELECT devicename FROM device WHERE device="$device"'`
xmlsql -C -d "$DB" head.html - foot.html << 'END'
<h1>将设备 <output name=device> 开通到本站点</h1>
<p>注意：设备将使用当前站点的 WiFi 设置（<b><sql table=site where="site='$USER_SITE'"><output name=wifissid></sql></b>）。</p>
<form style="display:inline;" method=post>
<table>
<tr><td>PCB</td><td><select name=pcb><option value=0>-- 选择 PCB --</option><sql table=pcb order=pcbname ><option value=$pcb><output name=pcbname blank="未命名"></option></sql></select></td></tr>
<tr><td>复制</td><td><select name=copydevice><option value=''>复制已有设备的设置</option><sql table="device LEFT JOIN pcb USING (pcb)" WHERE="site=$USER_SITE"><option value=$device><output name=pcbname>: <output name=devicename></option></sql></select></td></tr>
<tr><td>AID</td><td><select name=aid><sql table=aid WHERE="site=$USER_SITE"><option value=$aid><output name=aidname></option></sql></select></td></tr>
<tr><td>名称</td><td><input name=devicename size=20 autofocus></td></tr>
<tr><td><input type=submit name=PROVISION value="开通"></td></tr>
</table>
<p>也可以把这台设备迁出到另一台服务器。</p>
<table>
<tr><td>迁出</td><td><input name=deport size=20 placeholder='MQTT 服务器'></td></tr>
<tr><td><input type=submit name=DEPORT value="迁出"></td></tr>
</table>
</form>
'END'
