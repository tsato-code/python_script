import datetime

#
# 日付時刻の操作
#
in_datetime = '2018/06/01 22:50:31'
d = datetime.datetime.strptime(in_datetime,'%Y/%m/%d %H:%M:%S')
print('{}'.format(d.year))
print('{}'.format(d.month))
print('{}'.format(d.day))
print('{}'.format(d.hour))
print('{}'.format(d.minute))
print('{}'.format(d.second))



# 曜日計算
WEEK = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
print ("date {} ({})".format(d.date(), WEEK[d.weekday()]))


# 時刻加算
start = datetime.datetime.strptime(in_datetime, '%Y/%m/%d %H:%M:%S')
end = start + datetime.timedelta(hours=8) 
print("START {}".format( start.time() ))
print("  END {}".format( end.time() ))


"""
$ python test_datetime_day_of_week.py
date 2018-06-01 (Fri)
START 22:50:31
  END 06:50:31
"""