from appium.webdriver.common.mobileby import MobileBy
from views.base_view import BaseView
from selenium.common.exceptions import TimeoutException


class LoginView(BaseView):
    USERNAME_INPUT = (MobileBy.ACCESSIBILITY_ID, 'username')
    PASSWORD_INPUT = (MobileBy.ACCESSIBILITY_ID, 'password')
    LOGIN_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'loginBtn')
    ALERT_LABEL = (MobileBy.ID, 'android:id/message')

    def login(self, username, password):
        self.wait_for(self.USERNAME_INPUT).send_keys(username)
        self.wait_for(self.PASSWORD_INPUT).send_keys(password)
        self.find(self.LOGIN_BUTTON).click()

    def invalid_login_alert(self):
        return self.wait_for(self.ALERT_LABEL).text

    def nav_back(self):
        from views.home_view import HomeView
        self.driver.back()
        return HomeView.instance(self.driver)
