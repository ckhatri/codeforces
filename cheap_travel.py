numTrips, numMultRides, singleCost, multCost = map(int, raw_input().split(" "))
costPerTripSpecial = multCost
costPerTripRegular = numMultRides * singleCost
if costPerTripSpecial < costPerTripRegular:
	numMultTics = numTrips / numMultRides
	numRegTics = numTrips % numMultRides
	cost = 0
	if singleCost < multCost:
		cost = numMultTics * multCost + numRegTics * singleCost
		if numMultRides > numTrips:
			cost = multCost
	else:
		if numRegTics == 0:
			cost = (numMultTics) * multCost
		else:
			cost = (numMultTics + 1) * multCost
	print cost
else:
	print numTrips * singleCost

