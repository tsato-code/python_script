from time import sleep
from tqdm import tqdm
 
 
for i in tqdm(range(20)):
	sleep(0.1)

[sleep(0.1) for i in tqdm(range(20))]

"""
$ python test_tqdm.py
100%|████████████████████████████████████████| 20/20 [00:02<00:00,  9.96it/s]
100%|████████████████████████████████████████| 20/20 [00:02<00:00,  9.96it/s]
"""