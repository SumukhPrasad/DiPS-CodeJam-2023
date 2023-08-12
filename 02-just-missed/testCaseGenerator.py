import os
os.mkdir('./testCases')
os.mkdir('./testCases/input')
os.mkdir('./testCases/output')

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
	
			
numbers=[3,4,5,6,7]

for i in range(0, 5):
	nthCase = str(i).zfill(2)
	n=numbers[i]
	primes=generateFirstNPrimes(n)
	k=primes[-1]-1

	while checkModulos(k, primes)==False:
		k+=1
	
	inputFile = open(f'./testCases/input/input{n}.txt', 'a')
	inputFile.write(f'{n}')
	inputFile.close()
     
	outputFile = open(f'./testCases/output/output{n}.txt', 'a')
	outputFile.write(f'{k}')
	outputFile.close()

	print(f'Written case {nthCase}.')