def calLS():
	global roo 
	return roo/(1-roo)


def calLq(ls):
	global roo
	return ls - roo 

def calWs(ls):
	global lamda
	return ls/lamda

def calWq(lq):
	global lamda
	return lq/lamda
	
lamda = int(input())
mui = int(input())
roo = lamda/mui
Ls = calLS()
Lq = calLq(Ls)
Ws = calWs(Ls)
Wq = calWq(Lq)
print("LS=",Ls,"LQ=",Lq,"WS=",Ws,"WQ=",Wq)
