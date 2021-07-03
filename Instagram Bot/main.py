from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

Chrome_Driver_Path = "C:\Development\chromedriver.exe"
Instagram_Username = "pu.reheart"
Instagram_Password = 8877190290
Similar_account = "nofap.co"


class InstaFollower:

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.driver.get('https://www.instagram.com/accounts/login/')

    def login(self):
        time.sleep(2)
        username = self.driver.find_element_by_xpath('// *[ @ id = "loginForm"] / div / div[1] / div / label / '
                                                     'input')
        username.send_keys(Instagram_Username)
        time.sleep(3)
        password = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(Instagram_Password)
        time.sleep(3)
        password.send_keys(Keys.ENTER)
        time.sleep(3)
        not_now = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        not_now.click()
        time.sleep(4)

        notification = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        notification.click()

    def find_followers(self):
        time.sleep(4)
        click_search_option = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div['
                                                                '2]/div/div')
        click_search_option.click()
        time.sleep(3)
        search_for_the_inspired_account = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div['
                                                                            '2]/div/div/div[ '
                                                                            '2]/input')
        search_for_the_inspired_account.send_keys(Similar_account)
        search_for_the_inspired_account.send_keys(Keys.ENTER)
        search_for_the_inspired_account.click()
        time.sleep(6)

        inspired_account = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div['
                                                             '2]/div[ '
                                                             '4]/div/a[1]')
        inspired_account.send_keys(Keys.ENTER)
        inspired_account.click()

        time.sleep(5)

        folLowers_of_the_inspired_account = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul'
            '/li[2]/a')
        folLowers_of_the_inspired_account.click()
        folLowers_of_the_inspired_account.send_keys(Keys.ENTER)

        time.sleep(5)
        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower(Chrome_Driver_Path)
bot.login()
bot.find_followers()
bot.follow()
