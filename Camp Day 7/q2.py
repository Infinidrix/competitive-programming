
def fix_highway(length, good_days, bad_days):
	allowance = length // 2
	days = 0
	while length > 0:
		if length - good_days <= 0:
			#print("This is where 2")
			return days + length
		else:
			days += good_days
			length -= good_days
			
		if allowance == 0:
			temp = length // good_days
			temp += 1 if length % good_days != 0 else 0
			# print("this is temp", temp,"length", length, days)
			return days + temp * bad_days + length

		if length - bad_days <= 0: 
			if length <= allowance:
				# print("This is where")
				return days + length

			else:
				days += bad_days
				length -= allowance
				allowance = 0
		elif bad_days <= allowance:
			days += bad_days
			length -= bad_days
			allowance -= bad_days
		else:
			days += bad_days
			length -= allowance
			allowance = 0
	return days

useless = int(input())
for i in range(useless):
	n, g, b  = (int(i) for i in input().split())
	print(fix_highway(n, g, b))
