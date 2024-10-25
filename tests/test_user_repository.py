from lib.user_repository import UserRepository
from lib.user import User
import pytest
from psycopg import errors


def test_get_all_users(db_connection): 
    db_connection.seed("seeds/chitter.sql") 
    repository = UserRepository(db_connection) 
    user = repository.all()
    assert user == [
        User(1,'Duncan', 'Leonard Hofstadter', 'LeonardH@ihatesheldon.com'),
        User(2,'Shelly','Sheldon Cooper', 'DrCopper@spockfanclub.com'),
        User(3,'Froot_loops','Howard Wolowitz', 'Wolowizard@Nasa.com'),
        User(4,'Raj', 'Rajesh Koothrappali', 'Raj@nerdsunited.com'),
        User(5,'Stewie', 'Stewart Bloom', 'StanL33Fan@thecomicshop.com')
    ]


def test_get_single_user(db_connection):
    db_connection.seed("seeds/chitter.sql")
    repository = UserRepository(db_connection)
    user = repository.find(2)
    assert user == User(2,'Shelly','Sheldon Cooper', 'DrCopper@spockfanclub.com')

def test_get_user_by_name(db_connection):
    db_connection.seed("seeds/chitter.sql")
    repository = UserRepository(db_connection)
    user = repository.find_by_name("Duncan")
    assert user == User('Duncan', 'Leonard Hofstadter', 'LeonardH@ihatesheldon.com','P3nny', 1)


def test_create_unique_user(db_connection):
    db_connection.seed("seeds/chitter.sql")
    repository = UserRepository(db_connection)
    created_user = repository.create(User("Ames", "Amy Farrah Fowler", "BrainsRCool@neurobio.com", "Tum0ur"))
    assert created_user.id == 6
    assert created_user.user_name == "Ames"
    assert created_user.full_name == "Amy Farrah Fowler"
    assert created_user.email == "BrainsRCool@neurobio.com"
    assert created_user.user_password == "Tum0ur"

    result = repository.all()
    assert result == [
        User(1,'Duncan', 'Leonard Hofstadter', 'LeonardH@ihatesheldon.com'),
        User(2,'Shelly','Sheldon Cooper', 'DrCopper@spockfanclub.com'),
        User(3,'Froot_loops','Howard Wolowitz', 'Wolowizard@Nasa.com'),
        User(4,'Raj', 'Rajesh Koothrappali', 'Raj@nerdsunited.com'),
        User(5,'Stewie', 'Stewart Bloom', 'StanL33Fan@thecomicshop.com'),
        User(6,"Ames", "Amy Farrah Fowler", "BrainsRCool@neurobio.com")
    ]

def test_create_user_duplicate_email(db_connection):
    db_connection.seed("seeds/chitter.sql")
    repository = UserRepository(db_connection)
    with pytest.raises(ValueError) as excinfo:
        repository.create(User("ImposterStew", "Sewart Clone", "StanL33Fan@thecomicshop.com", "Fake123"))
    assert str(excinfo.value) == "A user with the email StanL33Fan@thecomicshop.com already exists."

def test_create_user_duplicate_username(db_connection):
    db_connection.seed("seeds/chitter.sql")
    repository = UserRepository(db_connection)
    with pytest.raises(ValueError) as excinfo:
        repository.create(User("Stewie", "Sewart Clone", "Stew@thecomicshop.com", "Fake123"))
    assert str(excinfo.value) == "A user with the username Stewie already exists."

def test_delete_record(db_connection):
    db_connection.seed("seeds/chitter.sql")
    repository = UserRepository(db_connection)
    repository.delete(5)

    result = repository.all()
    assert result == [
        User(1,'Duncan', 'Leonard Hofstadter', 'LeonardH@ihatesheldon.com'),
        User(2,'Shelly','Sheldon Cooper', 'DrCopper@spockfanclub.com'),
        User(3,'Froot_loops','Howard Wolowitz', 'Wolowizard@Nasa.com'),
        User(4,'Raj', 'Rajesh Koothrappali', 'Raj@nerdsunited.com'),
    ]
