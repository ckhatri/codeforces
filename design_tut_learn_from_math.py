# http://codeforces.com/problemset/problem/472/A

def isPrime(number):
	if number % 2 == 0:
		return False
	for x in range(3, int(number**0.5) + 1, 2):
		if number % x == 0:
			return False
	return True

inputNumber = int(input())
firstVal = 3
notDone = True
# if the first val isn't prime, and the second val isn't then they're composite.
while notDone and firstVal < (inputNumber / 2):
	firstVal += 1
	if not isPrime(firstVal):
		secondVal = inputNumber - firstVal
		if not isPrime(secondVal):
			notDone = False
print "%d %d" % (firstVal, secondVal)
