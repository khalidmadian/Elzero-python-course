# التكليف 01
# قم بكتابة ال Code التالي لتختبر نفسك ولا تقم بعمل Run له
# بعد آخر سطر في ال Code قم بكتابة تعليق يحتوي على ال Output الذي سيخرج من وجهة نظرك
# بعدها قم بعمل Run لترى النتيجة الخاصة بك سليمة أم لا
# قم بوضع تعليق قبل كل سطر من الأسطر الموجودة في ال Code لتشرح كيف ظهرت هذه النتيجة
values = (0, 1, 2)

if any(values):
    # will be True there at least one item is true
    my_var = 0

my_list = [True, 1, 1, ["A", "B"], 10.5, my_var]

# all item here is true expected the last item my_var = 0 beacuse values = true
# but this is will print good bescause the gate is or not and the other statement is true at least

if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):

    print("Good")

else:

    print("Bad")

    # the output will be good
