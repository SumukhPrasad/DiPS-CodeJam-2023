import os
from random import random
os.mkdir('./testCases')
os.mkdir('./testCases/input')
os.mkdir('./testCases/output')
import random

def solve(n, arr):
     s = []
     f = []

     for i in range(n):
          inputArr = list(map(int, arr[i].split()))
          s.append(inputArr[0])
          f.append(inputArr[1])

     conferences = []

     # The first conference is always selected
     i = 0
     conferences.append(i)

     # Consider rest of the conferences
     for j in range(n):

          # If this conference has start time greater than
          # or equal to the finish time of previously
          # selected conference, then select it
          if s[j] >= f[i]:
               conferences.append(j)
               i = j
     
     return len(conferences)

def getTestCase():
     numberOfActivities = random.randint(30,365)
     conferenceTimesIntegerStore = []
     for _ in range(numberOfActivities):
          #print(f"Activity {i+1}:")
          #conferenceTimes.append(input("Start time? ") + " " + input("End time? "))
          startT = random.randint(0,360)
          dur = random.randint(1,5)
          conferenceTimesIntegerStore.append([startT, startT+dur])
          
     conferenceTimesIntegerStore.sort(key=lambda x: x[1])

     conferenceTimes = [str(e[0]) + " " + str(e[1]) for e in conferenceTimesIntegerStore]

     
          
     return [str(numberOfActivities) + "\n" + "\n".join(conferenceTimes), str(solve(numberOfActivities, conferenceTimes))]

for i in range(0, 20):
     n = str(i).zfill(2)
     ioArr = getTestCase()


     inputFile = open(f'./testCases/input/input{n}.txt', 'a')
     inputFile.write(ioArr[0])
     inputFile.close()
     
     outputFile = open(f'./testCases/output/output{n}.txt', 'a')
     outputFile.write(ioArr[1])
     outputFile.close()

     print(f'Written case {n}.')

# def getTestCase():
#      numberOfActivities = int(input("Number of conferences? "))
#      conferenceTimes = []
#      for i in range(numberOfActivities):
#           print(f"Activity {i+1}:")
#           conferenceTimes.append(input("Start time? ") + " " + input("End time? "))
#           
#      return [str(numberOfActivities), "\n".join(conferenceTimes), str(solve(numberOfActivities, conferenceTimes))]