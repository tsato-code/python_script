import glob
 
path_list = glob.glob('test*')
print(path_list)


"""
$ python test_glob.py 
['test_sys_args.py', 'test_time.py', 'test_tempfile.py', 'test_multiprocessing.py', 'test_os_walk.py', 'test_bm.py', 'test_prim.py', 'test_glob.py', 'test_argparse.py']
"""