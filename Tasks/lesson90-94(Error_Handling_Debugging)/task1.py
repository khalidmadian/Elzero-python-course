# # التكليف 01
# # لديك ال Code التالي يستقبل منك مدخلات
# # بناء على المدخلات سنظهر بعض رسائل الخطأ


NUM = input("Add Your Number ")

try:
    if NUM.isalpha():
        raise Exception('Only Numbers Allowed')

    elif len(NUM) != 1:
        raise IndexError('Only One Character Is Allowed')

    elif NUM.isdigit():
        if int(NUM) == 0:
            raise ValueError('Number Must Be Larger Than 0')
        else:
            print(f'hi your number is "{NUM}"')



except IndexError as e:
    print(f'Index Error {e}')

except ValueError as e:
    print(f'ValueError: {e}')

except Exception as e:
    print(f'Exception: {e}')
