def calc(expr):
    stck = expr.split(" ")
    stack = []
    for i in stck:
    	if i == '*':
			x = stack.pop()
			y = stack.pop()
			stack.append(x * y)
		else:
			stack.append(float(i))	
	print stack

		
	

calc('5 4 *')
