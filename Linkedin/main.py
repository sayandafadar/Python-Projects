from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=marketing%20intern&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")
time.sleep(3)
sign_in = driver.find_element_by_xpath('/html/body/div[3]/a[1]')
sign_in.click()
time.sleep(6)
user_name = driver.find_element_by_xpath('//*[@id="username"]')
user_name.send_keys("dafadarts@gmail.com")
user_name.send_keys(Keys.ENTER)

password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys("IJe&i36ar#05fFMH")
password.send_keys(Keys.ENTER)

#Locate the apply button
time.sleep(5)
apply_button = driver.find_element_by_xpath('//*[@id="ember156"]/span')
apply_button.click()

#If application requires phone number and the field is empty, then fill in the number.
# time.sleep(5)
# phone = driver.find_element_by_class_name("fb-single-line-text__input")
# if phone.text == "":
#     phone.send_keys("7858825664")
#
# #Submit the application
# submit_button = driver.find_element_by_css_selector("footer button")
# submit_button.click()
