#http://codeforces.com/problemset/problem/82/A

import math

nthPerson = int(input())
totalPeople = 5
expCount = 0
# simply keep reducing where the nth person is by increasing totalPeople
while nthPerson > totalPeople:
	nthPerson -= totalPeople
	totalPeople *= 2
	expCount += 1
#multNum gets you how many of each person there is
multNum = math.pow(2, expCount)
#person in line gives the cutoff.
personInLine = nthPerson / multNum
if personInLine <= 1:
	print "Sheldon"
elif personInLine <= 2:
	print "Leonard"
elif personInLine <= 3:
	print "Penny"
elif personInLine <= 4:
	print "Rajesh"
else:
	print "Howard"
