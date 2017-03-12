import re
def to_camel_case(text):
	t = re.split(r'[-_]+',text)
	

	st =' '.join(t).title().replace(' ','')

	if len(st) > 0:
		if t[0][0].islower():
			print st[0].lower() + st[1:]
		else:
			print st
	else:
		pass
		



to_camel_case("the_cat-was_Pippi")