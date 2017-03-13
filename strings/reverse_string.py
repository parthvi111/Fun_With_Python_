def reverse_string(value):
	lst = value.split(" ")
	print ' '.join(list(reversed(lst)))
	print ' '.join([item for item in lst[::-1]])

val = raw_input()
reverse_string(val)
