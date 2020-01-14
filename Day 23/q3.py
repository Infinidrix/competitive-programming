import math
def next_prime(num):
	return num + 1
		
def find_all_factors(num):
	factors = [1, 1]
	last_tried = 1
	max_limit = int(math.sqrt(num)) + 1
	while num > 1 and last_tried <= max_limit:
		last_tried = next_prime(last_tried)
		addable = 1
		while True:
			if num % last_tried == 0:
				addable *= last_tried
				num = num // last_tried
			else:
				if addable != 1: factors.append(addable)
				break
	if num > 1:
		factors.append(num)
	return factors
	
def correct_factors(factors):
	corrected = [1]
	for i in factors:
		if corrected[-1]%i == 0:
			corrected[-1] *= i
		else:
			corrected.append(i)
	return corrected
	
def distribute_factors(num, factors, answers = []):
	if len(answers) < len(factors):
		max1 = distribute_factors(num, factors, answers + [1])
		max2 = distribute_factors(num, factors, answers + [0])
		return min(max1, max2)
	else:
		num1 = 1
		for i in range(len(answers)):
			if answers[i]: num1 *= factors[i]
		if num1 == 0: return num
		num2 = num // num1
		return max(num1, num2)

def main(number):
	answer = distribute_factors(number, find_all_factors(number))
	return str(number//answer) + " " + str(answer)


number = int(input())
print(main(number))