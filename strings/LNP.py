from itertools import combinations
def numeric_palindrome(*args):
	ls = [i for i in args]
	l = []
	for i in range(2 ,len(args)+1):
		l += list(combinations(ls , i))
	max_mul(l)
	
def max_mul(lst):
	temp = []
	multiplication = 1
	for i in lst:
		for j in i:
			multiplication *= j
		temp.append(multiplication)
	print listtemp





numeric_palindrome(57,62,23)

-- write your code in PostgreSQL 9.4
SELECT d.dept_id, count(*) as count, SUM(salary) as sum_of_salary from department d inner join employee e on d.dept_id = e.dept_id group by d.dept_id order by d.dept_id;