l=list(map(int, input().strip().split()))
n=int(input())

metamorph=l

for _ in range(n-1):
	next_metamorph=[]
	next_metamorph.append(metamorph[0])
	
	for num in metamorph:
		next_metamorph.append(next_metamorph[-1]+num)
		
	metamorph=next_metamorph
	
print(" ".join(list(map(str, metamorph))))