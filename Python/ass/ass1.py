from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
import time

url = 'https://www.facebook.com/lagin.php'

class FacebookLogin() :
    def __init__(self , email , password , browser):

        self.email = email 
        self.password = password 

        if browser == 'Chrome' :
            self.driver = webdriver.chrome(executable_path = ChromeDriverManager)
        elif browser == 'Firefox' :
            self.driver = webdriver.firefox(executable_path = firefoxDriverManager)
        self.driver.get(url)
        time.sleep(1)

    def login(self):
        email_element = self.driver.find_element(BY.ID , 'email')
        email_element.send_keys(self.email)

        password_elemnt self.driver.find_element(BY.ID , 'pass')
        password_elemnt.send_keys(self.password)

      login_button = self.driver.find_element(BY.Id , 'loginbutton')
      login_button.click()

       time.sleep(2)

    def MSg(self,msg):
        path_element = self.driver.find_element(By.XPath , '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]') 
        time.sleep(2)
        msg_element = self.driver.find_element(By.XPath , '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]') 
        msg_element.send_keys(msg)
        post_element = self.driver.find_element(By.XPath , '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]') 
        post_element.click()

if__name__ == '__main__'
    fb_lagin = FacebookLogin(email='', password = '' , browser = 'chrome')
    time.sleep(10)
    msg = 'This is my first automated post'

    fb_login.Msg(msg) 
    