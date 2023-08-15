import os
os.mkdir('./testCases')
os.mkdir('./testCases/input')
os.mkdir('./testCases/output')
import random


for i in range(0, 20):
	nthCase = str(i).zfill(2)
     
	n=random.randrange(3, 101)

	matrix=[[random.randrange(1, 10) for _ in range(n)] for _ in range(n)]
	
	def insertTarget():
		i,j=0,0
		if n>3:
			i,j= [random.randrange(0,n-3),random.randrange(0,n-3)]
		
		bounding_box_value=random.randrange(5, 10)
		
		for r in range(i, i+3):
			for c in range(j, j+3):
				matrix[r][c]=bounding_box_value
				if r==i+1 and c==j+1:
					matrix[r][c]=random.randrange(1, bounding_box_value)
	
	if random.randrange(0, 2)!=0:
		insertTarget()
	
	def safeCell(i, j):
		try:
			assert i>-1 and j>-1 # prevent back-indexes
			return matrix[i][j]
		except:
			return None
		
	def checkEquality(arr):
		if None in arr:
			return False
		else:
			if len(set(arr))==1:
				return True
		return False
	
	def isThereATarget():
		for i in range(n):
			for j in range(n):
				bounding_cells = [
					safeCell(i-1, j-1),
					safeCell(i-1, j),
					safeCell(i-1, j+1),
					safeCell(i, j-1),
					safeCell(i, j+1),
					safeCell(i+1, j-1),
					safeCell(i+1, j),
					safeCell(i+1, j+1),
				]
			
				if checkEquality(bounding_cells) and bounding_cells[0]!=matrix[i][j]:
					return True
		return False
	
	inputGrid=""
	for line in matrix:
		for cell in line:
			inputGrid+=f"{cell} "
		inputGrid+="\n"
	

	inputFile = open(f'./testCases/input/input{nthCase}.txt', 'a')
	inputFile.write(f"{n}\n{inputGrid}")
	inputFile.close()
     
	outputFile = open(f'./testCases/output/output{nthCase}.txt', 'a')
	outputFile.write("true" if isThereATarget() else "false")
	outputFile.close()

	print(f'Written case {nthCase}.')