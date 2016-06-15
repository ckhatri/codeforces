# http://codeforces.com/problemset/problem/266/B

numKids, numSeconds = map(int, raw_input().split(" "))
originalLine = raw_input()
#create an array, False = girls, True = Boys, goes through and sets correctly
originalBools = [False] * numKids
posInArray = 0
for char in originalLine:
	if char == "B":
		originalBools[posInArray] = True
	posInArray += 1
# for number seconds
for num in range(numSeconds):
	#check to see if you've already flipped, if so don't do anything
	flip = False
	for num in range(0, numKids-1):
		if not flip:
			#if a boy, check if next is a girl, if it is then flip
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
#rewrite
for person in originalBools:
	if person:
		finalLine += "B"
	else:
		finalLine += "G"
print finalLine