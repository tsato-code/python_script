import datetime

in_datetime = '2018/06/01 22:50:31'


# 曜日計算
WEEK = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
d = datetime.datetime.strptime(in_datetime,'%Y/%m/%d %H:%M:%S')
print ("date {} ({})".format(d.date(), WEEK[d.weekday()]))


# 時刻加算
start = datetime.datetime.strptime(in_datetime, '%Y/%m/%d %H:%M:%S')
end = start + datetime.timedelta(hours=8) 
print("START {}".format( start.time() ))
print("  END {}".format( end.time() ))
