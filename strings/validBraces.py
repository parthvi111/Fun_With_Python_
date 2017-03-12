def validBraces(string):
		openers = ['(','[','{']
		closers = [')',']','}']
		lst =[]

		for c in string:
			if c in openers:
				lst.append(c)
			else:
				if len(lst) != 0:
					if lst[-1] == '{' and c == '}':
						lst.pop()
					elif lst[-1] =="(" and c == ")":
						lst.pop()
					elif  lst[-1] == "[" and c == "]":
						lst.pop()
					else:
						pass

		if len(lst) == 0:
			return True
		else:
			return False

print validBraces("([{}])")