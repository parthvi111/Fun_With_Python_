def autocorrect(input):
	case_cast = input.lower()
	lst = case_cast.split(" ")
	key = ["y","o","u"]
	for i in range(0,len(lst)):
		if lst[i] == 'u':
			lst[i] = "your sister"
		if "you" in lst[i]:
			for j in lst[i]:
				if j not in ["y","o","u"]:
					pass
				
			lst[i] = "your sister"



	print lst		





autocorrect('youuuuu are genious you youtube u U')