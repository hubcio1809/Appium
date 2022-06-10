from appium.webdriver.common.mobileby import MobileBy
from views.base_view import BaseView
from views.echo_view import EchoView
from views.login_view import LoginView
from views.clipboard_view import ClipboardView


class HomeView(BaseView):
    ECHO_ITEM = (MobileBy.ACCESSIBILITY_ID, 'Echo Box')
    LOGIN_ITEM = (MobileBy.ACCESSIBILITY_ID, 'Login Screen')
    CLIPBOARD_ITEM = (MobileBy.ACCESSIBILITY_ID, 'Clipboard Demo')

    def nav_to_echo_box(self):
        self.wait_for(self.ECHO_ITEM).click()
        return EchoView.instance(self.driver)

    def nav_to_login_box(self):
        self.wait_for(self.LOGIN_ITEM).click()
        return LoginView.instance(self.driver)

    def nav_to_clipboard_box(self):
        self.wait_for(self.CLIPBOARD_ITEM).click()
        return ClipboardView.instance(self.driver)
