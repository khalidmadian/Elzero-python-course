# التكليف 03
# قم بعمل متغيرين بإسم first_name و second_name يحتووا على Input فيه الإسم الأول والثاني للشخص
# قم بالتأكد من أن أي مسافات قبل وبعد الإسم الأول والثاني سوف يتم إزالتها
# قم بالتأكد من أن الإسم الأول والثاني أول حرف فيهم Capital والباقي Small
# قم بطباعة رسالة ترحيبية فيها الإسم الأول وأول حرف من الإسم الثاني فقط.
# # Inputs
#
# "Osama" # First Name
# "Mohamed" # Second Name

# Needed Output

"Hello {First_Name} {First_Letter_From_Second_Name}." # Example "Osama M."

first_name=input('Enter First Name:').capitalize().strip()
second_name=input('Enter Second Name:').capitalize().strip()

print(f'Hello {first_name} {second_name[:1]}.')