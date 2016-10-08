def formula(xp,a,c,m):
	val = (a * xp) + c	# val = (a*xn + c)
	return val % m		# xn+1 = val mod m



def Generate(n,m):
	global a,c,x0
	store_x_values = list() #list stores previous x - values
	store_x_values.append(x0)
	n1 = list()
	for i in range(1,n):
		#print(store_x_values[i-1])
		get = formula(store_x_values[i-1], a, c, m)
		store_x_values.append(get)
		n1.append(get)
	hash_values[m] = n1 
		
x0 = 1
a = 2
c = 3
m = 5
hash_values = dict()
list_of_values = list() #list which stores values for every m

numbers = 20  #m - values
for i in range(m,numbers):
	Generate(numbers, i)
	if i == numbers - 1:
		for i in hash_values.keys():
			print(i," -> ", hash_values.get(i),end="\n")

