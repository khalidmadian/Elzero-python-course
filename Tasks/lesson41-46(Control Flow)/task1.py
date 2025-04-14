# التكليف 01
# قم بعمل متغيرين بإسم num1, num2 ويكونوا Input يحتوي على الرقم الأول والثاني
# قم بعمل متغير ثالث بإسم operation يكون عبارة عن Input يحتوي على نوع العملية الحسابية
# قم بالتأكد من أن متغيرات الأرقام عبارة عن Integer ولا يوجد مسافات قبلهم ولا بعدهم
# قم بالتأكد أن المتغير الخاص بالعملية الحسابية لا توجد مسافات قبله ولا بعده
# قم بجلب الرقم الأول والثاني والعملية الحسابية من المدخلات ثم قم بالعملية بناء على الأرقام والعملية الحسابية سواء كانت + – * / %
# # Inputs
#
# num1 = 20
# num2 = 40
# operation = "+" Or "-" Or "*" Or "/" Or "%"

# Needed Output

# [num1 20] [operation +] [num2]
# Example One 20 + 40 = 60
# Example Two 20 * 40 = 800

num1 = int(input('Enter num1:'))
num2 = int(input('Enter num2:'))
operation = input('choose "+" Or "-" Or "*" Or "/" Or "%" :')
sum = num1 + num2
min = num1 - num2
mul = num1 * num2
div = num1 / num2
rest_div = num1 % num2
if operation == '+':
    print(f'{num1} {operation} {num2} = {sum}')
if operation == '-':
    print(f'{num1} {operation} {num2} = {min}')
if operation == '*':
    print(f'{num1} {operation} {num2} = {mul}')
if operation == '/':
    print(f'{num1} {operation} {num2} = {div}')
if operation == '%':
    print(f'{num1} {operation} {num2} = {rest_div}')
