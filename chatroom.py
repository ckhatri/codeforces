# http://codeforces.com/problemset/problem/58/A

input_string = raw_input()
input_string.lower()
helloStr = "hello"
charLookingForPos = 0 #position to get the char we're looking for
charLookingFor = ''
pos = 0
while charLookingForPos < 5 and pos < len(input_string):
	charLookingFor = helloStr[charLookingForPos] #what are we looking for?
	charIn = input_string[pos] #what are we at?
	if charIn == charLookingFor: #if equal, then find the next letter
		charLookingForPos += 1
	pos += 1 #check next char in input string
# we've found all 5 so we're good, else no.
if charLookingForPos == 5:
	print "YES"
else:
	print "NO"
