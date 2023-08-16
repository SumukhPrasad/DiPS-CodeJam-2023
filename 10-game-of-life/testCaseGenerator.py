import os
os.mkdir('./testCases')
os.mkdir('./testCases/input')
os.mkdir('./testCases/output')

import random


for i in range(0, 20):
	nthCase = str(i).zfill(2)
     
	n=random.randrange(3, 100)

	grid=[[random.randrange(0, 2) for _ in range(n)] for _ in range(n)]
	
	newGrid = [[grid[i][j] for j in range(n)] for i in range(n)]

	def safeCell(i, j):
		try:
			assert i>-1 and j>-1 # prevent back-indexes
			return grid[i][j]
		except:
			return 0

	for i in range(n):
		for j in range(n):
			total = 0
			cells_to_check=[
				[i-1, j-1],
				[i-1, j],
				[i-1, j+1],
				[i, j-1],
				[i, j+1],
				[i+1, j-1],
				[i+1, j],
				[i+1, j+1],
			]
			for cell in cells_to_check:
				total+=safeCell(cell[0], cell[1])
		
			if safeCell(i, j):
				if (total < 2) or (total > 3):
					newGrid[i][j] = 0
			else:
				if total == 3:
					newGrid[i][j] = 1
	
	inputGrid=""
	for line in grid:
		for cell in line:
			inputGrid+=f"{cell} "
		inputGrid+="\n"
		
	sum_newGrid=sum([sum(i) for i in newGrid])

	inputFile = open(f'./testCases/input/input{nthCase}.txt', 'a')
	inputFile.write(f"{n}\n{inputGrid}")
	inputFile.close()
	
	outputFile = open(f'./testCases/output/output{nthCase}.txt', 'a')
	outputFile.write(f"{sum_newGrid}")
	outputFile.close()

	print(f'Written case {nthCase}.')