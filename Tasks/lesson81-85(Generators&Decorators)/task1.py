# التكليف 01
# إستخدم ال Yield مع ما تعلمته لتقوم بعمل Reverse لل String
# تأكد بعدها ان ال Loop يعمل بنجاح ويخرج النتيجة المطلوبة
def reverse_string(my_string):
  for i in reversed(my_string):
    yield i

# Reverse The String
for c in reverse_string("Elzero"):
  print(c)
