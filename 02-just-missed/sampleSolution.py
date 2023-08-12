import math

def generateFirstNPrimes(n):
	res=[]
	X = 0
	i = 2
	while True:
		flag=True
		if X==n:
			break
		
		for j in range(2, i//2+1):
			if i%j==0: 
				flag=False
				break
		if flag:
			res.append(i)
			X+=1
			
		i+=1
	return res
		
			
def modWithNegativeOne(dividend, divisor):
	rawMod=dividend%divisor
	return rawMod if rawMod-divisor != -1 else -1
	
def checkModulos(k,list_of_numbers):
	residues=[modWithNegativeOne(k,i) for i in list_of_numbers]
	return True if set(residues).issubset(set([-1,0,1])) else False
	
			
n=int(input())
primes=generateFirstNPrimes(n)
k=primes[-1]-1

while checkModulos(k, primes)==False:
	k+=1

print(k)