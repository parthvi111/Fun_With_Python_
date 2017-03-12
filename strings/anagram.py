from collections import Counter
def anagrams(word, words):
	new_list = []
	for i in words:
		if len(word) == len(i) and Counter(word) == Counter(i):
			new_list.append(i)
	return new_list
	
print anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])		

