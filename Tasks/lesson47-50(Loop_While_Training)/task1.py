# التكليف 01
# قم بعمل متغير بإسم num عبارة عن Input يقبل من الشخص رقم معين
# تأكد أن الرقم نوعه Int وأنه أكبر من 0 وإذا لم يكن أكبر من 0 قم بطباعة رسالة تفيد ذلك
# بعد إدخال الرقم قم بطباعة الرقم الأصغر منه مباشرة فالأصغر فالأصغر حتى تصل لرقم 1
# يجب عدم طباعة الرقم نفسه وعدم طباعة رقم 0
# إذا كانت الأرقام تحتوي على رقم 6 لا تطبعه من ضمن الأرقام
# بعد الإنتهاء من طباعة الأرقام قم بطباعة رسالة تفيد أن طباعة جميع الأرقام تمت بنجاح مع كتابة كم عدد الأرقام التي تم طباعتها
# Input

num = int(input('Enter your number'))
count = 0
# "Number 0 Is Not Larger Than 0"
while num > 0:
    num -= 1
    if num == 0:
        break
    print(f"# {num}")
    if num == 7 or num ==6:
        num -= 1
    count+=1
else:
    print('finally')

print(f'"{count if count != 0 else "wrong"} Numbers Printed ."')
# Needed Output
# 9
# 8
# 7
# 5
# 4
# 3
# 2
# 1
# "8 Numbers Printed Successfully."
