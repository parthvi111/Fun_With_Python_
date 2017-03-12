def calc(expr):
	if expr == "":
		return 0
	s0 = [(i) if i.isdigit() else i for i in expr.split(" ")]
	st = [float(i) if i.isdigit() else i for i in expr.split(" ")]

	s = []
	for i in st:
			

		if i == '*':
				first = s.pop()
				second = s.pop()
				s.append(second * first)
		elif i == '+':
				first = s.pop()
				second = s.pop()
				s.append(first+second)
		elif i == '-':
				first = s.pop()
				second = s.pop()
				s.append(second - first)
		elif  i == '/':
				first = s.pop()
				second = s.pop()
				s.append(second / first)
		else:
				s.append(i)
	if len(s) > 1:
		return type(max(s0))
	return s

		
	

print calc('1 2 3 + +')
