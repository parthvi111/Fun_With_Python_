def IQ_test(numbers):
	lst1 =[]
	lst2 = []
	val = map(int,numbers.split(" "))
	for i in val:
		 if i%2 == 0:
		 	lst1.append(i)
		 else:
		 	lst2.append(i)

	if len(lst1)<len(lst2):
		print lst1[0]
	else:
		element = lst2[0]
		print val.index(element)+1


IQ_test("2 4 7 8 10")