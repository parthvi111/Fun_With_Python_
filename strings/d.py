from itertools import combinations
def ladder1(lst):
		n =[]
		data = len(lst)
		new = []
		d ={}
		if len(lst[0]) == 1:
			if all(x == lst[0] for x in lst):
				return False
			else:
				return True
		
		ls = list(combinations(lst,2))
		for i in ls:
	   		ls1 = ['*' for k,l in zip(i[0],i[1]) if k != l]
	   		if len(ls1) == 1 :
					d[i[0]] = i[1]

		if len(d)>0:
			key, value = d.popitem()
			n.append(key)
			n.append(value)
			l =lst
			l.remove(key)
			l.remove(value)
			new = l
			print n
			print new
			for i in new:
				ls1 = ['*' for k,l in zip(i,n[0]) if k != l]
		   		if len(ls1) == 1 :
					n.insert(0,i)
					
			
			if len(n) == data:
				return True
			else:
				return False


#lst = ["aba", "bbb", "bab"] #false
#lst = ["ab", "bb", "aa"] # true
lst =["zzzzab", "zzzzbb", "zzzzaa"] #true
#lst = ["ab", "ad", "ef", "eg"] # false
#lst =["abc", "abx", "axx", "abc"] # false
#lst =["f", "g", "a", "h"] # true
#lst = ["q", "q"] # false
#lst =["abc", "abx", "axx", "abx", "abc"] #true


print ladder1(lst)