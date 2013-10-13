s = ["TTT","TTH","THT","THH","HTT","HTH","HHT","HHH"]
for i in range(input()):
	d = {"TTT":0,"TTH":0,"THT":0,"THH":0,"HTT":0,"HTH":0,"HHT":0,"HHH":0}
	n = input()
	x = raw_input()
	for j in range(38):
		d[x[j:j+3]] += 1
	print n,
	for j in s:
		print d[j],
	print ""



