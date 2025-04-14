# التكليف 04
# لديك قاموس يحتوي على أسماء الطلبة وكل طالب لديه مجموعة من المواد العلمية ودرجاته فيها
# كل قيمة من القيم في ال Rank تساوي نقاط معينة
# ال A تساوي 100 وال B تساوي 80 وال C تساوي 40 وال D تساوي 20
# قم بإستخدام ما تعلمته سابقا لتخرج بالنتيجة التالية بدون التعديل على القاموس الأصلي
# يجب عليك طباعة المخرجات كما هي بالعلامات بكل شيء
# قم بعمل الحل مرة بطريقة عادية ومرة أخرى بإستخدام ال
# items()
# Input
students = {
    "Ahmed": {
        "Math": "A",
        "Science": "D",
        "Draw": "B",
        "Sports": "C",
        "Thinking": "A"
    },
    "Sayed": {
        "Math": "B",
        "Science": "B",
        "Draw": "B",
        "Sports": "D",
        "Thinking": "A"
    },
    "Mahmoud": {
        "Math": "D",
        "Science": "A",
        "Draw": "A",
        "Sports": "B",
        "Thinking": "B"
    }
}

# Needed Output
# "------------------------------"
# "-- Student Name => Ahmed"
# "------------------------------"
# "- Math => 100 Points"
# "- Science => 20 Points"
# "- Draw => 80 Points"
# "- Sports => 40 Points"
# "- Thinking => 100 Points"
# "Total Points For Ahmed Is 340"
# "------------------------------"
# "-- Student Name => Sayed"
# "------------------------------"
# "- Math => 80 Points"
# "- Science => 80 Points"
# "- Draw => 80 Points"
# "- Sports => 20 Points"
# "- Thinking => 100 Points"
# "Total Points For Sayed Is 360"
# "------------------------------"
# "-- Student Name => Mahmoud"
# "------------------------------"
# "- Math => 20 Points"
# "- Science => 100 Points"
# "- Draw => 100 Points"
# "- Sports => 80 Points"
# "- Thinking => 80 Points"
# "Total Points For Mahmoud Is 380"
total = 0
for name in students:
    print('"-----------------------------"')
    print(f'"-- Student Name => {name}"')
    print('"-----------------------------"')
    for subject in students[name]:
        if students[name][subject] == 'A':  # Rank
            points = 100
            print(f'"- {subject} => {points}"')
            total += points
        elif students[name][subject] == 'B':
            points = 80
            print(f'"- {subject} => {points}"')
            total += points
        elif students[name][subject] == 'C':
            points = 40
            print(f'"- {subject} => {points}"')
            total += points
        elif students[name][subject] == 'D':
            points = 20
            print(f'"- {subject} => {points}"')
            total += points

    print(f' "Total Points For {name} Is {total}"')
    total = 0
