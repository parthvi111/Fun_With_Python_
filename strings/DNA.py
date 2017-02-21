import string
def DNA_strand(dna):
	translate_table = string.maketrans('ATCG','TAGC')
	return dna.translate(translate_table)


print DNA_strand('ATTGC')