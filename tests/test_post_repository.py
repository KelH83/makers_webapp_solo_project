from lib.post_repository import PostRepository
from lib.post import Post
from datetime import datetime

def test_get_all_posts(db_connection): 
    db_connection.seed("seeds/chitter.sql") 
    repository = PostRepository(db_connection) 
    post = repository.all()
    assert post == [
        Post('Sheldon your room mate agreement can suck it', 1, '2024-10-24 15:41:36.070985', 1),
        Post('My intelligence, is the answer to why I deserve the noble prize', 2, '2024-10-24 15:41:36.070985', 2),
        Post('Magic is NOT just for little kids', 3, '2024-10-24 15:41:36.070985', 3),
        Post('Men get yourself some face cream, my face feels so soft!', 4, '2024-10-24 15:41:36.070985', 4),
        Post('I am finally doing it! I have a stand at comic con, please visit me :(', 5, '2024-10-24 15:41:36.070985', 5),
    ]

def test_get_all_posts_by_desc_order(db_connection): 
    db_connection.seed("seeds/chitter.sql") 
    repository = PostRepository(db_connection) 
    time1 = datetime.now()
    repository.create(Post("Article 7.3 of the roommate agreement", 2, time1))
    post = repository.all()
    assert post == [
        Post("Article 7.3 of the roommate agreement", 2, time1.strftime('%Y-%m-%d %H:%M:%S.%f'), 6),
        Post('Sheldon your room mate agreement can suck it', 1, '2024-10-24 15:41:36.070985', 1),
        Post('My intelligence, is the answer to why I deserve the noble prize', 2, '2024-10-24 15:41:36.070985', 2),
        Post('Magic is NOT just for little kids', 3, '2024-10-24 15:41:36.070985', 3),
        Post('Men get yourself some face cream, my face feels so soft!', 4, '2024-10-24 15:41:36.070985', 4),
        Post('I am finally doing it! I have a stand at comic con, please visit me :(', 5, '2024-10-24 15:41:36.070985', 5),
    ]

def test_get_all_posts_with_users(db_connection): 
    db_connection.seed("seeds/chitter.sql") 
    repository = PostRepository(db_connection) 
    post = repository.all_posts_with_users()
    assert post == [
    Post('Sheldon your room mate agreement can suck it', 1, '2024-10-24 15:41:36.070985', 1, "Duncan", "Leonard Hofstadter"),
    Post('My intelligence, is the answer to why I deserve the noble prize', 2, '2024-10-24 15:41:36.070985', 2, "Shelly", "Sheldon Cooper"),
    Post('Magic is NOT just for little kids', 3, '2024-10-24 15:41:36.070985', 3, "Froot_loops", "Howard Wolowitz"),
    Post('Men get yourself some face cream, my face feels so soft!', 4, '2024-10-24 15:41:36.070985', 4, "Raj", "Rajesh Koothrappali"),
    Post('I am finally doing it! I have a stand at comic con, please visit me :(', 5, '2024-10-24 15:41:36.070985', 5, "Stewie", "Stewart Bloom"),
]

def test_get_single_post(db_connection):
    db_connection.seed("seeds/chitter.sql")
    repository = PostRepository(db_connection)
    post = repository.find(3)
    assert post == Post('Magic is NOT just for little kids', 3, '2024-10-24 15:41:36.070985', 3)


def test_create_post(db_connection):
    db_connection.seed("seeds/chitter.sql")
    repository = PostRepository(db_connection)
    time = datetime.now()
    created_post = repository.create(Post("Article 7.3 of the roommate agreement", 2, time))
    assert created_post.id == 6
    assert created_post.content == "Article 7.3 of the roommate agreement"
    assert created_post.user_id == 2
    assert created_post.post_time == time

    result = repository.all()
    assert result == [
        Post("Article 7.3 of the roommate agreement", 2, time.strftime('%Y-%m-%d %H:%M:%S.%f'), 6),
        Post('Sheldon your room mate agreement can suck it', 1, '2024-10-24 15:41:36.070985', 1),
        Post('My intelligence, is the answer to why I deserve the noble prize', 2, '2024-10-24 15:41:36.070985', 2),
        Post('Magic is NOT just for little kids', 3, '2024-10-24 15:41:36.070985', 3),
        Post('Men get yourself some face cream, my face feels so soft!', 4, '2024-10-24 15:41:36.070985', 4),
        Post('I am finally doing it! I have a stand at comic con, please visit me :(', 5, '2024-10-24 15:41:36.070985', 5)
    ]

def test_delete_record(db_connection):
    db_connection.seed("seeds/chitter.sql")
    repository = PostRepository(db_connection)
    repository.delete(3)

    result = repository.all()
    assert result == [
        Post('Sheldon your room mate agreement can suck it', 1, '2024-10-24 15:41:36.070985', 1),
        Post('My intelligence, is the answer to why I deserve the noble prize', 2, '2024-10-24 15:41:36.070985', 2),
        Post('Men get yourself some face cream, my face feels so soft!', 4, '2024-10-24 15:41:36.070985', 4),
        Post('I am finally doing it! I have a stand at comic con, please visit me :(', 5, '2024-10-24 15:41:36.070985', 5),
    ]
