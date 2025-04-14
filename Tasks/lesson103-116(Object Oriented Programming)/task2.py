class User:
    def __init__(self, f_name, s_name, age, gender):
        self.f_name = f_name
        self.s_name = s_name
        self.age = age
        self.gender = gender

    def full_details(self):
        if self.gender == 'Male':
            return f'Hello Mr {self.f_name} {self.s_name[0]}. [{40 - self.age}] Years To Reach 40'
        elif self.gender == 'Female':
            return f'Hello Mrs {self.f_name} {self.s_name[0]}. [{40 - self.age}] Years To Reach 40'


user_one = User("Osama", "Mohamed", 38, "Male")
user_two = User("Eman", "Omar", 25, "Female")

print(user_one.full_details())  # Hello Mr Osama M. [02] Years To Reach 40
print(user_two.full_details())  # Hello Mrs Eman O. [15] Years To Reach 40
