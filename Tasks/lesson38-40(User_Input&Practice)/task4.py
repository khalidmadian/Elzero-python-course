# التكليف 04
# قم بعمل متغير باسم email يحتوي على ال Input الخاص بالبريد الإلكتروني للشخص
# قم بالتأكد من إزالة المسافات قبل وبعد البريد الإلكتروني
# قم بالتأكد من أن جميع الحروف سوف تكون صغيرة Lower Letters
# قم بطباعة رسالة في السطر الأول تحتوي على إسم الشخص فقط الموجود قبل علامة @ مع تحويل أول حرف لحرف كبير Capital
# قم بطباعة رسالة في السطر الثاني تحتوي على الموقع الموجود عليه البريد الإلكتروني فقط بدون ال Domain
# في السطر الثالث قم بطباعة ال Top Level Domain الموجود بعد ال "Dot"
# # Inputs
#
# "Osama@Nn.Sa" # Email

# Needed Output

# "Your Name Is Osama"
# "Email Service Provider Is nn"
# "Top Level Domain Is sa"
#

from scanext import error

user_fname = input('Enter Your Name😀: ').strip()
user_email = input('Enter Your Email🧐: ').strip()

if '@' in user_email:
    print(f'your name is :{user_fname}')
    print(f'your username is {user_email[:user_email.index("@")]}')
    print(f'your domain is {user_email[user_email.index("@") + 1:]}')

else:
    raise error
