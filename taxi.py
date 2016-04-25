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
# if num three groups - ones group is >= 0 then you can pair that many up
numThreesMinusOne = threes-ones
if numThreesMinusOne >= 0:
	numTaxis += threes
	#print "NUM THREE PAIRS ARE: %d" % numThreesMinusOne
	ones = 0
else:
	numTaxis += threes
	ones -= threes
	#print "ONE GREATER THAN THREE SO ONES LEFT IS %d" % ones
# how many twos can you pair up?
numTwoPairs = twos / 2
numTaxis += numTwoPairs
#print "NUM TWO PAIRS ARE: %d" % numTwoPairs
# updated twos count
twos -= (numTwoPairs * 2)
# if you have a single two left, you can add and fill in with ones, so subtract ones amount appropriately
numTaxis += 1
#print "SINGLE TWO"
if ones > 1:
	ones -= 2
elif ones == 1:
	ones -= 1
#print "NUMS ONES LEFT IS: %d" % ones
# at this point if you have any ones, then you need to find how many can fit into one taxi, then all the left go into the other
if ones > 0:
	numFourOnesPairs = ones / 4
	#print "NUM FOUR ONE PAIRS IS %d:" % numFourOnesPairs
	numTaxis += numFourOnesPairs
	ones -= numFourOnesPairs * 4
	if ones > 0:
		#print "NUM ONES LEFT BY THEMSELVES IS %d" % ones
		numTaxis += 1
print numTaxis















