import os
os.mkdir('./testCases')
os.mkdir('./testCases/input')
os.mkdir('./testCases/output')

from math import *
import random


for i in range(20):
	nthCase = str(i).zfill(2)
	
	n=random.sample(range(1,10**5+1), random.randrange(1, 10**2))

	number_of_primes = 0
	composites = []
	def isprime(x):
		for i in range(2, x//2+1):
			if x%i == 0:
				return False
		return True
	def list_gcd(nums):
		if len(nums) == 1:
			return nums[0]
		div = gcd(nums[0], nums[1])
		if len(nums) == 2:
			return div
		for i in range(1, len(nums) - 1):
			div = gcd(div, nums[i + 1])
			if div == 1:
				return div
	def GIF(x):
		return int(floor(x))
	for i in n:
		if isprime(i):
			number_of_primes+=1
		else:
			composites.append(i)		
	s=0
	if number_of_primes!=0 and len(composites)!=0:
		s=(number_of_primes/list_gcd(composites))*len(n)
	
	
	inputFile = open(f'./testCases/input/input{nthCase}.txt', 'a')
	inputFile.write(" ".join(list(map(str, n))))
	inputFile.close()
     
	outputFile = open(f'./testCases/output/output{nthCase}.txt', 'a')
	outputFile.write(f'{GIF(s)}')
	outputFile.close()

	print(f'Written case {nthCase}.')