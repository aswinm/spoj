from datetime import datetime
day = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
for i in range(input()):
	x = map(int,raw_input().split())
	d = ""
	for j in x:
		d += str(j)+'-'
	d = d[:-1]
	d += " 12:00:00"
	dt = datetime.strptime(d,'%d-%m-%Y %H:%M:%S')
	n = datetime.isoweekday(dt)
	print day[n%7]

