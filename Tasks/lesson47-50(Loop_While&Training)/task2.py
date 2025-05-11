# التكليف 02
# أنشئ قائمة فيها خمس من أصدقائك ثم تأكد أن فيهم إسمين في الأقل مكتوبين بحروف صغيرة والباقي أول حرف من الإسم Capital
# قم بإستخدام While Loop لطباعة الأسماء كلها مع تجاهل الأسماء التي تبدأ بحروف صغيرة
# اطبع عدد الأسماء التي تم تجاهلها ويجب أن تكون بطريقة برمجية وليست يدوية
# Input

friends = ["Mohamed", "Shady",'Khalid', "ahmed", "eman",'saad' ,"Sherif"]

# Needed To be Output
# "Mohamed"
# "Shady"
# "Sherif"
# "Friends Printed And Ignored Names Count Is 2"
count = 0
not_ignored=0
length=len(friends)
while count < length:
    if friends[count][0].isupper() :
        print(friends[count])
        not_ignored+=1
    count += 1

print(f'ignored word is {len(friends) - not_ignored}')
