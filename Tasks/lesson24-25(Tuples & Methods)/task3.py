# قم بإنشاء Tuple تحتوي على الأرقام من 1 إلى 3
# قم بإنشاء Tuple تحتوي على الحروف من A إلى C
# قم بعمل Concatenate لهم في Tuple جديدة وقم بطباعة محتواها في السطر الأول
# في السطر الثاني قم بحساب عدد العناصر الموجودة داخل ال Tuple الجديدة

nums = (1, 2, 3)
letters = ("A", "B", "C")

# Needed Output

# nums_and_letters_one = (1, 2, 3, "A", "B", "C")
# 6 Elements



nums_and_letters_one=nums+letters

print(nums_and_letters_one)
print(f"{len(nums_and_letters_one)} Elements")
