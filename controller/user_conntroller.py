from service.user_services import UserServices
from model.users import Users
from logs.logger import log_event

class UserController:
    def __init__(self):
        self.user_service = UserServices()

    def register(self):
        try:
            print("\n--- Register ---")
            name = input("Enter name: ")
            email = input("Enter email: ")
            age = int(input("Enter age: "))
            password = input("Enter password: ")
            contact_number = input("Enter contact number: +91-")
            role = "customer"

            user = Users(name=name, email=email, age=age, password=password, contact_number=contact_number, role=role)
            s_id = self.user_service.add_user(user)
            print("User added successfully, ID:", s_id)
            log_event('register',s_id)


        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            log_event(f"Controller ERROR in register: {e}")

    def login(self):
        try:
            print("\n--- Login ---")
            email = input("Enter email: ")
            password = input("Enter password: ")
            user = self.user_service.log_in(email, password)
            print("Login successful!")
            return user

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            log_event(f"Controller ERROR in login: {e}")

    def view_all_users(self):
        try:
            print("\n--- All Users (Admin) ---")
            users = self.user_service.get_all_users()
            for u in users:
                print(f"User ID: {u['user_id']} | User Name: {u['user_name']} | User Age: {u['age']} | User Contact No: {u['contact_number']} | User Email : {u['email']}")
                # for cart in u['cart_items']:
                #     print(f"   -> {item['product_name']} | Qty: {item['quantity']} | Price: {item['unit_price']}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            log_event(f"Controller ERROR in view_all_users: {e}")

