# التكليف 04
# قم بعمل Function تقوم بطباعة رسالة ترحيب للشخص
# ال Function تطلب منك ثلاثة Parameters وهم إسم الشخص وسنه وبلده
# إذا لم يكتب الشخص أي بيانات تظهر رسالة إفتراضية
# Input
def say_hello(f_name='Unknown', age='Unknown', country='Unknown'):
    return f'Hello {f_name} Your Age {age} And You Live In {country}'


print(say_hello("Osama", 38, "Egypt"))

# Output
"Hello Osama Your Age Is 38 And You Live In Egypt"
# Input
print(say_hello())

# Output
"Hello Unknown Your Age Is Unknown And You Live In Unknown"
