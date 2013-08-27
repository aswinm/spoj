t = input()
d = { 'o' : 0 , 'h' : 0 , 't': 0 }
for i  in range(t):
	x = raw_input()
	if x == '1/2':
		d['h'] += 1
	elif x == '3/4':
		d['t'] += 1
	else:
		d['o'] += 1
count = 1
if d['t']>d['o']:
	count += d['o']
	d['t']-= d['o']
	count += d['t']
	if d['h']%2:
		count += (d['h']/2)+1
	else:
		count += d['h']/2
elif d['t'] == d['o']:
	count += d['t']
	count += d['h']/2
	if d['h']%2:
		count += 1
else:
	count += d['t']
	d['o'] -= d['t']
	d['h'] += d['o']/2
	count += d['h']/2
	if d['h']%2 or d['o']%2:
		count += 1
print count
print ""
	
