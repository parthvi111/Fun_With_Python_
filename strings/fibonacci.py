fib = lambda y: y if y < 2 else fib(y - 1) + fib(y - 2)
mid = map(fib ,range(int(raw_input())))
print map(lambda x: x**3,mid)

