positions = raw_input()
checkOnes = True
continousCount = 0
for position in positions:
	currBool = checkOnes
	if position == "0":
		checkOnes = False
	else:
		checkOnes = True
	if currBool != checkOnes:
		continousCount = 1
	else:
		continousCount += 1
	if continousCount == 7:
		break
if continousCount == 7:
	print "YES"
else:
	print "NO"

