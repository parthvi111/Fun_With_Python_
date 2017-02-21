from itertools import permutations
def sum_pairs(ints, s):
	print [(ints.index(a),ints.index(b)) for a,b in permutations(ints,2) if a+b == s]

sum_pairs([10, 5, 2, 3, 7, 5], 10)