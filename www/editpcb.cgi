#!../login/loggedin /bin/csh -f
can --redirect admin
if($status) exit 0
source ../setcan

if($?DELETE) then
	if(! $?SURE) then
		setenv MSG "请勾选删除按钮旁的复选框确认"
		goto done
	endif
	setenv C `sql -ct "$DB" 'DELETE FROM gpio WHERE pcb=$pcb' 'DELETE FROM pcb WHERE pcb=$pcb'`
	if("$C" == "" || "$C" == "0") then
		setenv MSG "正在使用中，无法删除"
		goto done
	endif
	unsetenv pcb
	setenv MSG 已删除
	goto done
endif
if($?COPY) then
	setenv C `sql "$DB" 'SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name="pcb" and column_name<>"pcb" AND column_name<>"pcbname"'|sed '2,$s/^/,/'`
	setenv N `sql -i "$DB" 'INSERT INTO pcb (pcb,pcbname,$%C) SELECT 0,concat(pcbname," 副本"),$%C FROM pcb WHERE pcb=$pcb'`
	setenv C `sql "$DB" 'SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name="gpio" and column_name<>"gpio" AND column_name<>"pcb"'|sed '2,$s/^/,/'`
	sql "$DB" 'INSERT INTO gpio (gpio,pcb,$%C) SELECT 0,$N,$%C FROM gpio WHERE pcb=$pcb'
	setenv pcb "$N"
	goto done
endif
if($?pcbname) then # save
	set changed=0
	if($pcb == 0) then
		setenv pcb `sql -i "$DB" 'INSERT INTO pcb SET pcb=0'`
	endif
	@ changed = $changed + `sqlwrite -c "$DB" pcb`
	set gpio=(`printenv gpio|sed 's/[^0-9 	]//g'`)
	set pin=(`printenv pin|sed 's/[^-0-9 	]//g'`)
	set io=(`printenv io|sed 's/[^-0-9A-Z 	]//g'`)
	set inittype=(`printenv inittype|sed 's/[^-0-9A-Z 	]//g'`)
	setenv set ""
	foreach n ($gpio)
	setenv n "$n"
	setenv g "$pin[1]"
	shift pin
	setenv t "$io[1]"
	shift io
	setenv i "$inittype[1]"
	shift inittype
	if("$n" == "0") then
		if("$g" != "-") then
			if("$initname" == "") then
				setenv MSG "请填写引脚名称"
				goto done
			endif
			@ changed = $changed + 1
			if("$inithold" == "")setenv inithold 0
			if("$initpulse" == "")setenv initpulse 0
			if("$value0" == "")setenv value0 Low
			if("$value1" == "")setenv value1 High
			if("$rgb" == "")setenv rgb 0
			if(! $?initinvert) setenv initinvert false
			set n=`sql -i "$DB" 'INSERT INTO gpio SET pcb="$pcb",pin="$g",io="$t",inittype="$i",rgb=$rgb,initname="$initname",inithold=$inithold,initpulse=$initpulse,initinvert="$initinvert",value0="$value0",value1="$value1"'`
		endif
	else
		if("$g" == "-") then
			@ changed = $changed + `sql -ct "$DB" 'DELETE FROM devicegpio WHERE gpio="$n"' 'DELETE FROM gpio WHERE gpio="$n" AND pcb="$pcb"'`
		else
			setenv name `printenv "initname$n"`
			setenv hold `printenv "inithold$n"`
			setenv pulse `printenv "initpulse$n"`
			setenv invert `printenv "initinvert$n"`
			setenv initfunc `printenv "initfunc$n"`
			setenv led `printenv "rgb$n"`
			if("$initfunc" == "-") setenv initfunc ""
			setenv v0 `printenv "value0$n"`
			if("$v0" == "") setenv v0 Low
			setenv v1 `printenv "value1$n"`
			if("$v1" == "")setenv v1 High
			if("$invert" == "") setenv invert false
			@ changed = $changed + `sql -c "$DB" 'UPDATE gpio SET pin="$g",io="$t",initfunc="$initfunc",rgb=$led,inittype="$i",initname="$name",inithold=$hold,initpulse=$pulse,initinvert="$invert",value0="$v0",value1="$v1" WHERE gpio="$n" AND pcb="$pcb" AND (pin<>"$g" OR io<>"$t" OR inittype<>"$i" OR inittype<>"$f" OR initname<>"$name" OR inithold<>$hold OR initpulse<>$pulse OR rgb<>$led OR initinvert<>"$invert" OR value0<>"$v0" OR value1<>"$v1")'`
		endif
	endif
	setenv set "$set,$n"
	end
	@ changed = $changed + `sql -c "$DB" 'DELETE FROM gpio WHERE pcb=$pcb AND gpio NOT IN ($,set)'`
	sql "$DB" 'UPDATE device SET poke=NOW() WHERE pcb=$pcb'
       	message --poke
	if($changed) goto done
	redirect editpcb.cgi
	exit 0
