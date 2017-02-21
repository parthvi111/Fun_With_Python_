def printer_error(s):
	lst=[]
	for i in s:
		if ord(i) not in range(ord('a'),ord('m')+1):
			lst.append(i)
	print (str(len(lst))+"/"+str(len(s)))

printer_error("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz")