class Users:
    def __init__(self, name, age, email, password, contact_number, role, user_id = None):
        self.user_id = user_id
        self.user_name = name
        self.age = age
        self.email = email
        self.password = password
        self.contact_number = contact_number
        self.role = role