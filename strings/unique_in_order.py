def unique_in_order(s):
	lst =[]
	
	for i in s:
		if not lst:
			lst.append(i)
		else:
			val = lst[-1]
			if val != i:
				lst.append(i)
	print lst

unique_in_order([1,2,2,3,3])