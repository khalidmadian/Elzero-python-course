# التكليف 01
# قم بطباعة رسالة فيها عدد الأيام ما بين التاريخ التالي “2021, 6, 25” واليوم
# شاهد المثال لتفهم الفكرة
# # The Date Is "2021, 6, 25"
# # Today Is "2021, 8, 10"
#
# # Message Will Be
# "Days From 2021-06-25 To 2021-08-10 Is => 46"

import datetime

the_date = datetime.datetime(2021,8,10)

current_date=datetime.datetime.now()
print(current_date-the_date)