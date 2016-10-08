L = list()
def k_plus(i,N,R):
	val_p = (i/N) - R
	k_minus(i,N,R,val_p)
	
def k_minus(i,N,R,val_p):
	val_m = R - ((i - 1)/N)
	global L
	L.append([val_p,val_m])

Random = [0.1,0.2,1,0.66,0.99,0.33,1.0,0.88,0.3332,.445]
N = 5
for i in range(1,len(Random)+1):
	k_plus(i,N ,Random[i-1])

#DMax = float('-inf')
V = list()
for i in L:
	V.append(sum(i))
DMax = max(V)
print(V)
print("Dmax - ",DMax)
if DMax <= 0.565:
	print("Accept")
else:
	print("reject")
#print(L)	
