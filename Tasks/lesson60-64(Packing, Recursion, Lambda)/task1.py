# التكليف 01
# قم بعمل ال Function المناسبة التي تخرج جميع المخرجات الموجودة في الأمثلة التالية
# البيانات يمكن أن تزيد أو تنقص
# Tests
def get_score(**scores):
    for name,score in scores.items():
        print(f'"{name} => {score}"')





get_score(Math=90, Science=80, Language=70)

# Output
# "Math => 90"
# "Science => 80"
# "Language => 70"
# Tests
# get_score(Logic=70, Problems=60)
#
# # Output
# # "Logic => 70"
# # "Problems => 60"
