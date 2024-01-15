import csv
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
driver.get("https://dev.baps.dev/mis")
driver.maximize_window()
driver.find_element(By.XPATH,value="//input[@name='submit']").click()
driver.maximize_window()
sleepTime=3
driver.implicitly_wait(10)
username=driver.find_element(By.NAME,value="userName")
username.send_keys("hiteshpatel1487")
print(username)
pwd=driver.find_element(By.NAME,value="password")
pwd.send_keys("Ims@0503")
submit_burron = driver.find_element(By.XPATH, value="//button[@class='btn btn-primary btn-submit']").click()
driver.find_element(By.XPATH,value="//button[normalize-space()='North America System Admin']").click()
time.sleep(sleepTime)
ManagePerson= driver.find_element(By.XPATH, value="//span[normalize-space()='Manage Person']")
time.sleep(sleepTime)
action = ActionChains(driver)
action.move_to_element(ManagePerson).click().perform()
time.sleep(sleepTime)
Addperson = driver.find_element(By.XPATH,value="//span[normalize-space()='Add Person']")
Addperson.click()
time.sleep(sleepTime)

excel_file= 'C:\\Users\\supportadmin\\Desktop\\Add_person.xlsx'
data_file1 = pd.read_excel(excel_file)
for index, row in data_file1.iterrows():
    firstname= row['First_name']
    middlename = row['Middle_name']
    lastname = row['Last_name']
    gender = row['Gender']
    maritalstatus = row['marital_status']
    mandal = row['Mandal']
    category = row['Category']
    membershipdept = row['Membership_dept']
    address = row['Address']
    zip = row['Zip']
    city = row['City']
    country= row['Country']
    state= row['State']
    center = row['Center']
    zone = row['Zone']
    primarycell = row['Primary_cell']
    primaryemail = row['Primary_email']








