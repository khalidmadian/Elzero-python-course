# قم بإنشاء Tuple تحتوي على أسماء 3 من أصدقاءك وأول إسم يكون Osama
# إستخدم خبرتك وما تعلمته سابقا لتغيير أول إسم من Osama إلى Elzero
# قم بطباعة محتوى ال Tuple في السطر الأول
# قم بطباعة النوع للتأكد من أنه Tuple وليس نوع بيانات آخر
# في السطر الثالث قم بطباعة عدد العناصر داخل ال Tuple


friends = ("Osama", "Ahmed", "Sayed")

# Needed Output

# ("Elzero", "Ahmed", "Sayed")
# <class 'tuple'>
# 3 Elements

# sum two tuples to each other ('Elzero',)+("Ahmed", "Sayed")

friends = ("Elzero",) + friends[1:]

print(friends)
print(type(friends))
print(f'{len(friends)} Elements')
