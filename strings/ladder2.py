def ladder1(s , e, lst):
	new_lst1 = []
	new_lst1.append(s)
	
	for word in lst:
		if len(new_lst1)>0:
			last_value = new_lst1[len(new_lst1)-1]
			ans = [j for j in range(len(last_value)) if last_value[j] != word[j]]
			ans2 = [k for k in range(len(word)) if word[k]!= e[k]]
			if len(ans) == 1:
				new_lst1.append(word)
			if len(ans2) == 1:
				break;
	new_lst1.append(e)		
	print new_lst1



start ="hit"
end ="cog"
lst =["hot","dot","dog","lot","log"]
ladder1(start ,end , lst)