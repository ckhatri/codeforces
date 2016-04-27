# http://codeforces.com/problemset/problem/116/A

numStops = int(input())
maxNum = 0
currNum = 0
for stopNum in range(numStops):
	numOut, numIn = map(int, raw_input().split(" "))
	currNum -= numOut
	currNum += numIn
	if currNum > maxNum:
		maxNum = currNum
print maxNum
