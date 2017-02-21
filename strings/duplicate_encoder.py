from collections import Counter
def duplicate_counter(word):
	word = word.lower()
	counter = Counter(word)
 	return ''.join(('(' if counter[c] == 1 else ')') for c in word)

print duplicate_counter("((((((")

