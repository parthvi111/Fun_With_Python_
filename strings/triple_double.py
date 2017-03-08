def triple_double(num1, num2):
    lst = []
    for i in range(0,len(num1)-1):
        if len(lst)<2:
            lst.append(num1[i])
        else:
            if lst[-1] != num1[i]:
                lst.append(num1[i])
            else:
                if lst[-1] == lst[-2]:
                    x = num1[i]
                else:
                    lst.append(num1[i])
    lst2 =[]
    if x in num2:
        y = num2.index(x)
    if  num2[y] == num2[y+1]:
        print 1
    else:
        print 0
    


        








    

triple_double("1233345","23345")
        