endif
done:
source ../types
if($?PATH_INFO) then
	setenv pcb "$PATH_INFO:t"
endif
unsetenv gpio
unsetenv pin
unsetenv io
unsetenv inittype
unsetenv initfunc
unsetenv inithold
unsetenv initpulse
unsetenv initname
unsetenv rgb
unsetenv value0
unsetenv value1
xmlsql -C -d "$DB" head.html - foot.html << 'END'
<h1>🔬 PCB 模板</h1>
<if not pcb>
<table>
<sql table=pcb order=pcbname>
<tr>
<td><output name=pcbname blank="未指定" missing="未命名" href="/editpcb.cgi/$pcb"></td>
</tr>
</sql>
</table>
<a href="/editpcb.cgi/0">新建 PCB</a>
</if><if else>
<form method=post action=/editpcb.cgi name=F><input type=hidden name=pcb>
<sql table=pcb key=pcb>
<table>
<tr><td>名称</td><td colspan=12><input name=pcbname size=40 autofocus></td></tr>
<if ledr==- ledg==- ledb==- OR NOT leda==-><tr><td><select name=leda><include var=GPIOREALPICK></select></td><td colspan=12>主控 LED 引脚（琥珀色）</td></tr></if>
<if leda==-><tr><td><select name=ledr><include var=GPIOREALPICK></select></td><td colspan=12>主控 LED 引脚（红色）</td></tr></if>
<if leda==-><tr><td><select name=ledg><include var=GPIOREALPICK></select></td><td colspan=12>主控 LED 引脚（绿色）</td></tr></if>
<if leda==-><tr><td><select name=ledb><include var=GPIOREALPICK></select></td><td colspan=12>主控 LED 引脚（蓝色）</td></tr></if>
<tr><td><select name=keypadtx onchange='F.submit();'><include var=GPIOREALPICK></select></td><td colspan=12>键盘 Tx 引脚</td></tr>
<if not keypadtx==->
<tr><td><select name=keypadrx><include var=GPIOREALPICK></select></td><td colspan=12>键盘 Rx 引脚</td></tr>
<tr><td><select name=keypadde><include var=GPIOREALPICK></select></td><td colspan=12>键盘 DE 引脚</td></tr>
<tr><td><select name=keypadre><include var=GPIOREALPICK></select></td><td colspan=12>键盘 RE 引脚</td></tr>
</if>
<tr><td><select name=nfctx onchange='F.submit();'><include var=GPIOREALPICK></select></td><td colspan=12>NFC Tx 引脚</td></tr>
<if not nfctx==->
<tr><td><select name=nfcrx><include var=GPIOREALPICK></select></td><td colspan=12>NFC Rx 引脚</td></tr>
<tr><td><select name=nfcpower><include var=GPIOREALPICK></select></td><td colspan=12>NFC 电源引脚</td></tr>
<tr><td><select name=nfcred><include var=GPIONFCPICK></select></td><td colspan=12>PN532 NFC 红色 LED</td></tr>
<tr><td><select name=nfcamber><include var=GPIONFCPICK></select></td><td colspan=12>PN532 NFC 琥珀色 LED</td></tr>
<tr><td><select name=nfcgreen><include var=GPIONFCPICK></select></td><td colspan=12>PN532 NFC 绿色 LED</td></tr>
<tr><td><select name=nfccard><include var=GPIONFCPICK></select></td><td colspan=12>PN532 NFC 刷卡时闪烁的 LED</td></tr>
<tr><td><select name=nfcbaud>
<option value=0>9,600</option>
<option value=1>19,200</option>
<option value=2>38,400</option>
<option value=3>57,600</option>
<option value=4>115,200</option>
<option value=5>230,400</option>
<option value=6>460,800</option>
<option value=7>921,600</option>
<option value=8>1,288,000</option>
</select></td><td colspan=12>PN532 NFC 波特率</td></tr>
</if>
<tr><td><select name=gpstx onchange='F.submit();'><include var=GPIOREALPICK></select></td><td colspan=12>GPS Tx 引脚</td></tr>
<if not gpstx==->
<tr><td><select name=gpsrx><include var=GPIOREALPICK></select></td><td colspan=12>GPS Rx 引脚</td></tr>
<tr><td><select name=gpstick><include var=GPIOREALPICK></select></td><td colspan=12>GPS 秒脉冲引脚</td></tr>
</if>
<sql table=gpio where="pcb=$pcb" order=rgb,io,initname><set initinvert$gpio="$initinvert"><set initfunc$gpio="$initfunc">
<tr>
<td><input name=gpio type=hidden><select name=pin><include var=GPIONUMPICK></select></td>
<td><input name="initinvert$gpio" type=checkbox value=true title="反相"></td>
<td><input name="value0$gpio" size=5 value="$value0" placeholder="0 的名称"></td>
<td><input name="value1$gpio" size=5 value="$value1" placeholder="1 的名称"></td>
<td><select name=io><include var=GPIOIOPICK></select></td>
<if not ledr=- ledr='$ledg'><td><input name="rgb$gpio" value="$rgb" title="LED 编号" placeholder='LED' size=3></td></if><if else><input name="rgb$gpio" value="$rgb" type=hidden></if>
<td>默认：</td>
<td><select name=inittype><include var=GPIOTYPEPICK></select></td>
<td><if inittype=*I><select name=initfunc$gpio><include var=GPIOFUNCPICKI></select></if><if inittype=*O><select name=initfunc$gpio><include var=GPIOFUNCPICKO></select></if></td>
<td><input name="initname$gpio" value="$initname" size=10></td>
<td><input name="inithold$gpio" size=3 value="$inithold"> 毫秒</td>
<td><input name="initpulse$gpio" size=5 value="$initpulse"> ×0.1 秒，正数为脉冲接通，负数为脉冲断开</td>
</tr>
</sql>
<tr><td><input name=gpio type=hidden value=0><select name=pin><include var=GPIONUMPICK></select></td>
<td><input name=initinvert type=checkbox value=true title="反相"></td>
<td><input name="value0" size=5 value="" placeholder="0 的名称"></td>
<td><input name="value1" size=5 value="" placeholder="1 的名称"></td>
<td><select name=io><include var=GPIOIOPICK></select></td>
<if not ledr=- ledr='$ledg'><td><input name=rgb title="LED 编号" placeholder='LED' size=3></td></if><if else><input name=rgb type=hidden></if>
<td>默认：</td>
<td><select name=inittype><include var=GPIOTYPEPICK></select></td>
<td><i>添加后设置</i></td>
<td><input name=initname size=10 placeholder='新引脚'></td>
<td><input name=inithold size=3 placeholder="保持"> 毫秒</td>
<td><input name=initpulse size=5 placeholder="脉冲"> ×0.1 秒</td>
</tr>
</table>
</sql>
<input type=submit value="保存">
<IF not pcb=0><input type=submit value="复制" name=COPY></if>
<IF not pcb=0><input type=submit value="删除" name=DELETE><input type=checkbox name=SURE title='勾选以确认删除'></if>
</form>
<p>输入引脚会尽量启用上拉电阻（低电平有效的输入则启用下拉）。</p>
</if>
</sql>
'END'
