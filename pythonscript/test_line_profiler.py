import sys
print("recursion limit: {}".format(sys.getrecursionlimit()))
# sys.setrecursionlimit(11)

@profile
def f(x):
	if x==1:
		return 1
	else:
		return f(x-1)

print(f(9))



"""
$ kernprof -l test_line_profiler.py
recursion limit: 3000
1
Wrote profile results to test_line_profiler.py.lprof

$ python -m line_profiler test_line_profiler.py.lprof
Timer unit: 3.01874e-07 s

Total time: 1.41881e-05 s
File: test_line_profiler.py
Function: f at line 5

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     5                                           @profile
     6                                           def f(x):
     7         9         11.0      1.2     23.4         if x==1:
     8         1          1.0      1.0      2.1                 return 1
     9                                                  else:
    10         8         35.0      4.4     74.5                 return f(x-1)
"""