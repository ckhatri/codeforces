# http://codeforces.com/problemset/problem/469/A
# broken tests?
import sys
numLevels = int(input())
levelsPPass = map(int, raw_input().split(" "))
levelsQPass = map(int, raw_input().split(" "))
pSet = set(levelsPPass[1:])
qSet = set(levelsQPass[1:])
pSet = pSet.union(qSet)
pSet.discard(0)
if len(pSet) == numLevels:
	print "I become the guy."
else:
	print "Oh, my keyboard!"