# التكليف 03
# قم بعمل ال Dictionary الذي يحتوي على البيانات التالية
# قم بعمل ال Function المناسبة التي تخرج جميع المخرجات الموجودة في الأمثلة التالية
# إذا لم يتم كتابة الإسم لا تظهر السطر الترحيبي الأول
# إذا لم يكن لديه مهارات قم بإظهار رسالة تفيد أنه لا يوجد لديه Score كما في المثال
# Test 1
scores_list = {
    'Math': '90',
    'Science': '80',
    'Language': '70'
}


def get_the_scores(name='none', **scores):
    if name and name!='none':
        print(f'your name is {name}')
        if scores:
            for subj, score in scores.items():
                print(f'{subj}=>{score}')
        else:
            print('no scores')
    else:
        print('no name')
        for subj, score in scores.items():
            print(f'{subj}=>{score}')


# get_the_scores("Osama", **scores_list)
print('-----------------------------')

# Output
# "Hello Osama This Is Your Score Table:"
# "Math => 90"
# "Science => 80"
# "Language => 70"

# Test 2
# get_the_scores("Osama")
print('-----------------------------')

# Output
# "Hello Osama You Have No Scores To Show"

# Test 3
get_the_scores(**scores_list)
print('---------------------------')
# Output
# "Math => 90"
# "Science => 80"
# "Language => 70"
