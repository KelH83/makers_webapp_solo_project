from playwright.sync_api import Page, expect

def test_get_peeps(page, test_web_address): 
    page.goto(f"http://{test_web_address}/")
    img_tag = page.locator("img")
    expect(img_tag).to_be_visible()
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Welcome to Chitter")
    login_link = page.locator('.nav-item.login a')
    expect(login_link).to_be_visible()
    signup_link = page.locator('.nav-item.signup a')
    expect(signup_link).to_be_visible()
    user_name_box = page.locator('.peep .user-name').first
    expect(user_name_box).to_be_visible()
    real_name_box = page.locator('.peep .real-name').first
    expect(real_name_box).to_be_visible()

def test_get_logged_in(page, test_web_address): 
    page.goto(f"http://{test_web_address}/logged")
    logout_link = page.locator('.nav-item.logout a')
    peep_link = page.locator('.nav-item.make-peep a')
    expect(logout_link).to_be_visible()
    expect(peep_link).to_be_visible()

def test_post_new_peep(page, test_web_address): 
    page.goto(f"http://{test_web_address}/peep")
    h2_tag = page.locator("h2")
    expect(h2_tag).to_have_text("Create a Peep")
    page.fill("input[name='username']", "Shelly")
    page.fill("input[name='content']", "Today was a good day")
    page.click("text=Send Peep")
    page.wait_for_timeout(2000)
    page.goto(f"http://{test_web_address}/")
    first_peep = page.locator(".peep").first
    user_name = first_peep.locator(".user-name").inner_text()
    assert "Shelly" in user_name
    content = first_peep.locator(".content")
    expect(content).to_have_text("Today was a good day")

def test_get_signup(page, test_web_address): 
    page.goto(f"http://{test_web_address}/signup")
    home_link = page.locator('.nav-item.login a')
    expect(home_link).to_be_visible()
    h2_tag = page.locator("h2")
    expect(h2_tag).to_have_text("Sign up for an account")

def test_post_new_user(page, test_web_address): 
    page.goto(f"http://{test_web_address}/signup")
    page.fill("input[name='username']", "Ames")
    page.fill("input[name='full_name']", "Amy Farrah Fowler")
    page.fill("input[name='email']", "brainsrcool@neurobio1.com")
    page.fill("input[name='password']", "Tum0ur")
    page.click("text=Sign me up")

