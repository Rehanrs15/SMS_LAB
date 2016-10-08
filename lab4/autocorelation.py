#check for autocorelation between random numbers
'''----
---generate N random numbers - > N
---start index - > i
--- lag - > L
-----'''

import random
import math
def CalculateM():
	global N,L
	v = N/L
	v1 = v - i - 1 			#formula to calculate M 
	return int(v1)			#----> (i + M + 1)*L < = N

Sum = 0	#this will store the summation of Rowcap
def RowCap(k,M):
	global i,RandomNumbers,Sum
	f1 = i + (k * M)
	f2 = i + (k + 1)* M
	Sum = Sum + (RandomNumbers[f1] - RandomNumbers[f2])
	

#this method will return Standard Deviation
def StandardDeviation(M):
	v1 = math.sqrt((13*M +7))		#formula to calculate standard Deviation	
	v2 = 12 * (M + 1)			#formula---> SQUAREROOT(13M + 1)/ 12*(m+1)
	return v1 / v2

#thsi methis will return test statistics value
def TestStatistics(r,s):
	return r/s


#this checks Z0 in range of -ZAlpha and +ZAlpha	
def CheckForValidity(A,Z):
	m_Z = -A
	p_Z = A
	if Z >= m_Z and Z <= p_Z:
		return 1
	else:
		return 0
	
N = 40
i = 2
L = 5
Alpha = 0.05
Z_Alpha = 1.96

RandomNumbers = [random.random() for i in range(N)] # this loop will generate N random numbers 1 <= VAL >= 0
print(RandomNumbers)
M = CalculateM()
for k in range(1,M+1):
	RowCap(k,M)

rowCap = ((1/(M+1)) * Sum) - 0.25  #final value of RwCap
SD = StandardDeviation(M) #Standard Devaition
Z0 = TestStatistics(rowCap,SD) 	#this is test statistics
print("Z0 ->",Z0)
Check = CheckForValidity(Z_Alpha,Z0)
if Check == 1:
	print("Accepted")
else:
	print("Not Accepted")


	
