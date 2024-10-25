class Post:
    def __init__(self, content, user_id, post_time, id=None, user_name = None, full_name = None):
        self.content = content
        self.user_id = user_id
        self.post_time = post_time
        self.id = id
        self.user_name = user_name
        self.full_name = full_name

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
            return f"Post(ID: {self.id}, Content: {self.content}, User ID: {self.user_id}, Time posted: {self.post_time})"

    def is_valid(self):
        if self.content == None or self.content == "":
            return False
        if self.user_id == None or self.user_id == "":
            return False
        return True

    def generate_errors(self):
        errors = []
        if self.content == None or self.content == "":
            errors.append("Peep can't be blank")
        if self.user_id == None or self.user_id == "":
            errors.append("Username can't be blank")
        if len(errors) == 0:
            return None
        else:
            return ", ".join(errors)