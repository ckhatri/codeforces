#http://codeforces.com/contest/1/problem/A

import math

sideN, sideM, areaFlag = map(float, raw_input().split(" "))
#get numNeeded on width wise, round up
numNeededWidth = math.ceil(sideN / areaFlag)
#get numNeeded on length
numNeededLength = math.ceil(sideM / areaFlag)
# multiply
numNeeded = int(numNeededWidth*numNeededLength)
print numNeeded
