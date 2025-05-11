# التكليف 02
# قم بإنشاء Folder بإسم Python في أي مكان تريده
# قم بإنشاء ملف بإسم main.py
# قم بإنشاء ملف آخر بإسم my_mod.py
# داخل ملف my_mod.py قم بإنشاء Two Functions
# ال Functions تكون أسمائها كالتالي say_hello و say_welcome
# say_hello تقوم بإرجاع إسمك وقبله كلمة Hello و say_welcome تقوم بإرجاع إسمك وقبله كلمة Welcome
# في ملف main.py قم بإستدعاء ال my_mod.py
# في ملف main.py قم بإستخدام جميع ال Functions الموجودة في ملف my_mod.py
# "Hello Osama"
# "Welcome Osama"

import my_mod
from my_mod import say_welcome as sw

print(my_mod.say_hello('khalid'))
print(my_mod.say_welcome('khalid'))

print(sw('saad'))