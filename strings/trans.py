from string import maketrans
val=int(raw_input())
value ='0:032b'.format(val)
trnastab = maketrans('01','10')
print int(value.translate(trnastab),2)
