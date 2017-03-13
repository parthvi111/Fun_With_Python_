from itertools import combinations
def ladder1(lst):
	if len(lst[0]) == 1 and len(set(lst)) == len(lst):
		return True
	new = []
	d ={}
	ls = list(combinations(lst,2))
	for i in ls:
   		ls1 = ['*' for k,l in zip(i[0],i[1]) if k != l]
   		if len(ls1) == 1 :
				d[i[0]] = i[1]
	print d	
   	for k,v in d.items():
   		if len(new) > 0:
   			if new[-1] in d.keys():
   				new.append(d[k])
   		if len(new) == 0:
	   		if k not in new:
	   			new.append(k)
	   		if v not in new:
	   			new.append(v)
   	if  len(new) == len(lst):
         return True
	else:
         return False

#lst = ["aba", "bbb", "bab"] #false
#lst = ["ab", "bb", "aa"] # true
#lst =["zzzzab", "zzzzbb", "zzzzaa"] #true
#lst = ["ab", "ad", "ef", "eg"] # false
#lst =["abc", "abx", "axx", "abc"] # false
#lst =["f", "g", "a", "h"] # true
#lst = ["q", "q"] # false
lst =["abc", "abx", "axx", "abx", "abc"] #true


print ladder1(lst)