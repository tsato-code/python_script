# lambda
square = lambda x: x**2
print(square(9))


# lambda + sorted
t = [(7, 1), (3, 4), (5, 0), (10, 2)]
t_sorted = sorted(t, key=lambda x: x[1])
print(t_sorted)


# lambda + map
r = [11, 22, 33, 44, 55]
r_square = list(map(lambda x: x**2, r))
print(r_square)

r_even = list(map(lambda x: True if x%2==0 else False, r))
print(r_even)


a = [0, 1, 2, 3, 4]
b = [10, 11, 12, 13, 14]
c = list(map(lambda x, y: x*y, a, b))
print(c)


# lambda + filter
s = [(1,2), (2,3), (3,4), (4,5), (5,6)]
s_filter = list(filter(lambda x: x[1]%2==0, s))
print(s_filter)


# lambda + recursive
fib = lambda n: n if n < 2 else fib(n-1) + fib(n-2)
print(fib(8))


"""
$ python test_lambda.py
81
[(5, 0), (7, 1), (10, 2), (3, 4)]
[121, 484, 1089, 1936, 3025]
[False, True, False, True, False]
[0, 11, 24, 39, 56]
[(1, 2), (3, 4), (5, 6)]
21
"""