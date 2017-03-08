def reverseWords(string):
	
	
    if string == "":
       print {}
    else:
    	dic = {}
    	for i in set(string):
       		dic[i] = string.count(i)
    print dic
   
	



reverseWords('aba')