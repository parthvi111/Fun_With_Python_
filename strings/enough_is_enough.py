def delete_nth(order , max_e):
	lst = []
	for i in order:
		if lst.count(i)<max_e:
			lst.append(i)
		


	print map(int,lst)			


input1 = raw_input().split(' ')
N = int(raw_input())
delete_nth(input1 , N)
