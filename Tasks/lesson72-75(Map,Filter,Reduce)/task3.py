# التكليف 03
# قم بإستخدام ما تعلمته لتحسب حاصل ضرب جميع الأرقام الموجودة في القائمة nums
# يجب عليك أن تعرف ان القائمة يمكن أن تتغير عناصرها لذلك الحل لابد أن يعمل على اي قائمة
# قم بعمل نفس الحل بواسطة Lambda Function
from past.builtins import reduce

nums = [2, 4, 6, 2]


# Output
# 96

def mult_num(num1, num2):
    return num1 * num2


my_red = reduce(mult_num, nums)
print(my_red)

print('--------------------------another method------------------------------')

result = reduce(lambda a, b: a * b, nums)
print(result)
