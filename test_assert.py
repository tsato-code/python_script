import sys

args = sys.argv[1:]
x = int(args[0])
y = int(args[1])

assert x < y, "{} < {}: False".format(x, y)
print("{} < {}: True".format(x, y))


"""
$ python test_assert.py 10 5
Traceback (most recent call last):
  File "test_assert.py", line 7, in <module>
    assert x < y, "{} < {}: False".format(x, y)
AssertionError: 10 < 5: False
"""