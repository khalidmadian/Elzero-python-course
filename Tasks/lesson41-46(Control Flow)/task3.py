# التكليف 03
# قم بعمل Input يقبل منك العمر الخاص بالشخص
# تأكد أن المدخل عبارة عن Integer
# المطلوب طباعة عمرك بالشهور والأسابيع والأيام والساعات والدقائق والثواني
# المطلوب طباعة كل وحدة من وحدات الوقت في سطر منفصل
# يجب التأكد من أن العمر أكبر من 10 وأقل من 100 وفي حالة غير ذلك إطبع رسالة تفيد أن العمر خارج النطاق.
# # Input Example 38

# Needed Output
# "Your Age In Months Is 456 Months" # Months Example
# "Your Age In Weeks Is 1824 Weeks" # Weeks Example

age = int(input('Enter your age: '))

months = age * 12
weeks = months * 4
days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

if age < 100 and age > 10:
    print(f"Your Age In Months Is {months:,} Months")
    print(f"Your Age In weeks Is {weeks:,} weeks")
    print(f"Your Age In days Is {days:,} days")
    print(f"Your Age In minutes Is {minutes:,} minutes")
    print(f"Your Age In seconds Is {seconds:,} seconds")
else:
    print('out of limited')
