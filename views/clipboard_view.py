from appium.webdriver.common.mobileby import MobileBy
from views.base_view import BaseView


class ClipboardView(BaseView):
    MESSAGE_INPUT = (MobileBy.ACCESSIBILITY_ID, 'messageInput')
    SET_CLIPBOARD_BTN = (MobileBy.ACCESSIBILITY_ID, 'setClipboardText')
    REFRESH_CLIPBOARD_BTN = (MobileBy.ACCESSIBILITY_ID, 'refreshClipboardText')
    CLIPBOARD_VIEW = (MobileBy.ACCESSIBILITY_ID, 'Hubert test#!@')

    def set_clipboard_text(self, clipboard_text):
        self.wait_for(self.MESSAGE_INPUT).send_keys(clipboard_text)
        self.find(self.SET_CLIPBOARD_BTN).click()
        self.find(self.REFRESH_CLIPBOARD_BTN).click()

    def read_clipboard_text(self):
        return self.wait_for(self.CLIPBOARD_VIEW).text

    def nav_back(self):
        from views.home_view import HomeView
        self.driver.back()
        return HomeView.instance(self.driver)
