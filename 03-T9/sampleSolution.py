presses=input().strip().split(" ")

res=""

chars=["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

for i in presses:
	char=" "
	if int(i[0])>0:
		char=chars[ (int(i[0])-2) ][ (len(i)-1) ]
	res+=char
	
print(res)

