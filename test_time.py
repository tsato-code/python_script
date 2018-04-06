import time

start = time.time()
time.sleep(1)
elapsed = time.time() - start
print(elapsed, "[sec]")

"""
$ python test_time.py
1.0009441375732422 [sec]
"""
