import os
os.mkdir('./testCases')
os.mkdir('./testCases/input')
os.mkdir('./testCases/output')
import random


for i in range(0, 20):
	nthCase = str(i).zfill(2)
     
	l=[random.randrange(1, 100) for i in range(random.randrange(5, 100))]
	n=random.randrange(5, 10)

	metamorph=l

	for _ in range(n-1):
		next_metamorph=[]
		next_metamorph.append(metamorph[0])
	
		for num in metamorph:
			next_metamorph.append(next_metamorph[-1]+num)
		
		metamorph=next_metamorph
	

	inputFile = open(f'./testCases/input/input{nthCase}.txt', 'a')
	inputFile.write(" ".join(list(map(str, l)))+f"\n{n}")
	inputFile.close()
     
	outputFile = open(f'./testCases/output/output{nthCase}.txt', 'a')
	outputFile.write(" ".join(list(map(str, metamorph))))
	outputFile.close()

	print(f'Written case {nthCase}.')