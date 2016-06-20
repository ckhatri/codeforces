# http://codeforces.com/problemset/problem/119/A

def gcd(a, b):
	while b:
		a, b = b, a % b
	return a
simon, antisimon, heap = map(int, raw_input().split(" "))

keepPlaying = True
simonsTurn = True
while keepPlaying:
	numToTake = 0
	# if simons turn find gcd of simon, else antisimon
	if simonsTurn:
		numToTake = gcd(heap, simon)
	else:
		numToTake = gcd(heap, antisimon)
	#someone lost, figure out who and print and stop. 
	# if its simons turn he lost antisimon wins!
	if heap < numToTake:
		if simonsTurn:
			print "1"
		else:
			print "0"
		keepPlaying = False
	# else update and keep playing
	heap -= numToTake
	simonsTurn = not simonsTurn


