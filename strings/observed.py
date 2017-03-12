from itertools import product
def get_pins(observed):
	d = { 0: '08' , 1:'124' , 2:'1235' , 3:'236' , 4 :'1457' ,5:'24568',6:'3569',7:'748', 8:'7895',9:'968'}
	st = []
	for i in observed:
		if int(i) in d.keys():
			st.append(list(d[int(i)]))
	l = list(product(*st))
	return [("%s"*len(x)%x).strip() for x in l]

print get_pins('369')

