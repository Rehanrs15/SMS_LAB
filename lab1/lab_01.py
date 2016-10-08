import math,random

def init():
	fighter[0.2343] = 0.2343

def distanceFormula(xa,xb,ya,yb):
	x = (xa - xb)**2
	y = (ya - yb)**2
	val = math.sqrt(x+y)
	return val

bomber = dict()
fighter = dict()
vf = 30
#RESULT VALUE
res = 0.1

init()
for i in range(1,20):
	x = random.random()
	y = random.random()
	bomber[float(format(x,".4f"))] = float(format(y,".4f"))
count = 0
while True:
	x1 = list(fighter.keys())[0]
	y1 = list(fighter.values())[0]
	for i in bomber.keys():
		x2 = i
		y2 = bomber.get(i)
		result = distanceFormula(x1,x2,y1,y2)
		print(result)
		if result <= res:
			print("bomber shot")
			break
		else:
			cos = (y2 - y1)/result
			sin = (x2 - x1)/result
			x1 = x1 + (vf * cos)
			x2 = y1 + (vf * sin)
		count= count + 1	
		if count == 19:
			print("bomber escaped")
			break
	break
	
		
	






