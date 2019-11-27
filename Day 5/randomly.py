from random import randint

def randomizer(ranges = 10000):
	rand = [i for i in range(ranges)]
	for i in range(len(rand)):
		chosen = randint(0, len(rand) - 1)
		rand[i], rand[chosen] = rand[chosen], rand[i]
	return rand