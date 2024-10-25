from lib.post import Post
from datetime import datetime

def test_post_constructs():
    time = datetime.now()
    post = Post("I just looked at the list of this year's noble prize winners..chumps", 2,time, 1)
    assert post.id == 1
    assert post.content == "I just looked at the list of this year's noble prize winners..chumps"
    assert post.user_id == 2
    assert post.post_time == time

def test_posts_format_nicely():
    time = datetime.now()
    post = Post("I just looked at the list of this year's noble prize winners..chumps", 2, time,1)
    assert str(post) == f"Post(ID: 1, Content: I just looked at the list of this year's noble prize winners..chumps, User ID: 2, Time posted: {time})"

