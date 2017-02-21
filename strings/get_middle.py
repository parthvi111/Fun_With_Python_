def get_middle(s):
    length = len(s)
    if length<=2:
        return s
    else:
    	res = length // 2
    	if length%2 == 0:
        	return s[res-1]+s[res]
        else:
        	return s[res]

print get_middle("ooetoo")