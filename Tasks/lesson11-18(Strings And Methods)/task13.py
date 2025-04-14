# التكليف 13
# قم بعمل ثلاث متغيرات فيها اسمك وسنك وبلدك وتأكد أن العمر عبارة عن Integer وليس String وقم بطباعة الرسالة التالية بإستخدام طريقة ال Format ألجديدة f"", شاهد المثال
from orca.debug import printResult

name = "Osama"
age = "38"
country = "Egypt"


if type(age)==int:
    print(f'My Name Is {name}, And My Age Is {age}, And My Country Is {country}')

else:
    print('error')

# Needed Output Using f""
# My Name Is Osama, And My Age Is 38, And My Country Is Egypt