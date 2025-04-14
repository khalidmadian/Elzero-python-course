# التكليف 01
# قم بكتابة ال Code المناسب داخل ال Loop لتظهر النتيجة كما في المثال “Elzero”
# لا تقم بتعديل أي شيء موجود مسبقا في ال Code
my_list = ["E", "Z", "R", 1, 2, 3]
my_tuple = ("L", "E", "O")
my_data = []

for data in zip(my_list, my_tuple):
    my_data.append(data)  # نأخذ العنصر الأول من كل زوج

final_string = ''
print(my_data)
for item in my_data:
    for i in item:
        final_string += str(i)
print(final_string)  # Elzero



print('=================Another way===========================')

my_list = ["E", "Z", "R", 1, 2, 3]
my_tuple = ("L", "E", "O")
my_data = []

# دمج العناصر من my_list و my_tuple
for data in zip(my_list, my_tuple):
    my_data.append(data[0])  # نأخذ العنصر الأول من كل زوج (من my_list)
    my_data.append(data[1])  # نأخذ العنصر الثاني من كل زوج (من my_tuple)

# تحويل القائمة إلى سلسلة نصية
final_string = ''.join([str(item) for item in my_data])

print(final_string)  # النتيجة: Elzero
