import re
def abbreviate(s):
	lst =  re.findall(r"[\w]+",s)
	new_list = []
	for i in lst:
		length = len(i)
		new_list.append(i[0]+str(length-2)+i[length-1])
	print new_list
	



s = "elephant-rides are really fun!"
abbreviate(s)
