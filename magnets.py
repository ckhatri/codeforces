numInputs = int(input())
first = True
matching = ""
currCount = 0
for numberInput in xrange(0, numInputs):
	numInput = raw_input()
	if first:
		matching = numInput
		first = False
		currCount += 1
	if not numInput == matching:
		currCount += 1
		matching = numInput
print currCount
