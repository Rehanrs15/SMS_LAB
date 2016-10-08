def PO(roo):
	global N
	return (1-roo)/(1-(roo**N+1))
	
def PN(r,po):
	return r*po
	
def calLS(r):
	global N
	num = r * (1 + (N * (r**N+1)) - ((N+1)*(r**N)))
	den = (1-r) * (1 - (r **N+1))
	return num/den
		
	
	
	
	
lamda = int(input())
mui = int(input())
N = int(input())
roo = lamda/mui

P0 = PO(roo)
Pn = PN(roo,P0)

Ls = calLS(roo)
Lq = calLq(Ls)
Ws = calWs(Ls)
Wq = calWq(Lq)
