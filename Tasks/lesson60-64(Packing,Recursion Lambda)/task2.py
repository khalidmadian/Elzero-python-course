# التكليف 02
# قم بعمل ال Function المناسبة التي تخرج جميع المخرجات الموجودة في الأمثلة التالية
# لدينا بيانات جديدة وهي إسم الشخص
# البيانات يمكن أن تزيد أو تنقص
# إذا لم يتم كتابة الإسم لا تظهر السطر الترحيبي الأول
# إذا لم يكن لديه مهارات قم بإظهار رسالة تفيد أنه لا يوجد لديه Score كما في المثال
# Test 1
def get_people_scores(name='none', **scores):

    if name == 'none':
        print('none name')
    else:
        print(f'"Hello {name} This Is Your Score Table:"')
    for subj, score in scores.items():
        print(f'{subj}=>{score}')
    if len(scores)==0:
        print('no scores')


get_people_scores( Math=90, Science=80, Language=70)
print('---------------------------')

# Output
# "Hello Osama This Is Your Score Table:"
# "Math => 90"
# "Science => 80"
# "Language => 70"

# Test 2
get_people_scores("Mahmoud", Logic=70, Problems=60)
print('---------------------------')


# Output
# "Hello Mahmoud This Is Your Score Table:"
# "Logic => 70"
# "Problems => 60"

# Test 3
get_people_scores(Logic=70, Problems=60)
print('---------------------------')


# Output
# "Logic => 70"
# "Problems => 60"

# Test 4
get_people_scores("Ahmed")
print('---------------------------')


# Output
# "Hello Ahmed You Have No Scores To Show"
