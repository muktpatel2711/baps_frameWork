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
#driver.get("https://uat.baps.dev/mis/")
driver.get("https://mis.na.baps.org/")
driver.maximize_window()
driver.find_element(By.XPATH,value="//input[@name='submit']").click()
driver.maximize_window()
sleepTime=3
driver.implicitly_wait(10)
username=driver.find_element(By.NAME,value="userName")
username.send_keys("3145377914")
print(username)
pwd=driver.find_element(By.NAME,value="password")
pwd.send_keys("Sw@mibapa1")
submit_burron = driver.find_element(By.XPATH, value="//button[@class='btn btn-primary btn-submit']").click()
driver.find_element(By.XPATH,value="//button[normalize-space()='North America System Admin']").click()
time.sleep(sleepTime)
ManagePerson= driver.find_element(By.XPATH, value="//span[normalize-space()='Manage Person']")
time.sleep(sleepTime)
action = ActionChains(driver)
action.move_to_element(ManagePerson).click().perform()
time.sleep(sleepTime)
SearchPerson=driver.find_element(By.XPATH,value="//span[normalize-space()='Search Person']")
SearchPerson.click()
time.sleep(sleepTime)
excel_file= 'C:\\Users\\supportadmin\\Desktop\\mis_yuvak.xlsx'
data_file = pd.read_excel(excel_file)
for index, row in data_file.iterrows():
    misid= row['BAPS ID Matching']
    email_address= row['Email']
    phone_number = row['Cell Phone']
    year_enter = row ['Year Entered Satsang']
    sabha_satatus = row['Sabha Status']
    kishor_yuvak = row['Kishore to Yuvak']
    MIS = driver.find_element(By.XPATH, value="//input[@formcontrolname='BAPSId']")
    MIS.clear()
    MIS.send_keys(misid)
    #time.sleep(sleepTime)
    MIS.send_keys(Keys.ENTER)
    time.sleep(4)
    driver.find_element(By.XPATH, value="(//a[@type='button'])[1]").click()
    #time.sleep(4)
    m_dept = driver.find_element(By.XPATH, "//div[@class='form-group mr-5']")
    attribute = m_dept.get_attribute("value")
    print(attribute)
    driver.find_element(By.XPATH,"(//button[@class='table-icon mr-1 ng-star-inserted'])[3]").click()
    time.sleep(sleepTime)
    yuva = driver.find_element(By.XPATH,"(//input[@role='combobox'])[26]")
    yuva.send_keys("yuvak")
    yuva.send_keys(Keys.ENTER)
    m_name =driver.find_element(By.XPATH,"//input[@placeholder='Middle Name']")
    name1=m_name.get_attribute("value")
    name_le = len(name1)
    print(name_le)
    if name_le == 2:
      m_name.send_keys(Keys.BACKSPACE)
    time.sleep(sleepTime)
    driver.find_element(By.XPATH, value="(//button[text()='Save'])[4]").click()
    time.sleep(sleepTime)
    driver.find_element(By.XPATH,value="//button[@class='close']").click()
    driver.find_element(By.XPATH, value="//strong[text()='Satsang Info']").click()
    time.sleep(sleepTime)
    # Satsang since year
    data = driver.find_element(By.XPATH, value="(//div[text()=' No data to display '])[7]")
    data_text = data.text
    print(data_text)
    if data_text == "No data to display":
        print(driver.find_element(By.XPATH, value="(//button[@class='table-icon ng-star-inserted'])[1]").click())
    else:
        driver.find_element(By.XPATH, value="(//button[@class='table-icon ng-star-inserted'])[1]").click()
        time.sleep(sleepTime)
    year_value = year_enter
    if pd.notnull(year_value) and year_value != "":
        dropdown_span = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='mat-select-value'])[2]")))
        dropdown_span.click()
        year_option = driver.find_element(By.XPATH, value=f"//span[text()={year_value}]")
        ActionChains(driver).move_to_element(year_option).click().perform()
        time.sleep(2)
        driver.find_element(By.XPATH, value="(//button[@type='submit'])[1]").click()
        time.sleep(sleepTime)
        # driver.back()
    else:
        driver.find_element(By.XPATH, value="//i[@class='las la-times-circle']").click()
        # driver.back()
    # Graduation_year
    try:
        data1 = driver.find_element(By.XPATH, value="(//div[text()=' No data to display '])[5]")
        data_text1 = data1.text
        print(data_text1)
    except:
        print("data not found")
    if data_text1 == "No data to display":
        driver.find_element(By.XPATH, value="(//button[@class='table-icon ng-star-inserted'])[3]").click()
    else:
        driver.find_element(By.XPATH, value="(//button[@class='table-icon ng-star-inserted'])[3]").click()
    enter_year = driver.find_element(By.XPATH, value="(//div[@class='mat-select-value'])[3]")
    enter_year.click()
    enter =kishor_yuvak
    e_year = driver.find_element(By.XPATH, value=f"//span[text()={enter}]")
    print(e_year)
    ActionChains(driver).move_to_element(e_year).click().perform()
    driver.find_element(By.XPATH, value="//button[@type='submit']").click()
    time.sleep(sleepTime)
    driver.find_element(By.XPATH, value="(//button)[10]").click()
    time.sleep(sleepTime)
    # Gread
    Attendance_Grade = driver.find_element(By.XPATH, value="(//input[@role='combobox'])[27]")
    Attendance_Grade.send_keys(sabha_satatus)
    Attendance_Grade.send_keys(Keys.ENTER)
    time.sleep(2)
    driver.find_element(By.XPATH, value="(//button[@class='btn btn-primary mr-4'])[1]").click()
    time.sleep(sleepTime)
    Attendance_Grade.click()
    time.sleep(sleepTime)
    # driver.find_element(By.XPATH,value="(//button[@aria-label='Close'])[1]").click()
    # time.sleep(sleepTime)
    # driver.back()
