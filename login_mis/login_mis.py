from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver= webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://dev.baps.dev/mis/")
title =driver.title
print(title)
submit = driver.find_element(By.XPATH,"//input[@class='login-btn']")
submit.click()

driver.find_element(By.ID,"userName").send_keys("hiteshpatel1487")
driver.find_element(By.ID,"password").send_keys("Ims@0503")
driver.find_element(By.XPATH,"//button[text()='Sign In']").click()
driver.find_element(By.XPATH,"//button[text()='North America System Admin']").click()

user_name = driver.find_element(By.XPATH,'//*[@id="mainmenu"]/div/div[2]/h4[1]/strong')
user_name_text =user_name.text
print(user_name_text)
assert user_name_text == "USER : MANISH PATEL"
driver.find_element(By.XPATH,"//i[@class='las la-sign-out-alt logout-icon']").click()
driver.close()


