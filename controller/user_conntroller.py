from service.user_services import UserService
from model.user import user

class UserController:
    def __init__(self):
        self.user_service = UserService()

    def add_user(self):
        name = input("Enter name")
        email = input("Enter email")
        age = int(input("Enter age"))
        course = input("Enter course")

        user = user(name, email, age, course)

        s_id = self.user_service.add_user(user)
        print("user added successfully", s_id)