# التكليف 02
# لديك ال Code التالي يستقبل منك مدخلات
# المطلوب إستعمال Try, Except, Else لتظهر النتائج كما هو في الأمثلة


LETTER = input("Add Letter From A to Z:")


try:
    if len(LETTER)>1:
        raise Exception("You Must Write One Character Only")

    elif  LETTER.isalpha():
        print(f"You Typed {LETTER}")

    else:
        print("The Letter Not In A - Z")


except Exception as e:
    print(e)
