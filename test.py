# ['', 'Hicoder', '2019年06月29日10:17', '']
# ['', '读芯术', '2019年06月29日12:00', '']
# ['', 'python大大', '2019年06月27日19:35', '']
# ['', 'python大大', '2019年06月29日11:37', '']
# # ['', 'Excel函数编程可视化', '2019年06月27日06:50', '']
l='2019年06月27日06:50'
import time,datetime
p=datetime.date.today()
p=p.strftime("%Y-%m-%d")
print(type(p),p)
import time
import re
timeStamp = 1557502800
timeArray = time.localtime(timeStamp)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print(type(otherStyleTime))
import time



pattern=re.compile("((([0-9]){4})年([0-9]{2}|[1-9]))月([0-9]{2}|[1-9])日")
matcher = pattern.search(l)
op=matcher.group(0)

publish_Time = op
array = time.strptime(publish_Time, u"%Y年%m月%d日")
publishTime = time.strftime("%Y-%m-%d", array)
print(publishTime)


def compare_time(time1,time2):
    s_time = time.mktime(time.strptime(time1,'%Y-%m-%d'))
    e_time = time.mktime(time.strptime(time2,'%Y-%m-%d'))
    print(type(s_time),e_time)
    return int(s_time) - int(e_time)

result = compare_time(publishTime,p)
print(result)
