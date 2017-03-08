
def solution(s):
	new_list =[]	
	if len(s) != 0:
		lst = [i for i in s]
		
		st =""
		for i in lst:
			if len(st)<2:
				st += i
			else:
				new_list.append(st)
				st =""
				st += i
		new_list.append(st.ljust(2,'_'))
		print new_list
	print new_list

solution('')