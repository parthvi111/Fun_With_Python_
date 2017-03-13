from itertools import groupby

def binary_gap(N):
	word = str("{0:b}".format(N))
	print word
	lst = [len(list(g)) for k, g in groupby(word) if k == '0'  ]
	if len(lst)>0:
		return max(lst)
	return 0

print binary_gap(6)