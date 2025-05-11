import os

# التكليف 01
# قم بإنشاء مجلد بإسم Python على سطح المكتب ثم إنشيء بداخله ملف بإسم assign.py ثم قم بفتحه
# قم بإنشاء 50 Text بإسم txt1 و txt2 و txt3 حتى txt50 داخل المجلد Python بطريقة برمجية
# قم بكتابة جملة Elzero Web School => {File Number} ومكان File Number أكتب رقم الملف
# تأكد أن الملف رقم 25 بإسم تقوم بتسميته special-text ويكون فارغ بدون أي كتابة داخله
# في السطر الأول قم بطباعة ال Current Working Directory
# في السطر الثاني قم بطباعة المسار الموجود فيه الملف حاليا
# في السطر الثالث قم بطباعة إسم الملف المفتوح حاليا
# في السطر الرابع قم بطباعة مجموع الملفات الموجودة داخل المجلد Python
# -------------------------------------------------------my code ---------------------------------------------------------
# i = 0
# while i < 50:
#     i += 1
#     if i == 25:
#         file = open(f'/home/khalid/Abolftoh/courses/Elzero python/Tasks/lesson65-68(Files Handling)/task1+task2/python/khalidsaaad','w')
#         file.write(f'Elzero Web School => {i}')
#         file.close()
#     else:
#         file = open(f'/home/khalid/Abolftoh/courses/Elzero python/Tasks/lesson65-68(Files Handling)/task1+task2/python/khalid{i}','w')
#         file.write(f'Elzero Web School => {i}')
#         file.close()
#

# ------------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------# التكليف 02----------------------------------------------------------------

# قم بالتكملة على ما سبق في التكليف الأول
# قم بفتح الملف txt1.txt
# إترك السطر الأول كما هو والمكتوب فيه Elzero Web School => 1
# من بداية السطر الثاني قم بكتابة
# Appended => Elzero Web School
# خمسون مرة كل واحدة على سطر مختلف
# -------------------------------------------------------my code ---------------------------------------------------------
# file = open('/home/khalid/Abolftoh/courses/Elzero python/Tasks/lesson65-68(Files Handling)/task1+task2/python/khalid1','a')
#
# file.write('\nAppended => Elzero Web School'*50)


# ------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------# التكليف 03---------------------------------------------------------------

# التكليف 03
# قم بالتكملة على ما سبق في التكليف الأول
# قم بفتح الملف txt1.txt
# في السطر الأول قم بطباعة عدد الأسطر الموجودة داخل الملف
# في السطر الثاني قم بحساب عدد الكلمات الموجودة في الملف
# في الصف الثالث قم بطباعة عدد ال Characters الموجودة في الملف
# في السطر الرابع قم بطباعة كم عدد المرات التي وجد فيها الحرف “l”
# # Output
# "Number Of Lines Is => 51"
# "Number Of Words Is => 255"
# "Number Of Chars Is => 1268"
# "Number Of "l" Char Is => 102"
# -------------------------------------------------------my code ---------------------------------------------------------
# my_file_task3=open('/home/khalid/Abolftoh/courses/Elzero python/Tasks/lesson65-68(Files Handling)/task1+task2/python/khalid1','r')
#
#
# count_line_number=len(my_file_task3.readlines())
#
# my_file_task3.seek(0)
#
# count_word=(my_file_task3.read())
# count_word_number=len(count_word.split())
#
# my_file_task3.seek(0)
# count_chars=len(my_file_task3.read())
#
#
#
# print(f'"Number Of Lines Is => {count_line_number}"')
# print(f'"Number Of Words Is => {count_word_number}"')
# print(f'"Number Of Chars Is => {count_chars}"')
#
# my_file_task3.seek(0)
# count=0
# Characters=(my_file_task3.read())
# for char in Characters:
#     if 'l' == char:
#         count+=1
# print(f'"Number Of "l" Char Is => {count}"')

# ------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------# التكليف 04---------------------------------------------------------------

# التكليف 04
# قم بالتكملة على ما سبق في التكليف الأول
# بطريقة برمجية وبواسطة ال Loop قم بحذف آخر عشر ملفات txt
# بعد إتمام العملية السابقة بنجاح سيكون آخر ملف عندك إسمه txt40.txt

# -------------------------------------------------------my code ---------------------------------------------------------
# i = 50
# while i > 40:
#     i -= 1
#     file_path = os.path.join(
#         f'/home/khalid/Abolftoh/courses/Elzero python/Tasks/lesson65-68(Files Handling)/task1+task2/python/khalid{i}',
#         'file')
#     os.remove(
#         f'/home/khalid/Abolftoh/courses/Elzero python/Tasks/lesson65-68(Files Handling)/task1+task2/python/khalid{i}')
#
