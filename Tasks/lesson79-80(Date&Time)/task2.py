# التكليف 02
# قم بطباعة التاريخ والوقت الخاص باليوم الحالي بأكثر من طريقة
# شاهد المثال لتفهم الفكرة
# # Today Is "2021, 8, 10"
#
# "2021-08-10"
# "Aug 10, 2021"
# "10 - Aug - 2021"
# "10 / Aug / 21"
# "10 / August / 2021"
# "Tue, 10 August 2021"
import datetime


print(dir(datetime))
today=datetime.date.today()
print(today)
print(today.strftime('"%b %d,%Y"'))
print(today.strftime('"%d - %b - %Y"'))
print(today.strftime('"%d / %b / %Y"'))
print(today.strftime('"%d / %B / %Y"'))
print(today.strftime('"%a, %d  %B  %Y"'))
