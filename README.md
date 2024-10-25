# Chitter Challenge

# User Stories
STRAIGHT UP

As a Maker
So that I can let people know what I am doing
I want to post a message (peep) to chitter
POSTS > add > content, user

As a maker
So that I can see what others are saying
I want to see all peeps in reverse chronological order
POSTS > view(reverse chronological)

As a Maker
So that I can better appreciate the context of a peep
I want to see the time at which it was made
POSTS > view(timestamp)

As a Maker
So that I can post messages on Chitter as me
I want to sign up for Chitter
USERS > add > email >password > name > username

HARDER

As a Maker
So that only I can post messages on Chitter as me
I want to log in to Chitter
USERS > Login

As a Maker
So that I can avoid others posting messages on Chitter as me
I want to log out of Chitter
USERS > logout

ADVANCED

As a Maker
So that I can stay constantly tapped in to the shouty box of Chitter
I want to receive an email if I am tagged in a Peep

USERS > email notificaiton

# Additional Notes
You don't have to be logged in to see the peeps.

Users sign up to chitter with their email, password, name and a username (e.g. samm@makersacademy.com, password123, Sam Morgan, sjmog).

The username and email are unique.

Peeps (posts to chitter) have the name of the user and their user handle.


## Setup

```shell

# Enter the directory
; cd YOUR_PROJECT_NAME

# Set up the virtual environment
; python -m venv solo_venv

# Activate the virtual environment
; source solo_venv/bin/activate 

# Install dependencies
(solo_venv); pip install -r requirements.txt
# Read below if you see an error with `python_full_version`

# Install the virtual browser we will use for testing
; playwright install
# If you encounter problems at this stage please contact your coach

# Create a test and development database
(solo_venv); createdb YOUR_PROJECT_NAME
(solo_venv); createdb YOUR_PROJECT_NAME_test

# Open lib/database_connection.py and change the database name to YOUR_PROJECT_NAME
(solo_venv); open lib/database_connection.py

# Seed the development database
(solo_venv); python seed_dev_database.py

# WRITE SOME TESTS

# Run the tests (with extra logging) 
(solo_venv); pytest -sv

# Run the app
(solo_venv); python app.py
# Now visit http://localhost:5001/emoji in your browser
```

<br>
<details>
  <summary>I get a <code>ModuleNotFoundError: No module named 'psycopg'</code></summary>
  <br>
If, after activating your <code>venv</code> and installing dependencies, you see this error when running <code>pytest</code>, please deactivate and reactivate your <code>venv</code>. This should solve the problem - if not, contact your coach.
</details>
<br>

If you would like to remove the example code:

```shell
; ./remove_example_code.sh
```