#email and phone
    #driver.find_element(By.XPATH, value="(//button)[10]").click()
   # time.sleep(3)
    driver.find_element(By.XPATH, value="//strong[text()=' Phone ']").click()
    try:
        primary_phone = driver.find_element(By.XPATH, "(//div[@class='col-2 mb-3 readonly break-word'])[1]")
        phone = primary_phone.text
        # Check if phone variable is empty or not containing the expected text
        if phone.strip() != "":
            # Perform click if text is present
            other = driver.find_element(By.XPATH, value="(//input[@role='combobox'])[46]")
            other.send_keys("Secondary Cell")
            other.send_keys(Keys.ENTER)
            time.sleep(3)
            Phone_id = driver.find_element(By.XPATH,value="(//mat-form-field[contains(@class, 'mat-primary')]//input[@formcontrolname='newPhone'])[2]")
            Phone_id.send_keys(phone_number)
            print(phone_number)
        else:
            Phone_id1 = driver.find_element(By.XPATH, value="(//mat-form-field[contains(@class, 'mat-primary')]//input[@formcontrolname='newPhone'])[1]")
            Phone_id1.send_keys(phone_number)
            print(phone_number)
    except NoSuchElementException:
        # Handle NoSuchElementException if element is not found
        pass
    driver.find_element(By.XPATH, value="(//button[text()='Save'])[7]").click()
    time.sleep(sleepTime)
    # Email
    time.sleep(3)
    driver.find_element(By.XPATH, value="//strong[text()=' Email ']").click()
    try:
        primary_email = driver.find_element(By.XPATH, "(//div[@class='col-2 mb-3 readonly break-word'])[3]")
        email = primary_email.text
        print(email)
        # Check if phone variable is empty or not containing the expected text
        if email.strip() != "":
            # Perform click if text is present
            other1 = driver.find_element(By.XPATH, value="(//input[@role='combobox'])[49]")
            other1.send_keys("Secondary")
            time.sleep(3)
            other1.send_keys(Keys.ENTER)
            driver.find_element(By.XPATH,value="(//mat-form-field[contains(@class, 'mat-primary')]//input[@formcontrolname='newEmail'])[2]").send_keys(email_address)
        else:
            driver.find_element(By.XPATH,value="(//mat-form-field[contains(@class, 'mat-primary')]//input[@formcontrolname='newEmail'])[1]").send_keys(email_address)
        print(misid)
    except NoSuchElementException:
        # Handle NoSuchElementException if element is not found
        pass
    driver.find_element(By.XPATH, value="(//button[text()='Save'])[8]").click()
    time.sleep(5)
    driver.find_element(By.XPATH, value="(//button[text()='Cancel'])[7]").click()
    driver.back()






