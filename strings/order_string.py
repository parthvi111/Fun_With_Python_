def order(sentence):
	if sentence == " ":
		return " "
	else:
		dic = {}
		lst = sentence.split(" ")
		for i in lst:
			check_digit = ''.join([j for j in list(i) if j.isdigit()])
			dic[check_digit] = i
		print ' '.join([values for key ,values in sorted(dic.items())])
		


sen1 = raw_input()
order(sen1)			

