code = raw_input()
ops = ["H", "Q", "9"]
notFound = True
opNum = 0
while notFound and opNum < len(ops):
	currOp = ops[opNum]
	if currOp in code:
		print "YES"
		notFound = False
	opNum += 1
if notFound:
	print "NO"

