# التكليف 03
# لديك قاموس يحتوي على المواد العلمية الخاصة بك وال Rank الذي حصلت عليه
# كل قيمة من القيم في ال Rank تساوي نقاط معينة
# ال A تساوي 100 وال B تساوي 80 وال C تساوي 40
# قم بإستخدام ما تعلمته سابقا لتخرج بالنتيجة التالية بدون التعديل على القاموس الأصلي
# قم بطباعة مجموع النقاط في النهاية بعد إنتهاء ال Loop
# Input
my_ranks = {
    'Math': 'A',
    "Science": 'B',
    'Drawing': 'A',
    'Sports': 'C'
}

# Needed Output
# "My Rank in Math Is A And This Equal 100 Points"
# "My Rank in Science Is B And This Equal 80 Points"
# "My Rank in Drawing Is A And This Equal 100 Points"
# "My Rank in Sports Is C And This Equal 40 Points"
# "Total Points Is 320
total = 0
for i, x in my_ranks.items():
    if x == 'A':
        points = 100
        print(f'"My Rank in {i} Is {x} And This Equal 100 {points}"')
    elif x == 'B':
        points = 80
        print(f'"My Rank in {i} Is {x} And This Equal 80 Points"')
    elif x == 'C':
        points = 40
        print(f'"My Rank in {i} Is {x} And This Equal 40 Points"')
    total += points

print(total)
