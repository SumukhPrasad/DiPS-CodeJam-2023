s=input().strip()

substrings = [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]

for substring in substrings:
	possibleRepeat=substring*2
	if possibleRepeat in substrings:
		print("true")
		break
else:
	print("false")