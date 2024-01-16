from appium import webdriver

from appium.options.common import AppiumOptions

cap:dict[str,any] = {
    'platformName': 'Android',
    'platformVersion': '12',
    'deviceName': 'sdk_gphone64_x86_64',
    'app': "C:\\Users\\supportadmin\\Downloads\\Apxor Demo_ e-Commerce_2.2_apkcombo.com.apk",
    'automationName': 'UiAutomator2'
}

url = 'http://localhost:4723/wd/hub'

driver = webdriver.Remote(url,options=AppiumOptions().load_capabilities(cap))
driver.implicitly_wait(10)
