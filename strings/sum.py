def  summation(numbers):
    sum = 0
    for i in numbers:
    	sum += int(i)
    print sum	
	    
N = int(raw_input())
values = []
for i in range(N):
    values.append(raw_input())

summation(values)




		if i == "+":
    		x = stack.pop()
    		y = stack.pop()
    		stack.append(x+y) 
        if i == "-":
	    	x = stack.pop()
	    	y = stack.pop()
	    	stack.append(y-x)
	    if i == "/":
			x = stack.pop()
			y = stack.pop()
			stack.append(y/x)