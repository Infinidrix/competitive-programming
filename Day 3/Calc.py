from divide import *

def substract(num1, num2):
	return add(num1, "-"+num2)

oper_dict = {"+":adder, "-":substract, "*":multiply, "/":divide}
expr = input().split()

print(oper_dict[expr[1]](expr[0], expr[2]))
