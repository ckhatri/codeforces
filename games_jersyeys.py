# http://codeforces.com/problemset/problem/268/A

numTeams = int(input())
listOfJerseys = []
count = 0
for teamNum in range(0, numTeams):
	jerseyList = map(int, raw_input().split(" "))
	listOfJerseys.append(jerseyList)
for homeTeamNum in range(0, numTeams):
	homeTeamJerseys = listOfJerseys[homeTeamNum]
	homeTeamJerseyNum = homeTeamJerseys[0]
	for awayTeamNum in range(0, numTeams):
		if not homeTeamNum == awayTeamNum:
			awayTeamJerseys = listOfJerseys[awayTeamNum]
			awayTeamJerseyNum = awayTeamJerseys[1]
			if homeTeamJerseyNum == awayTeamJerseyNum:
				count += 1
print count