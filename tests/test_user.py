from lib.user import User

def test_user_constructs():
    user = User("Ames", "Amy Farrah Fowler", "BrainsRCool@neurobio.com", "Tum0ur", 1)
    assert user.id == 1
    assert user.user_name == "Ames"
    assert user.full_name== "Amy Farrah Fowler"
    assert user.email == "BrainsRCool@neurobio.com"
    assert user.user_password == "Tum0ur"

def test_users_format_nicely():
    user = User("Ames", "Amy Farrah Fowler", "BrainsRCool@neurobio.com", "Tum0ur", 1)
    assert str(user) == "User(ID: 1, User name: Ames, Full name: Amy Farrah Fowler, Email: BrainsRCool@neurobio.com)"