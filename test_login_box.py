def test_invalid_login(home):
    login = home.nav_to_login_box()

    username = 'username'
    password = 'password'
    login.login(username, password)
    assert 'Invalid login credentials' in login.invalid_login_alert()
