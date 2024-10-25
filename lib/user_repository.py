from lib.user import User
from psycopg import errors

class UserRepository:
    def __init__(self, connection):
        self._connection = connection
    # READ
    def all(self):
        rows = self._connection.execute('SELECT * FROM users')
        users = []
        for row in rows:
            item = User(row["id"], row["user_name"], row["full_name"], row["email"])
            users.append(item)
        return users

    def find(self, user_id):
        rows = self._connection.execute('SELECT * FROM users WHERE id = %s', [user_id])
        row = rows[0]
        return User(row["id"], row["user_name"], row["full_name"], row["email"])
    
    def find_by_name(self, username):
        rows = self._connection.execute('SELECT * FROM users WHERE user_name = %s', [username])
        row = rows[0]
        return User(row["user_name"], row["full_name"], row["email"],row['user_password'], row["id"], )

    # CREATE
    def create(self, user):
        try:
            rows = self._connection.execute('INSERT INTO users (user_name, full_name, email, user_password) VALUES (%s, %s, %s, %s) RETURNING id', [
                                        user.user_name, user.full_name, user.email, user.user_password])
            row = rows[0]
            user.id = row["id"]
            return user
        except errors.UniqueViolation as e:
            if "users_email_key" in str(e):
                raise ValueError(f"A user with the email {user.email} already exists.")
            elif "users_user_name_key" in str(e):
                raise ValueError(f"A user with the username {user.user_name} already exists.")
            else:
                raise


    # DELETE
    def delete(self, user_id):
        self._connection.execute('DELETE FROM users WHERE id = %s', [user_id])
        return None


