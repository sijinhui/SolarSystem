#!../login/loggedin /bin/csh -f
can --redirect --organisation='$USER_ORGANISATION' admin
if($status) exit 0
source ../setcan

done:
echo "Content-encoding: none" # so no deflating and hence no caching for interactive status
xmlsql -C -d "$DB" head.html - foot.html << 'END'
<h1>初始化门卡</h1>
<form method=post>
设备：<select name=device><sql table=device where="nfctrusted='true' AND online IS NOT NULL"><set found=1><option value="$device"><output name=devicename blank="未命名"> <output name=address></option></sql></select>
<if found><set found><input type=submit value="初始化门卡"></if>
<if else><p>没有可用于初始化门卡的在线设备</p></if>
</form>
<if device><ul id=status></ul></if>
<if else><p>仅适用于全新空白门卡。</p></if>
'END'
if($?device) then
	message --device="$device" --fob-provision --status=status --silent
endif

