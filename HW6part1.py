import psutil, datetime


html = open("CPUST.html", "w")

boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")

cpu_util = psutil.cpu_percent(interval = 1, percpu=True)

CPUT = []
for cpu in cpu_util:
    CPUT.append(cpu)

mem = psutil.virtual_memory()
THRESHOLD = 100*1024*1024 #100mb

mv = str(mem.available)
mu = str(mem.used)
mp = str(mem.percent)

s1 = "<td colspan='2' bgcolor = 'Blue' >"+boot_time+"</td>"
s2 = "<td bgcolor = 'Plum'>"+str(CPUT[0])+"%</td>"
s3 = "<td bgcolor = 'Plum'>"+str(CPUT[1])+"%</td>"
s4 = "<td bgcolor = 'Plum'>"+str(CPUT[2])+"%</td>"
s5 = "<td bgcolor = 'Plum'>"+str(CPUT[3])+"%</td>"
s6 = "<td bgcolor = 'Blue' colspan='2'>"+str(mv)+"</td>"
s7 = "<td colspan='2'>"+str(mu)+"</td>"
s8 = "<td bgcolor = 'Blue' colspan='2'>"+str(mp)+"</td>"
p = """<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 4.0 Transitional//EN'>
 <HTML>
 <HEAD>
 </HEAD>

 <BODY>
	<table>
	<tr>
		<td width='60%' bgcolor = 'Blue'>BOOT TIME</td>"""
p += s1

p += """
	</tr>
	<tr>
		<td rowspan='4'>CPU UTILIZATION</td>
		<td>CPU1</td>"""
p += s2
p += """
	</tr>
	<tr>
		<td>CPU2</td>"""
p += s3
p += """
	</tr>
	<tr>
		<td>CPU3</td>"""
p += s4
p += """
	</tr>
	<tr>
		<td>CPU4</td>"""
p += s5
p += """
	</tr>
	<tr>
		<td bgcolor = 'Blue'>AVAILBLE MEMORY</td>"""
p += s6
p += """
	</tr>
	<tr>
		<td>USED MEMORY</td>"""
p += s7
p += """
	</tr>
	<tr>
		<td bgcolor = 'Blue'>USED PERCENTAGE</th>"""
p += s8
p += """
	</tr>
	</table>
 </BODY>
</HTML>
"""
html.write(p)

html.close()
