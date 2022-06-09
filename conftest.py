import pytest
from appium import webdriver
from os import path
from views.home_view import HomeView

CUR_DIR = path.dirname(path.abspath(__file__))
ANDROID_APP = path.join(CUR_DIR, 'TheApp.apk')
IOS_APP = path.join(CUR_DIR, 'TheApp.app.zip')
APPIUM = 'http://localhost:4723'

ANDROID_CAPS = {
    'appium:platformName': 'Android',
    'appium:deviceName': 'Android Emulator',
    'appium:automationName': 'UiAutomator2',
    'appium:app': ANDROID_APP
}
IOS_CAPS = {
    'platformName': 'iOS',
    'platformVersion': '13.6',
    'deviceName': 'iPhone 11',
    'automationName': 'XCUITest',
    'app': IOS_APP,
}


def pytest_addoption(parser):  #option witch help to implement new flag pytest --platform=android/ios test_echo_box.py
    parser.addoption('--platform', action='store', default='android')


@pytest.fixture
def platform(request):  #request - fixture witch allow us to read command line options
    plat = request.config.getoption('--platform').lower()
    if plat not in ['ios', 'android']:
        raise ValueError('--platform value must be android or ios')
    return plat


@pytest.fixture
def driver(platform):
    caps = ANDROID_CAPS if platform == 'android' else IOS_CAPS
    driver = webdriver.Remote(APPIUM,caps)
    driver._platform = platform
    yield driver
    driver.quit()

@pytest.fixture
def home(driver):
    return HomeView.instance(driver)





