# http://codeforces.com/problemset/problem/158/B

numGroups = int(input())
numTaxis = 0
groupList = map(int, raw_input().split(" "))
ones = 0
twos = 0
threes = 0
fours = 0
for numKids in groupList:
	if numKids == 1:
		ones += 1
	elif numKids == 2:
		twos += 1
	elif numKids == 3:
		threes += 1
	else:
		fours += 1
# fours need own taxi no matter what
numTaxis += fours
numThreeOnePairs = 0
# add all the threes, either they get paired up or they go alone.
# then you just need to update the ones appropriately
numThreesMinusOne = threes-ones
numTaxis += threes
if threes >= ones:
	ones = 0
else:
	ones -= threes
# how many twos can you pair up?
numTwoPairs = twos / 2
numTaxis += numTwoPairs
# updated twos count
twos -= (numTwoPairs * 2)
# if you have a single two left, you can add and fill in with ones, so subtract ones amount appropriately
if twos == 1:
	numTaxis += 1
	if ones > 1:
		ones -= 2
	elif ones == 1:
		ones -= 1
# at this point if you have any ones, then you need to find how many can fit into one taxi, then all the left go into the other
if ones > 0:
	numFourOnesPairs = ones / 4
	numTaxis += numFourOnesPairs
	ones -= numFourOnesPairs * 4
	# taxi for the rest unless you're at zero then you're done!!
	if ones > 0:
		numTaxis += 1
print numTaxis















