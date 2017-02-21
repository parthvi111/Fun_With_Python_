def filter_list(l):
	return [x for x in l if type(x) is not str]



print filter_list([2,1])
