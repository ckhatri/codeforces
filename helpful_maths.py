eq = raw_input("").split("+")
eq.sort()
result = ""
count = 0
for num in eq:
	result += num
	if count < len(eq) - 1:
		result += "+"
	count += 1
print result
