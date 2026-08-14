from dao.users_dao import UserDAO

class UserServices:
    def __init__(self):
        self.user_dao = UserDAO()

    def add_user(self, user):
        if user.age < 18:
            raise ValueError("You must be 18 or above to register")
        if not user.email.strip():
            raise ValueError("Email cannot be empty")
        return self.user_dao.add_user(user)

    def log_in(self, email, password):
        user = self.user_dao.log_in(email, password)
        if not user:
            raise ValueError("Invalid credentials")
        return user
