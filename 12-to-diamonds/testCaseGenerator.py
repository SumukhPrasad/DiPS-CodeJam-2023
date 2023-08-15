import os
os.mkdir('./testCases')
os.mkdir('./testCases/input')
os.mkdir('./testCases/output')

from collections import defaultdict
import random

for i in range(0, 20):
	nthCase = str(i).zfill(2)
     
	
	n=random.randrange(3, 101)

	matrix=[[random.randrange(1, 10) for _ in range(n)] for _ in range(n)]
	
	d = defaultdict(list)

	for y in range(n):
		for x in range(n):
			d[x-y].append(matrix[y][x])
	
	inputGrid=""
	outputGrid=""
	
	for line in matrix:
		for cell in line:
			inputGrid+=f"{cell} "
		inputGrid+="\n"
	
	for i in sorted(d):
		outputGrid+=" ".join(map(str,d[i]))
		outputGrid+="\n"
	
	outputGrid=outputGrid.strip()
	

	inputFile = open(f'./testCases/input/input{nthCase}.txt', 'a')
	inputFile.write(f"{n}\n{inputGrid}")
	inputFile.close()
     
	outputFile = open(f'./testCases/output/output{nthCase}.txt', 'a')
	outputFile.write(outputGrid)
	outputFile.close()

	print(f'Written case {nthCase}.')