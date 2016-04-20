# http://codeforces.com/problemset/problem/158/A

numParticipants, posToBeat = map(int, raw_input().split(" "))
listOfScores = map(int, raw_input().split(" "))
# need to be equal to or beat this person's score to advance.
scoreToBeat = listOfScores[posToBeat-1]
numMoveOn = 0
for score in listOfScores:
	# score must be postive, and be >= kth persons score.
	if score >= scoreToBeat and score > 0:
		numMoveOn += 1
print numMoveOn