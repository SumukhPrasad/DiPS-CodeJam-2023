import os
os.mkdir('./testCases')
os.mkdir('./testCases/input')
os.mkdir('./testCases/output')

cases=[[8,2,2],[20,5,4],[100,12,12],[300,11,11],[340,15,8],[300,36,24]]


for i in range(0,len(cases)):
	nthCase = str(i).zfill(2)
	
	d = cases[i][0]
	l_x, l_y = cases[i][1],cases[i][2]

	max_die_count = 0
	best_gx = 0
	best_gy = 0
	radius = d // 2

	for g_x in range(l_x):
		for g_y in range(l_y):
			die_count = 0
			for x1 in range(g_x - radius, radius, l_x):
				x2 = x1 + l_x
				for y1 in range(g_y - radius, radius, l_y):
					y2 = y1 + l_y
					if (x1 * x1 + y1 * y1 <= radius**2 and
						x2 * x2 + y2 * y2 <= radius**2 and
						x1 * x1 + y2 * y2 <= radius**2 and
						x2 * x2 + y1 * y1 <= radius**2):
						die_count += 1
			if die_count > max_die_count:
				max_die_count = die_count
				best_gx = g_x
				best_gy = g_y
	
	inputFile = open(f'./testCases/input/input{nthCase}.txt', 'a')
	inputFile.write(f'{d}\n{l_x} {l_y}')
	inputFile.close()
     
	outputFile = open(f'./testCases/output/output{nthCase}.txt', 'a')
	outputFile.write(f'{max_die_count}')
	outputFile.close()

	print(f'Written case {nthCase}.')