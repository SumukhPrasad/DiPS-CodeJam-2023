n=int(input())

matrix=[]

for i in range(n):
	matrix.append(list(map(int, input().strip().split())))
	
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
	
print("true" if isThereATarget() else "false")
