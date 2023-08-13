import os
os.mkdir('./testCases')
os.mkdir('./testCases/input')
os.mkdir('./testCases/output')

import random
import string

	
	
	
for i in range(20):
	nthCase = str(i).zfill(2)
	
	s=''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=random.randrange(1, 10*3)))
	res=""
	substrings = [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]

	for substring in substrings:
		possibleRepeat=substring*2
		if possibleRepeat in substrings:
			res="true"
			break
	else:
		res="false"
	
	
	inputFile = open(f'./testCases/input/input{nthCase}.txt', 'a')
	inputFile.write(s)
	inputFile.close()
     
	outputFile = open(f'./testCases/output/output{nthCase}.txt', 'a')
	outputFile.write(f'{res}')
	outputFile.close()

	print(f'Written case {nthCase}.')