# التكليف 04
# قم بعمل Loop على ال Tuple التالية مع طباعة ال Index الخاص بكل عنصر
# يجب أن يبدأ ال Index من رقم 50
# إذا وجدت أرقام في ال Tuple قم بتجاهلها
# تأكد أن البيانات يتم طباعتها بطريقة معكوسة لكن ال Index بطريقة منظمة
# قم بعمل الحل بطريقتين مختلفتين
print('--------------------first method------------------------------ ')
skills = reversed(("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript"))

format_skils = enumerate(skills, 50)

for i, s in format_skils:
    if type(s) == int:
        continue
    else:
        print(f'"{i} - {s}"')

print('--------------------second method------------------------------ ')
skill1 = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")
counter = 50

for item in reversed(skill1):
    if isinstance(item, str):
        print(f'"{counter} - {item}"')
        counter += 1
    else:
        continue

# Output
# "50 - JavaScript"
# "52 - Python"
# "53 - PHP"
# "55 - CSS"
# "56 - HTML"
