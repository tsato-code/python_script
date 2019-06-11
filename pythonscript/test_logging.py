import logging
import time
from contextlib import contextmanager


@contextmanager
def timer(name, logger=None, level=logging.DEBUG):
    print_ = print if logger is None else lambda msg: logger.log(level, msg)
    t0 = time.time()
    print_(f'[{name}] start')
    yield
    print_(f'[{name}] done in {time.time() - t0:.0f} s')


def time_sleep():
	for i in range(10):
		time.sleep(0.2)


with timer('time_sleep'):
	time_sleep()
