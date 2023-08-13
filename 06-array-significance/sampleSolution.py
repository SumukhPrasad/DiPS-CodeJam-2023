from math import *

n=list(map(int, input().strip().split()))

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
	
print(GIF(s))