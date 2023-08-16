n=int(input())

grid=[]

for i in range(n):
	grid.append( list(map(int, input().strip().split())) )
	
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

print(sum([sum(i) for i in newGrid]))