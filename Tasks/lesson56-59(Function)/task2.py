# التكليف 02
# قم بعمل Function تقوم بعمل عمليات حسابية بإسم addition
# ال Function تقبل عدد غير معلوم من ال Parameters
# كل ما عليك هو إيجاد حاصل جمع جميع الأرقام التي يتم تمريرها لل Function
# إذا كان الرقم 10 من ضمن الأرقام لا تقم بإضافته للعملية الحسابية
# إذا كان الرقم 5 من ضمن الأرقام قم بطرحه من باقي الأرقام بدلا من جمعه
# Tests



def addition(*numbers):
    sum_1 = 0
    for number in numbers:
        if number == 10:
            continue
        elif number == 5:
            sum_1 -= number

        else:
            sum_1 += number
    return sum_1



print(addition(10, 20, 30, 10, 15))  # 65
print(addition(10, 20, 30, 10, 15, 5, 100))  # 160
