from lib.post import Post
from lib.user import User

class PostRepository:
    def __init__(self, connection):
        self._connection = connection
    # READ
    def all(self):
        rows = self._connection.execute('SELECT * FROM posts ORDER BY post_time DESC')
        posts = []
        for row in rows:
            post_time_str = row["post_time"].strftime('%Y-%m-%d %H:%M:%S.%f')
            item = Post(row["content"], row["user_id"], post_time_str, row["id"])
            posts.append(item)
        return posts
    

    def all_posts_with_users(self):
        rows = self._connection.execute("SELECT posts.id AS post_id, user_id, content, user_name, full_name, post_time FROM posts JOIN users ON posts.user_id = users.id ORDER BY post_time DESC")
        posts = []
        for row in rows:
            post_time_str = row["post_time"].strftime('%Y-%m-%d %H:%M:%S.%f')
            item = Post(row["content"], row["user_id"], post_time_str, row["post_id"], row["user_name"], row["full_name"])
            posts.append(item)
        print("HERE: ", posts)    
        return posts


    def find(self, post_id):
        rows = self._connection.execute('SELECT * FROM posts WHERE id = %s', [post_id])
        row = rows[0]
        post_time_str = row["post_time"].strftime('%Y-%m-%d %H:%M:%S.%f')
        return Post(row["content"], row["user_id"], post_time_str, row["id"])

    # CREATE
    def create(self, post):
        rows = self._connection.execute('INSERT INTO posts (content, user_id, post_time) VALUES (%s, %s, %s) RETURNING id', [
                                    post.content, post.user_id, post.post_time])
        row = rows[0]
        post.id = row["id"]
        return post

    # DELETE
    def delete(self, post_id):
        self._connection.execute('DELETE FROM posts WHERE id = %s', [post_id])
        return None
