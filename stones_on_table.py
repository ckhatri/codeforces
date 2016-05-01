# http://codeforces.com/problemset/problem/266/A
numRocks = int(input())
orderRocks = raw_input()
RED_ROCK = 1
BLUE_ROCK = 2
GREEN_ROCK = 3
resultingString = ""
lastRock = ""
for rock in orderRocks:
	# if the current rock doesn't equal the most recent rock in the string, add it, update.
	if rock != lastRock:
		resultingString += rock
	lastRock = resultingString[len(resultingString)-1]
# difference in result and original is the number removed
print numRocks - len(resultingString)