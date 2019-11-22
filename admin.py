from user import User

class Admin(User):
    def __init__(self, first_name, last_name, age, login_attempts, privileges ):
        super().__init__(first_name, last_name, age, login_attempts)
        self.privileges = privileges

class Privileges():
    def show_privileges(self, privileges):
        self.privileges = privileges
        print(self.privileges)

privilegas_attrib =
privileges_list = ['can add posts', 'can delete post', 'can ban users' ]
admin_privileges = Admin('gledis', 'qose', 19, 0, privileges_list)
admin_privileges.show_privileges()



