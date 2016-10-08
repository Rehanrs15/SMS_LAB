fp=open("rndOut.csv","r")
ln=[float(i) for i in fp.read().split(",")[1:]]
ln.sort()
n=len(ln)
dMax=0.0
for i in range(1,n):
	dp=float(i)/n-ln[i]
	dn=ln[i]-float(i-1)/n
	if dp>dMax:
		dMax=dp
	if dn>dMax:
		dMax=dn
dAlpha=1.36/(n**0.5)
if dMax>dAlpha:
	print "The System Was Rejected Pending Evidence"
else:
	print "The System Was Accepted Pending Evidence"