from selenium import webdriver
from selenium.webdriver.common.by import By
from MIS.config_data import config
import time


class login_mis():
    def __init__(self):
    #browser
        if config.browser == "Chrome":
            self.driver = webdriver.Chrome()
        elif config.browser == "Firefox":
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Edge()
    #URL
    def url(self):
        self.driver.get(config.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        print(config.browser)
        print(config.url)

    def submit(self):
        submit = self.driver.find_element(By.XPATH, config.submit_button_field)
        submit.click()

    def login(self,username,password):
        user = self.driver.find_element(By.ID, config.username_field)
        passw = self.driver.find_element(By.ID, config.password_filed)
        user.send_keys(config.username)
        passw.send_keys(config.password)

    def sign_in(self):
        sign = self.driver.find_element(By.XPATH, config.login_button_field)
        sign.click()

    def position(self):
        position = self.driver.find_element(By.XPATH, config.position_select)
        position.click()
        user_name = self.driver.find_element(By.XPATH, '//*[@id="mainmenu"]/div/div[2]/h4[1]/strong')
        print(user_name.text)
        assert user_name.text=="USER : MANISH PATEL"
    def signin(self):
        self.url()
        self.submit()
        self.login(config.username, config.password)
        self.sign_in()
        self.position()


if __name__ == '__main__':
    login = login_mis()
    login.signin()








