import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.post_repository import PostRepository
from lib.user_repository import UserRepository
from lib.post import Post
from datetime import datetime
from lib.user import User

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_peeps():
    connection = get_flask_database_connection(app) 
    post_repository = PostRepository(connection)
    all_posts = post_repository.all_posts_with_users()
    return_list = []
    for post in all_posts:
        return_list.append(post)
    return render_template('posts.html',return_list=return_list)

@app.route('/logged', methods=['GET'])
def get_logged_in_peeps():
    connection = get_flask_database_connection(app) 
    post_repository = PostRepository(connection)
    all_posts = post_repository.all_posts_with_users()
    return_list = []
    for post in all_posts:
        return_list.append(post)
    return render_template('logged_in.html',return_list=return_list)

@app.route('/peep', methods=['GET'])
def get_new_peep():
            return render_template('new_peep.html')

@app.route('/peep', methods=['POST'])
def create_post():
    connection = get_flask_database_connection(app)
    repository = PostRepository(connection)
    user_repository = UserRepository(connection)
    user_to_find = request.form['username']
    user = user_repository.find_by_name(user_to_find)
    time = datetime.now()
    content = request.form['content']
    user_id =  user.id
    post = Post(content, user_id, time)

    if not post.is_valid():
        return render_template('/new_peep.html', post=post, errors=post.generate_errors()), 400

    post = repository.create(post)

    return redirect(f"/")

@app.route('/logged', methods=['GET'])
def get_logged_in():
            return render_template('logged_in.html')

@app.route('/signup', methods=['GET'])
def get_new_signup():
            return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def create_user():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    username = request.form['username']
    full_name = request.form['full_name']
    email = request.form['email']
    password = request.form['password']
    user = User(username, full_name, email, password)

    if not user.is_valid():
        return render_template('/signup.html', user=user, errors=user.generate_errors()), 400

    user = repository.create(user)

    return redirect(f"/")


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
