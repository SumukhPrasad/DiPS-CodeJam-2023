import os
os.mkdir('./testCases')
os.mkdir('./testCases/input')
os.mkdir('./testCases/output')

import random


for i in range(0, 20):
	nthCase = str(i).zfill(2)
     
	n=random.randrange(5, 100)

	grid=[[random.randrange(0, 2) for _ in range(n)] for _ in range(n)]
	
	newGrid = grid.copy()

	def safeCell(i, j):
		try:
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
		
		if grid[i][j]  == 1:
			if (total < 2) or (total > 3):
				newGrid[i][j] = 0
		else:
			if total == 3:
				newGrid[i][j] = 1
	
	inputGrid=""
	for line in newGrid:
		for cell in line:
			inputGrid+=f"{cell} "
		inputGrid+="\n"

	inputFile = open(f'./testCases/input/input{nthCase}.txt', 'a')
	inputFile.write(f"{n}\n{inputGrid}")
	inputFile.close()
     
	outputFile = open(f'./testCases/output/output{nthCase}.txt', 'a')
	outputFile.write(f"{sum([sum(i) for i in newGrid])}")
	outputFile.close()

	print(f'Written case {nthCase}.')