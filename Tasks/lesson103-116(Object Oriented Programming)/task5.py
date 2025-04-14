# التكليف 05
# لديك ال Class الرئيسي بالخواص الموجودة فيه
# المطلوب في Admins إنشاء Admins Class والذي يرث الخواص من ال Class الرئيسي
# بعدها قم بإنشاء Moderators Class والذي يرث الخواص أيضا من ال Class الرئيسي ولكن بطريقة مختلفة غير السابقة
# قم بطباعة المطلوب كما في المثال
# Main Class
class Members:

    def __init__(self, n, p):
        self.name = n

        self.permission = p

    def show_info(self):
        return f"Your Name Is {self.name} And You Are {self.permission}"


class Admins(Members):
    def __init__(self, n, p):
        super().__init__(n, p)

class Moderators(Members):
    def __init__(self, n, p):
        super().__init__(n, p)


member_one = Admins("Osama", "Admin")
member_two = Moderators("Ahmed", "Moderator")

print(member_one.show_info())
# Output
# Your Name Is Osama And You Are Admin

print(member_two.show_info())
# Output
# Your Name Is Ahmed And You Are Moderator
