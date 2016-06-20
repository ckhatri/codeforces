# http://codeforces.com/problemset/problem/337/A

numKids, numPresents = map(int, raw_input().split(" "))
presentValues = map(int, raw_input().split(" "))
presentValues.sort()
startPos = 0
endPos = numKids - 1
minVal = presentValues[len(presentValues)-1] - presentValues[0]
notDone = True
while notDone:
	lowestVal = presentValues[startPos]
	highestVal = presentValues[endPos]
	difference = highestVal - lowestVal
	if minVal > difference:
		minVal = difference
	startPos += 1
	endPos += 1
	if endPos == len(presentValues):
		notDone = False
print minVal