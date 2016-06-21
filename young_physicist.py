# http://codeforces.com/problemset/problem/69/A
# assume array only has 3 dimensions

NUM_DIMENSIONS = 3
numForces = int(input())
coordinates = [0] * NUM_DIMENSIONS
for force in xrange(0, numForces):
	forceCoordinates = map(int, raw_input().split(" "))
	for dimension in xrange(0, NUM_DIMENSIONS):
		coordinates[dimension] += forceCoordinates[dimension]

pos = 0
equilibrium = True
while equilibrium and pos < NUM_DIMENSIONS:
	if coordinates[pos] != 0:
		equilibrium = False
	pos += 1
if equilibrium:
	print "YES"
else:
	print "NO"