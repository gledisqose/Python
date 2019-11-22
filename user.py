class User():
    def __init__(self, first_name, last_name, age, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = login_attempts

    def describe_user(self):
        print("Frist name: " + self.first_name.title())
        print("Last name: " + self.last_name.title())
        print("Age: "+ str(self.age))

    def greet_user(self):
        print("Hello " + self.first_name.title() + ' ' + self.last_name.title()+ '\n')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0



first_user = User('john', 'tomson', 20, 0)
#second_user = User('siri', 'jackson', 34)
#third_user = User('gledis', 'qose', 19)

first_user.describe_user()
first_user.greet_user()

#second_user.describe_user()
#second_user.greet_user()

#third_user.describe_user()
#third_user.greet_user()

first_user.increment_login_attempts()
first_user.increment_login_attempts()
first_user.increment_login_attempts()

print(str(first_user.login_attempts))

first_user.reset_login_attempts()
print(str(first_user.login_attempts))