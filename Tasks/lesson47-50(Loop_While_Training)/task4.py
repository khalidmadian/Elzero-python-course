# التكليف 04
# قم بإنشاء List فارغة سوف تحتوي لاحقا على أسماء أصدقائك وضعها في متغير بإسم my_friends
# قم بتحديد أقصى عدد للأصدقاء لإضافتهم في القائمة هو 4
# قم بعمل Input يطلب منك إسم الشخص الذي تريد إضافته للقائمة
# إذا كان إسم الشخص كاملا عبارة عن حروف كبيرة Uppercase قم برفض الشخص وإظهار رسالة تفيد أن الإسم غير صالح
# إذا كان الإسم كله حروف صغيرة قم بتحويل أول حرف فقط لحرف كبير ثم قم بإضافته للقائمة
# بعد إضافة الإسم تطبع معه رسالة تفيد أنك قمت بتحويل أول حرف لحرف كبير
# يجب طباعة إسم الشخص مع الرسالة الخاصة بالإضافة
# في حالة قام الشخص بكتابة إسم وأول حرف فيه كبير قم بإضافته مباشرة وإطبع رسالة تفيد الإضافة
# في حالة تم إضافة الإسم ومازال هناك مكان آخر في القائمة قم بإظهار ال Input ليقوم بإضافة إسم
#
# آخر حتى تمتليء القائمة
# مع كل إضافة قم بكتابة رسالة تفيد كم عدد الأسماء المتبقية في القائمة قبل أن تمتليء
# كل إسم يتم إضافته يجب أن يتم إزالة المسافات من قبله وبعده إن وجدت

my_friends = []

counter = 0
while len(my_friends) < 4:

    name = input('Enter your friend name:').strip()
    new_name = name.lower()
    if name.isupper():
        print('inavalid name')
        counter -= 1


    else:
        new_name = name.lower()
        if new_name.islower():
            my_friends.append(new_name.capitalize())
            print(f'We convert the first letter to be capital this is the name ({my_friends[counter]})')
        elif new_name[0].isupper():
            my_friends.append(new_name)
            print('Thank you 😀 right syntax We added this name directly')

    counter += 1
    print(f'{4 - counter} Names left you can add')
    print(f'These are youre friends{my_friends}')
