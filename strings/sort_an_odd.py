def sort_an_odd(lst):
	if len(lst) >0:
		lst1 =[]
		for c in range(0,len(lst)):
			 if lst[c]%2 != 0:
			 	lst1.append(lst[c])
			 	lst[c] = ''
		lst1.sort()
		for k in range(0,len(lst)):
			if lst[k] == '':
				lst[k] = lst1[0]
				lst1.remove(lst1[0])
		print lst
	else:
		print []


sort_an_odd([5, 3, 1, 8, 0])