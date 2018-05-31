import datetime

yobi = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

in_date = '2016/07/30'
a = datetime.datetime.strptime(in_date,'%Y/%m/%d')
print ("{} {}".format(in_date, yobi[a.weekday()]))