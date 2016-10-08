sum = 0
def formula(observed,expected):
	global sum
	val = ((observed - expected)**2)/expected
	sum =sum + val
	
L = [[100,100],[96,100],[98,100],[85,100],[105,100],[93,100],[97,100],[125,100],[107,100],[94,100]]
for i in L:
	formula(i[0],i[1])
print("chi-square :",sum)
