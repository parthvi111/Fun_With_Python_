def solution(A):
    # write your code in Python 2.7
    N = len(A)
    for p in range(1,N+1):
    	if sum(0,p,A) == sum(p+1,N,A):
    		return p


def sum(i,j,A):
	sum =0;
	for k in range(i,j):
		sum += A[k]
	return sum

print solution([-1,3,-4,5,1,-6,2,1])