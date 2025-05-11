# التكليف 02
# قم بكتابة ال Code المناسب داخل ال Loop لتظهر النتيجة كما في المثال “Elzero”
# لا تقم بتعديل أي شيء موجود مسبقا في ال Code
my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
my_data = []

for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):
    # نأخذ العنصر الأول من my_list1 والعنصر الثاني من my_tuple والعنصر الثالث من my_list2
    if item1 or item2 or item3 in my_data:
        continue
    else:
        my_data.append(item1)
        my_data.append(item2)
        my_data.append(item3)

# تحويل القائمة إلى سلسلة نصية
final_string = ''.join([str(item) for item in my_data if str(item).isalpha()])

print(final_string)  # النتيجة: Elzero
