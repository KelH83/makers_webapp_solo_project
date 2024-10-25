class User:
    def __init__(self, user_name, full_name, email, user_password, id=None):
        self.id = id
        self.user_name = user_name
        self.full_name = full_name
        self.email = email
        self.user_password = user_password
        self.logged_in = False

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"User(ID: {self.id}, User name: {self.user_name}, Full name: {self.full_name}, Email: {self.email})"
    
    def is_valid(self):
        if self.user_name == None or self.user_name == "":
            return False
        if self.full_name == None or self.full_name == "":
            return False
        if self.email == None or self.email == "":
            return False
        if self.user_password== None or self.user_password== "":
            return False
        return True

    def generate_errors(self):
        errors = []
        if self.user_name== None or self.user_name== "":
            errors.append("Username can't be blank")
        if self.full_name== None or self.full_name== "":
            errors.append("Real name can't be blank")
        if self.email== None or self.email== "":
            errors.append("Email can't be blank")
        if self.user_password== None or self.user_password== "":
            errors.append("Password can't be blank")
        if len(errors) == 0:
            return None
        else:
            return ", ".join(errors)