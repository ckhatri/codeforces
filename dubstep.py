# http://codeforces.com/problemset/problem/208/A

wubInput = raw_input() 
wubInput = wubInput.replace("WUB", ' ')
numSpaces = 0
pos = 0
notDone = True
while pos < wubInput and notDone:
	currChar = wubInput[pos]
	if currChar == " ":
		numSpaces += 1
	else:
		notDone = False
	pos += 1
print wubInput[numSpaces:]