from collections import defaultdict

n=int(input())

matrix=[]

for i in range(n):
	matrix.append(list(map(int, input().strip().split())))
	
d = defaultdict(list)

for y in range(n):
	for x in range(n):
		d[x-y].append(matrix[y][x])
		
for i in sorted(d):
	print(" ".join(map(str,d[i])))