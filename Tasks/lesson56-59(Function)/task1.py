# التكليف 01
# قم بعمل Function تقوم بعمل عمليات حسابية بإسم calculate
# العمليات الحسابية هي الجمع والطرح والقسمة
# ال Function تقبل ثلاثة Parameters الرقم الأول والرقم الثاني ونوع العملية الحسابية وقم بتسميتهم كما تريد
# كل ما عليك هو تنفيذ العملية الحسابية بناء على المدخلات
# في حالة قام الشخص بكتابة نوع العملية الحسابية خطأ تظهر له رسالة أنه لا توجد هذه العملية
# العمليات الحسابية المتاحة هي add, subtract, multiply
# يمكن للشخص أن يكتب العملية الحسابية بحروف كبيرة أو صغيرة او Mix بدون مشكلة. مثلا add, ADD, aDd
# يمكن للشخص كتابة أول حرف فقط من العملية الحسابية فمثلا subtract يمكن أن يكتب S أو s
# إذا لم يكتب الشخص العملية الحسابية نهائيا قم بعمل العملية الإفتراضية وهي الجمع
# # Tests


def calculate(num1, num2, operation='add'):
    # Normalize the operation input to lowercase
    operation = str(operation).strip().lower()

        # Perform calculations based on the operation
    if operation == 'add' or operation == 'a':  # Check for exact match or single leading character
        return num1 + num2  # Addition
    elif operation == 'subtract' or operation == 's':  # Check for exact match or single leading character
        return num1 - num2  # Subtraction
    elif operation == 'multiply' or operation == 'm':  # Check for exact match or single leading character
        return num1 * num2  # Multiplication
    else:
        return "لا توجد هذه العملية"  # Error message for invalid operation


# Testing the function
print(calculate(10, 20))  # Output: 30 (default addition)
print(calculate(10, 20, "AdD"))  # Output: 30 (addition)
print(calculate(10, 20, "a"))  # Output: 30 (addition)
print(calculate(10, 20, "A"))  # Output: 30 (addition)

print(calculate(10, 20, "S"))  # Output: -10 (subtraction)
print(calculate(10, 20, "subTRACT"))  # Output: -10 (subtraction)

print(calculate(10, 20, "Multiply"))  # Output: 200 (multiplication)
print(calculate(10, 20, "m"))  # Output: 200 (multiplication)

print(calculate(10, 20, "aaaadd"))  # Output: "لا توجد هذه العملية" (invalid)
