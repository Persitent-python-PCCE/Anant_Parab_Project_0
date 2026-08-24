from logs.logger import log_event
from dao.users_dao import UserDAO

class UserServices:
    def __init__(self):
        self.user_dao = UserDAO()

    def add_user(self, user):
        
        if user.age < 18:
            log_event("Validation failed: " + str("You must be 18 or above to register"))
            raise ValueError("You must be 18 or above to register")
        if user.age > 110:
            log_event("Validation failed: " + str("Please enter a valid age"))
            raise ValueError("Please enter a valid age")
        if not user.email.strip():
            log_event("Validation failed: " + str("Email cannot be empty"))
            raise ValueError("Email cannot be empty")
        if len(user.contact_number) < 10 or len(user.contact_number) > 10:
            log_event("Validation failed: " + str("Contact Number must contain 10 digits"))
            raise ValueError("Contact Number must contain 10 digits")
        if not user.contact_number.isnumeric:
            log_event("Validation failed: " + str("Contact Number cannot contain alphabets"))
            raise ValueError("Contact Number cannot contain alphabets")
        
        log_event("Service operation successful")
        return self.user_dao.add_user(user)

    def log_in(self, email, password):
        user = self.user_dao.log_in(email, password)
        if not user:
            log_event("Validation failed: " + str("Invalid credentials"))
            raise ValueError("Invalid credentials")
        log_event("Service operation successful")
        return user

    def get_all_users(self):
        # if not role in ["customer", "admin"]:
        #     raise ValueError(f"There is no {role} role. Either choose 'admin' or 'customer'")
        user = self.user_dao.get_all_users()
        if not user:
            log_event("Validation failed: " + str("There are no Users"))
            raise ValueError("There are no Users")
        log_event("Service operation successful")
        return user