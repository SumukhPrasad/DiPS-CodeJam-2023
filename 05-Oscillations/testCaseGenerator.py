import os
os.mkdir('./testCases')
os.mkdir('./testCases/input')
os.mkdir('./testCases/output')

import math
import itertools
signum = lambda z : int(z/math.fabs(z))
cases = [
[1, 3, 5, 8, 6, 4, 2, 3, 5, 7, 6, 4, 2, 5, 7, 9, 6, 4, 2],
[1, 3, 5, 7, 6, 4, 5, 7, 9, 8, 6, 4, 2, 3, 5],
[2, 3, 6, 4, 2, 3, 7, 5, 3, 4, 6],
[3, 6, 4, 8, 5, 7, 3, 5, 2],
[8],
[1, 3, 5, 7],
[4, 5, 7, 6, 8, 9],
[6, 4, 2, 3, 5, 4, 2],
[8, 5, 3, 2, 4, 6, 5, 3, 2, 5, 7],
[1, 5, 10, 19, 15, 13, 8, 13, 18, 23, 19, 18, 14],
[15, 14, 17, 16, 19, 18],
[12, 16, 19, 15, 18, 19]
]

for i in range(len(cases)):
	nthCase = str(i).zfill(2)
	
	l=cases[i]
	deltas=[l[i+1]-l[i] for i in range(0, len(l)-1)]
	delta_signs=[signum(i) for i in deltas]
	lengths_of_groups = [len([*y]) for x, y in itertools.groupby(delta_signs)]

	res= "true" if len(set(lengths_of_groups))==1 else "false"
	
	
	inputFile = open(f'./testCases/input/input{nthCase}.txt', 'a')
	inputFile.write(" ".join(list(map(str, l))))
	inputFile.close()
     
	outputFile = open(f'./testCases/output/output{nthCase}.txt', 'a')
	outputFile.write(f'{res}')
	outputFile.close()

	print(f'Written case {nthCase}.')