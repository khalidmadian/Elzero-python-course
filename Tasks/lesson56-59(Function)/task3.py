# التكليف 03
# قم بعمل Function تقوم بطباعة بيانات عن الشخص ومهاراته
# ال Function تقبل منك إسم الشخص وبعده عدد غير معلوم من المهارات
# كل ما عليك هو طباعة رسالة ترحيبية بالشخص ثم طباعة مهاراته تحت الإسم
# إذا لم يكن لديه مهارات يجب عليك إظهار رسالة تفيد أنه ليس لديه مهارات حتى الآن
# Input
def show_skills(name, *skills):
    if len(skills) == 0:
        print(f'Hello {name} You Have No Skills To Show')
    else:
        print(f'Hello {name} Your Skills Is')
        for skill in skills:
            print(skill)


# Output
# "Hello Osama Your Skills Is"
# "- HTML"
# "- CSS"
# "- JS"
# "- Python"
# Input
show_skills("Ahmed")
show_skills("Osama", "HTML", "CSS", "JS", "Python")
# Output
# "Hello Ahmed You Have No Skills To Show"
