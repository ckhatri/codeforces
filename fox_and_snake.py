# http://codeforces.com/problemset/problem/510/A

n, m = map(int, raw_input().split(" "))
snakeDefault = ""
spaceDefaultLeft = ""
spaceDefaultRight = ""
for numCols in range(0, m):
	snakeDefault += "#"
	spaceDefaultLeft += "."
	spaceDefaultRight += "."
spaceDefaultLeft = "#" + spaceDefaultLeft[1:]
spaceDefaultRight = spaceDefaultRight[:(m-1)] + "#"
result = ""
leftSpace = False
for lineNum in range(0, n):
	if lineNum % 2 == 1:
		if leftSpace:
			result += spaceDefaultLeft
		else:
			result += spaceDefaultRight
		leftSpace = not leftSpace
	else:
		result += snakeDefault
	if lineNum < n-1: 
		result += "\n"
print result