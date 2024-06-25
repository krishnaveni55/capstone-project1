from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


class Orangehrm:
   def __init__(self, url):
       self.url = url
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

   def boot(self):
       self.driver.get(self.url)

       sleep(3)
# Maximizing the window
       self.driver.maximize_window()

   def quit(self):
    self.driver.quit()

   def Negativelogin(self):
       self.boot()
       sleep(3)
       username=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
# writing username
       username.send_keys("Admin")
       password=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
# writing password
       password.send_keys("12345667")
       loginbutton=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')

       loginbutton.click()
       sleep(3)
# Alert message
       self.quit()
       print("Invalid credentials is displayed !!!")
# class orangehrm with the url
obj = Orangehrm("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
obj.Negativelogin()