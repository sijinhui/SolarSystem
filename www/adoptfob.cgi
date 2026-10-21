#!../login/loggedin /bin/csh -f
can --redirect --organisation='$USER_ORGANISATION' --site='$USER_SITE' adoptfob
if($status) exit 0
source ../setcan

echo "Content-encoding: none" # so no deflating and hence no caching for interactive status
xmlsql -C -d "$DB" head.html - foot.html << 'END'
<h1>🙋 绑定门卡</h1>
<sql table="device LEFT JOIN aid USING (aid)" where="(nfcadmin='true' AND device.site=$USER_SITE OR nfctrusted='true') AND online IS NOT NULL"><set found=1></sql>
<if found>
 <if not fob><p>请先读取门卡 ID。</p></if>
 <form name=f method=post style="display:inline;">
 <select name=device>
 <sql table="device" where="(nfcadmin='true' AND device.site=$USER_SITE  OR nfctrusted='true') AND online IS NOT NULL" ORDER=nfctrusted>
 <option value="$device"><output name=devicename blank="$device"></option>
 </sql>
 </select>
 <input type=submit name=IDENTIFY value="读取门卡 ID">
 <input type=hidden name=fob>
 <if not IDENTIFY fob not fob="">
  <set mem><set capacity><sql table=fob where="fob='$fob'"><set foundfob=1><if mem><set mem="$mem"></if><if capacity><set capacity="$capacity"></if></sql>
  <if not foundfob><p>抱歉，系统无法识别门卡 <output name=fob>。所有门卡都必须先由系统管理员初始化后才能绑定。详情请联系系统管理员 <sql table=user where="admin='true'" limit=1 order="rand()"><output name=username></sql>。</p></if>
  <if else>
   <h2>🔑 已识别门卡：<output name=fob href="editfob.cgi/$fob"></h2>
   <if IDENTIFIED><sql table=foborganisation where="fob='$fob' AND organisation=$USER_ORGANISATION"><set fobname="$fobname"></sql></if>
   <sql table="fobaid LEFT JOIN aid USING (aid) LEFT JOIN access USING (access)" WHERE="fob='$fob' AND access.organisation=$USER_ORGANISATION AND access.site=$USER_SITE">
   <p>已绑定到 <output name=aidname> <output name=accessname></p>
   </sql>
   <input name=fobname size=15 maxlength=15 placeholder="名称" autofocus><if mem> 剩余 <output name=mem> 字节</if><br>
   <select name=aid><sql table=aid where='site=$USER_SITE'><option value=$aid><output name=aidname></option></sql></select>
   <select name=access><sql table=access where='site=$USER_SITE'><option value=$access><output name=accessname></option></sql></select>
   <input name=ADOPT type=submit value="绑定门卡">
   <if USER_ADMIN=true><br><input name=FORMAT type=submit value="格式化"></if>
  </if>
 </if>
 <if device><ul id=status></ul></if>
 </form>
</if>
<if else>
 <p>当前没有可用于绑定门卡的受信任在线设备。</p>
</if>
'END'

if($?IDENTIFY) then
	echo "<script>e=document.createElement('li');e.textContent='等待刷卡';document.getElementById('status').append(e);</script>"
	setenv fob `message --device="$device" --fob-identify --silent`
	if("$fob" == "") then
		echo "<script>e=document.createElement('li');e.textContent='失败';document.getElementById('status').append(e);</script>"
	else
		echo "<script>f.fob.value='$fob';e=document.createElement('input');e.type='hidden';e.name='IDENTIFIED';f.append(e);f.submit();</script>"
	endif
	exit 0
endif
if($?ADOPT) then
	message --device="$device" --fob-adopt="$fob" --aid="$aid" --access="$access" --status=status --silent --fob-name="$fobname" --organisation="$USER_ORGANISATION"
	exit 0
endif
if($?FORMAT) then
	can --redirect admin
	if($status) exit 0
	if($?hardformat) then
		message --device="$device" --fob-format="$fob" --status=status --silent
	else
		message --device="$device" --fob-format="$fob" --status=status --silent
	endif
	exit 0
endif
