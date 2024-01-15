from selenium import webdriver


from selenium.common.exceptions import NoSuchElementException

import time

import pandas as pd
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
#driver.get("https://uat.baps.dev/mis/")
driver.get("https://dev.baps.dev/mis")
driver.find_element(By.XPATH, value="//input[@name='submit']").click()
time.sleep(3)
username =driver.find_element(By.NAME, value="userName")
username.send_keys("hiteshpatel1487")
pwd =driver.find_element(By.NAME, value="password")
pwd.send_keys("Ims@0503")
driver.find_element(By.XPATH, value="//button[@class='btn btn-primary btn-submit']").click()
roles = driver.find_elements(By.XPATH,"//button[@class='btn btn-primary']")
'''for i in range(len(roles)):
    role = driver.find_elements(By.XPATH, "//button[@class='btn btn-primary']")[i]
    role.click()
    time.sleep(2)
    position = driver.find_element(By.XPATH, "//div[@class='mat-select-value']")
    test = position.text
    print(test)
    time.sleep(3)
    driver.back()
    time.sleep(3)'''
driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()












