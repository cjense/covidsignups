import time
import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

file = open('num.txt', 'r')

num = file.read()
num = int(num)
num += 1
num = str(num)
file.close()

file = open('num.txt', 'w')
file.write(num)
file.close()

# variables
date = ""
sunday = ""
tuesday = "_test2"
thursday = "_test3"
url = "https://www.signupgenius.com/go/amherst_spring" + num
i = 0

# xpath variables
button_xpath = "//*[starts-with(@id,'checkbox')]"
first_xpath = "//input[@id='firstname']"
last_xpath = "//input[@id='lastname']"
email_xpath = "//input[@id='email']"

# initialize driver
driver = webdriver.Chrome("C:\\Users\\clair\\Desktop\\python projects\\chromedriver.exe")

while(i != 3):

    # check date
    if date == sunday:
        url = "https://www.signupgenius.com/go/amherst_spring" + num
        date = "_test2"
    elif date == tuesday:
        url = "https://www.signupgenius.com/go/amherst_spring" + num + date
        date = "_test3"
    elif date == thursday:
        url = "https://www.signupgenius.com/go/amherst_spring" + num + date
        date = ""
    i += 1

    driver.get(url)

    # find first signup button on the list, select and click submit
    button = driver.find_element_by_xpath(button_xpath).send_keys(' ')
    sumbit = driver.find_element_by_class_name("giantsubmitbutton.rounded.link_cursor").send_keys(' ')

    # fill in first and last name, fill email, then click submit

    # iframe = driver.find_element_by_xpath("//iframe[@name='Dialogue Window']")
    # driver.switch_to.frame(iframe)

    WebDriverWait(driver, 1000)
    #.until(EC.presence_of_element_located((By.ID, "firstname"))

    wait = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "firstname")))
    fill_first_name = driver.find_element_by_id('firstname').send_keys("Claire")
    fill_last_name = driver.find_element_by_xpath(last_xpath).send_keys("Jensen")
    fill_email = driver.find_element_by_xpath(email_xpath).send_keys("cjensen24@amherst.edu")
    fill_email = driver.find_element_by_name('btnSignUp').send_keys(' ')

    # go back to main page
    driver.implicitly_wait(4)
    back_to_signup = driver.find_element_by_class_name("btn.btn-xl.btn-success.ng-binding")

# quit driver
driver.quit()

# increase num every week
num += 1

file.close()