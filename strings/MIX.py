from collections import Counter
def mix(s1, s2):
	ans_lst1 =[]
	ans_lst2 =[]
	ans_lst3 =[]
	s1 = ischar(s1)
	s2 = ischar(s2)
	
	for key , value in s1.items():
		if key in s2.keys():
			if value == s2[key] and value !=1 :
				
				ans_lst1.append('=:'+ key*value) 
			elif value > s2[key] and value >1 :
				
				ans_lst2.append('1:'+key*value)
			elif value < s2[key] and s2[key] > 1:
				
				ans_lst3.append('2:'+ key*s2[key])
		else:
			if value >1 :
				ans_lst2.append('1:'+key*value)

	for k , v in s2.items():
		if k not in s1.keys():
			if v > 1 :
				ans_lst3.append('2:'+ k *s2[k])




	ans = sorted(ans_lst2, key=lambda x: x[-1]) + sorted(ans_lst3, key=lambda x: x[-1]) + sorted(ans_lst1, key=lambda x: x[-1])
	print '/'.join(sorted(ans,key =len , reverse = True))
	

def ischar(st):
	lst = [i for i in st if i.islower()]
	d = dict(Counter(lst))
	return d


s1 = " In many languages"
s2 = " there's a pair of functions"
mix(s1,s2)
