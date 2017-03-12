from itertools import groupby
from operator import itemgetter
def  prison(n, m, h, v):
	ls = []
	ls1 =[]
	for k,g in groupby(enumerate(h) ,lambda (i,x):i-x):
		ls.append(map(itemgetter(1),g))
	for k,g in groupby(enumerate(v) ,lambda (i,x):i-x):
		ls1.append(map(itemgetter(1),g))
	return (max([len(i) for i in ls ])+1) * (max([len(i) for i in ls1 ])+1)
	

print prison(4,3,[1,2,3],[1,2])