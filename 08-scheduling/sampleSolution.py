# n --> Total number of conferences
# s[]--> An array that contains start time of all conferences
# f[] --> An array that contains finish time of all conferences
 
n = int(input())

s = []
f = []

for i in range(n):
     inputArr = list(map(int, input().split()))
     s.append(inputArr[0])
     f.append(inputArr[1])

conferences = []

# The first activity is always selected
i = 0
conferences.append(i)

# Consider rest of the conferences
for j in range(n):

     # If this activity has start time greater than
     # or equal to the finish time of previously
     # selected activity, then select it
     if s[j] >= f[i]:
          conferences.append(j)
          i = j
 
print(len(conferences))