from service.user_services import UserServices
from model.users import Users

class UserController:
    def __init__(self):
        self.user_service = UserServices()

    def register(self):
        print("\n--- Register ---")
        name = input("Enter name: ")
        email = input("Enter email: ")
        age = int(input("Enter age: "))
        password = input("Enter password: ")
        contact_number = input("Enter contact number: ")
        role = "customer"

        user = Users(name=name, email=email, age=age, password=password, contact_number=contact_number, role=role)
        s_id = self.user_service.add_user(user)
        print("User added successfully, ID:", s_id)

    def login(self):
        print("\n--- Login ---")
        email = input("Enter email: ")
        password = input("Enter password: ")
        user = self.user_service.log_in(email, password)
        print("Login successful!")
        return user
