from dao.users_dao import UserDAO

class UserServices:
    def __init__(self):
        self.user_dao = UserDAO()

    def add_user(self, user):
        
        if user.age < 18:
            raise ValueError("You must be 18 or above to register")
        if user.age > 110:
            raise ValueError("Please enter a valid age")
        if not user.email.strip():
            raise ValueError("Email cannot be empty")
        if len(user.contact_number) < 10 or len(user.contact_number) > 10:
            raise ValueError("Contact Number must contain 10 digits")
        if not user.contact_number.isnumeric:
            raise ValueError("Contact Number cannot contain alphabets")
        
        return self.user_dao.add_user(user)

    def log_in(self, email, password):
        user = self.user_dao.log_in(email, password)
        if not user:
            raise ValueError("Invalid credentials")
        return user

    def get_all_users(self):
        # if not role in ["customer", "admin"]:
        #     raise ValueError(f"There is no {role} role. Either choose 'admin' or 'customer'")
        user = self.user_dao.get_all_users()
        if not user:
            raise ValueError("There are no Users")
        return user