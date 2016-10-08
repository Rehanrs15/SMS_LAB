import random,math
import matplotlib.pyplot as plt
def generateRandomNumbers(N):
	global R
	'''
		this function will generate N random numbers	
	'''
	for i in range(N):
		R.append(random.random())
		
def formula(r):
	'''
		general formula
		Xi = -(1/lambda)*(ln(1-Ri))
	'''
	global l_lambda
	n1 = (1/l_lambda)
	n2 = math.log(1 - r)
	return n1 * n2


def formula1(r):
	'''
		general formula
		Ri(b-a)+a = X
	'''
	a = 10
	b= 20
	return r*(b-a) + a
	
def inverseVariatesForExponentDistribution(R):
	'''
		this function stores inverse variates for each random number
	'''
	global X
	for i in range(len(R)):
		X.append(formula(R[i]))
	print("using Exponent distribution")
	for i in X:
		print(i)
	#graph  X-axis ->Random Variates, Y-axis -> Random Number
	plt.plot(R,X)
	plt.show()
	
def inverseVariatesForUniformDistribution(R):
	'''
		this function stores inverse variates for each random number
	'''
	global X1
	for i in range(len(R)):
		X1.append(formula1(R[i]))
	print("\nusing Uniform distribution")
	for i in X1:
		print(i)
	#graph  X-axis ->Random Variates, Y-axis -> Random Number
	plt.plot(R,X1)
	plt.show()
	
	
R = [0.1306,0.0422,0.6597,0.7965,0.7696] #random numbers
X = list() #inverse variates ForExponentDistribution
X1 = list() #inverse variates ForUniformDistribution
l_lambda = 0.5
#N = int(input())
#generateRandomNumbers(N)  #generates N random numbers
inverseVariatesForExponentDistribution(R)
inverseVariatesForUniformDistribution(R)
