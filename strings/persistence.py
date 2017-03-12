def persistence(n):
	mul =1
	if len(str(n)) > 1:
		nw = cal(n)
		count = 1
		while len(nw) > 1:
			nw = cal (nw)
			count = count + 1
		print count
		
	else:
		print 0

def cal(news):
	mul=1
	for i in str(news):
		mul *= int(i)
	return str(mul) 


persistence(39)