# http://codeforces.com/problemset/problem/118/A

vowels = ["a", "e", "i", "o", "u", "y"]
word = raw_input()
result = ""
for letter in word:
	lowerCase = letter.lower()
	if lowerCase not in vowels:
		result += "." + lowerCase
print result


