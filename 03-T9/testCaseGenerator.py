import os
import string
import random
os.mkdir('./testCases')
os.mkdir('./testCases/input')
os.mkdir('./testCases/output')


for i in range(0,20):
	nthCase = str(i).zfill(2)
	
	chars=["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
	word=''.join(random.choices('abcdefghijklmnopqrstuvwxyz ', k=random.randrange(1, 10**5+1)))
	charcodes= []
	for c in word:
		if c==" ":
			charcodes.append('0')
			continue
		index=[idx for idx, s in enumerate(chars) if c in s][0]
		repeats=chars[index].index(c)+1
		charcodes.append(str(str(index+2)*repeats))
		
	print(charcodes)
	
	inputFile = open(f'./testCases/input/input{nthCase}.txt', 'a')
	inputFile.write(" ".join(charcodes).strip())
	inputFile.close()
     
	outputFile = open(f'./testCases/output/output{nthCase}.txt', 'a')
	outputFile.write(f'{word}')
	outputFile.close()

	print(f'Written case {nthCase}.')