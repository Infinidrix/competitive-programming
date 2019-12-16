def add_one(num1, num2, carry):
	summ = num1 + num2 + carry
	if summ < 0:
		add = str(summ + 10)
		carry = -1
	elif summ >= 10:
		add = str(summ - 10)
		carry = 1
	else:
		add = str(summ)
		carry = 0
	return add, carry


def adder(num1, num2):
	prefix1 = ""
	prefix2 = ""
	if num1[0] == "-":
		prefix1 = "-"
		num1 = num1[1:]
	if num2[0] == "-":
		prefix2 = "-"
		num2 = num2[1:]
	bigger_num = max(len(num1), len(num2))
	smaller_num = min(len(num1), len(num2))
	if len(num1) < len(num2):
		num1, num2 = num2, num1
		prefix1, prefix2 = prefix2, prefix1
	carry = 0
	summation = []
	for i in range(1, bigger_num + 1):
		if i > smaller_num:
			summ, carry = add_one(0, int(prefix1 + num1[-i]), carry)
			summation.insert(0, summ)
		else:
			summ, carry = add_one(int(prefix1 + num1[-i]), int(prefix2 + num2[-i]), carry)
			summation.insert(0, summ)
	if carry == 1:
		summation.insert(0, str(carry))
	elif (carry < 0):
		summation = summation[1:]
		return ["-"] + adder("1" + "0" * len(summation), ["-"] + summation)
	while summation[0] == "0" and len(summation) != 1:
		summation.pop(0)
	return "".join(summation)


def multiply(num1, num2):
	multip = "0"
	counter = 0
	neg_flag = False
	if num1[0] == "-":
		neg_flag = not neg_flag
		num1 = num1[1:]
	if num2[0] == '-':
		neg_flag = not neg_flag
		num2 = num2[1:]
	for i in range(len(num1), 0, -1):
		temp = ""
		carry = 0
		for j in range(len(num2), 0, -1):
			temp_mul = int(num1[i - 1]) * int(num2[j - 1]) + carry
			temp = str(temp_mul % 10) + temp
			carry = temp_mul // 10
		if carry != 0:
			temp = str(carry) + temp
		multip = adder(multip, temp + "0" * counter)
		counter += 1
	if neg_flag and multip != "0":
		multip = "-" + multip
	return multip


def divide(a, b):  # a/b
	a += "000"
	result = ""
	temp = ""
	while a:
		temp += a[0]
		a = a[1:]
		if len(temp) < len(b):
			result += "0"
			continue
		elif temp < b and len(temp) == len(b):
			result += "0"
			continue
		temp_value = 0
		while len(temp) >= len(b):
			if temp < b and len(temp) == len(b):
				break
			temp_value += 1
			temp = str(int(temp) - int(b))
		result += str(temp_value)
	result = result.lstrip("0")
	return result[0:-3]+'.'+result[-3:]

if __name__ == "__main__":
	num1 = input("Enter the first number:")
	num2 = input("Enter the second number:")
	print(divide(num1, num2))
