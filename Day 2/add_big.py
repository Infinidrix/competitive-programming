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
	for i in range(1, bigger_num+1):
		if i > smaller_num:
			summ, carry = add_one(0, int(prefix1 + num1[-i]), carry)
			summation.insert(0, summ)
		else:
			summ, carry = add_one(int(prefix1 + num1[-i]), int(prefix2 + num2[-i]), carry)
			summation.insert(0, summ)
	if carry == 1:
		summation.insert(0, str(carry))
	elif(carry<0):
		summation = summation[1:]
		return ["-"]+adder("1"+"0"*len(summation), ["-"]+summation)
	while summation[0] == "0":
		summation.pop(0)
	return "".join(summation)


num1 = input("Enter the first number:")
num2 = input("Enter the second number:")
print(adder(num1, num2))
