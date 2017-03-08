def is_merge(s,part1,part2):
	lst=[i for i in s]
	lst2 =[]
	for i in part1+part2:
		if i in lst:
			lst.remove(i)
		else:
			lst2.append(i)	

	
	if len(lst2)>0:
		print "True"

	





s="codewars"
part1="codeabc"
part2="warsxyz"
is_merge(s,part1,part2)