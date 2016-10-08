import math 
def funcMM1inf(la,mu):
    ro = la/mu
    Ls = ro/(1-ro)
    Lq = Ls - ro
    ws = Ls/la
    wq = Lq/la
    print "M/M/1 - infinite/infinite -:"
    print "LS : ",Ls
    print "Lq : ",Lq
    print "Ws : ",ws
    print "Wq : ",wq

def funcMM1fin(la,mu,N):
    ro = la/mu 
    ro_n1 = math.pow(ro,N+1)
    ro_n = math.pow(ro,N)
    p0 = (1 - ro)/(1-ro_n1)
    pn =  ro_n * p0
    laeff = la*(1-pn)
    a = (N+1)*ro_n
    b = 1 + N*ro_n1
    Ls = (ro*(b - a))/((1-ro)*(1-ro_n1))
    Lq = Ls - laeff/mu
    ws = Ls / laeff
    wq = Lq / laeff
    print "M/M/1 - N/infinite -:"
    print "LS : ",Ls
    print "Lq : ",Lq
    print "Ws : ",ws
    print "Wq : ",wq

def funcMMcinf(la,mu,c):
    ro = la/mu
    n = 0
    p = 0
    while(n<c):
        a = math.pow(ro,c)/math.factorial(c)
        b = 1/(1- ro/c)
        p = p + ((math.pow(ro,n)/math.factorial(n)) + (a*b))
        n = n + 1
    p0 = math.pow(p,-1)
    Lq = math.pow(ro,c+1)*p0 / (math.factorial(c-1) * math.pow(c-ro,2))
    Ls = Lq + ro
    ws = Ls / la
    wq = Lq / la
    print "M/M/c - infinite/infinite -:"
    print "LS : ",Ls
    print "Lq : ",Lq
    print "Ws : ",ws
    print "Wq : ",wq

def funcMMcfin(la,mu,c,N):
    ro = la/mu
    n = 0
    p = 0
    while(n<N-c+1):
        a = math.pow(ro,c)* math.pow((1 - ro/c),N-c+1)
        b = math.factorial(c) * (1-ro/c)
        p = p + ((math.pow(ro,n)/math.factorial(n)) + (a/b))
        n = n+1
    p0 = math.pow(p,-1)
    pn = (math.pow(ro,N) / (math.factorial(c) * math.pow(c,N-c))) * p0
    laeff = la * (1 - pn)
    e = (1 - math.pow(ro/c,N-c+1)) - (N-c+1)
    d = ((1-ro/c) * math.pow(ro/c,N-c))/math.pow((c-ro),2)
    Lq = -((math.pow(ro,c+1)* p0 / math.factorial(c-1) ) * (e * d))
    Ls = Lq + laeff/mu
    ws = Ls / laeff
    wq = Lq / laeff
    print "M/M/c - N/infinite -:"
    print "LS : ",Ls
    print "Lq : ",Lq
    print "Ws : ",ws
    print "Wq : ",wq
      

funcMM1inf(8.0,9.0)    
funcMM1fin(8.0,9.0,10)
funcMMcinf(10.0,6.0,2)
funcMMcfin(10.0,6.0,2,7)








