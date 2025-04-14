# التكليف 01
# قم بعمل Function بإسم remove_chars تزيل أول وآخر حرف من اي String
# قم بإستخدام ال map لتجعل هذه ال Function تمر على جميع عناصر ال List الموجودة في التكليف
# قم بعمل متغير بإسم cleaned_list وقم بتخزين نتيجة إستخدام ال map فيه
# قم بعمل Loop على المتغير cleaned_list لتطبع جميع الأسماء الموجودة في القائمة
# قم بإستخدام نفس المثال ولكن بإستخدام Lambda Function داخل ال Loop مباشرة
friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

# Output
# "Eman"
# "Ahmed"
# "Sameh"
# "Osama"
print('-------------------- first method ------------------------')


def remove_chars(name):
    return name[1:len(name) - 1]


my_map = map(remove_chars, friends_map)
for item in my_map:
    print(item)

print('-------------------- second method ------------------------')

my_map2 = map(lambda name1: name1[1:len(name1) - 1], friends_map)
for item1 in my_map2:
    print(item1)
