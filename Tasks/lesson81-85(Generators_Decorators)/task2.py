# التكليف 02
# قم بعمل Decorator Function تقوم بإضافة رسالة قبل ال Function و Separator مكون من علامة Hash بعد ال Function
# قم بإستخدام ال Decorator مع ال Functions الحالية
# شاهد المثال لتفهم المطلوب
# # Create Your Decorator Here
def my_decorator(func):
    def nested():
        print('Sugar Added From Decorators')
        func()
        print("####################")

    return nested


@my_decorator
def make_tea():
    print("Tea Created")

@my_decorator
def make_coffe():
    print("Coffe Created")


make_tea()
make_coffe()

# Needed Output

# "Sugar Added From Decorators"
# "Tea Created"
# "####################"
# "Sugar Added From Decorators"
# "Coffe Created"
# "####################"
