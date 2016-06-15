# http://codeforces.com/problemset/problem/266/B

numKids, numSeconds = map(int, raw_input().split(" "))
originalLine = raw_input()
originalBools = [False] * numKids
posInArray = 0
for char in originalLine:
	if char == "B":
		originalBools[posInArray] = True
	posInArray += 1
for num in range(numSeconds):
	flip = False
	for num in range(0, numKids-1):
		if not flip:
			if originalBools[num]:
				if not originalBools[num + 1]:
					originalBools[num] = False
					originalBools[num + 1] = True
					flip = True
				else:
					flip = False
			else:
				flip = False
		else:
			flip = False
finalLine = ""
for person in originalBools:
	if person:
		finalLine += "B"
	else:
		finalLine += "G"
print finalLine