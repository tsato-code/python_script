string1 = '左詰め'
string2 = '中央寄せ'
string3 = '右詰め'

print('{0:<10}'.format(string1))
print('{0:^10}'.format(string2))
print('{0:>10}'.format(string3))

string_list = [string1, string2, string3]
print('{0[0]:<10} {0[1]:^10} {0[2]:>10}'.format(string_list))
print('{0:<10} {1:^10} {2:>10}'.format(*string_list))

import datetime
d = datetime.datetime(2010, 7, 4, 12, 15, 58)
print('{:%Y-%m-%d %H:%M:%S}'.format(d))


"""
$ python test_format.py
左詰め
   中央寄せ
       右詰め
左詰め           中央寄せ           右詰め
左詰め           中央寄せ           右詰め
2010-07-04 12:15:58
"""