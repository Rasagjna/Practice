import datetime

mytime=datetime.time(2,20)# 2am ,20min past 2am
print(mytime.minute)
print(mytime.hour)
print(mytime)
#hour min sec microsec...
today=datetime.date.today()
print(today)# yyyy mm dd
print(today.year)
print(today.month)
print(today.day)
print(today.ctime())
from datetime import datetime
mydatetime=datetime(2021,10,3,14,20,1)
print(mydatetime)
mydatetime=mydatetime.replace(year=2020)
print(mydatetime)
#DATE
from datetime import date
date1=date(2021,11,3)
date2=date(1990,11,3)

result=date1-date2
print(type(result))
print(result.days)
datetime1=datetime(2021,11,3,22,0)
datetime2=datetime(2020,11,3,12,0)
re=datetime1-datetime2
print(re)
print(re.seconds)
print(re.total_seconds())