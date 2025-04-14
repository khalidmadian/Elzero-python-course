# التكليف 02
# قم بعمل Function بإسم get_names تقوم بإرجاع الأسماء التي تنتهي بحرف ال m
# قم بإستخدام ال filter لتجعل هذه ال Function تمر على جميع عناصر ال List الموجودة في التكليف
# قم بعمل متغير بإسم names وقم بتخزين نتيجة إستخدام ال filter فيه
# قم بعمل Loop على المتغير names لتطبع جميع الأسماء الموجودة في القائمة
# قم بإستخدام نفس المثال ولكن بإستخدام Lambda Function داخل ال Loop مباشرة
# Output
# "Wessam"
# "Essam"

friends_filter_iterable = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

print('-------------------- first method ------------------------')


def my_filter_func(name):
    return name[len(name) - 1] == 'm'


my_map = filter(my_filter_func, friends_filter_iterable)
for item in my_map:
    print(item)

print('-------------------- second method ------------------------')

small_filter = filter(lambda name1: name1[len(name1) - 1] == 'm', friends_filter_iterable)

for item1 in small_filter:
    print(item1)
