from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


class Orangehrm:  #creating class
   def __init__(self, url):
       self.url = url
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

   def boot(self):

       self.driver.get(self.url)

       sleep(3)
# Maximizing  window
       self.driver.maximize_window()

   def quit(self):
       self.driver.quit()

   def AddPIM(self):

       self.boot()
       sleep(3)
       username = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
# writing username
       username.send_keys("Admin")
       password = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
# writing password
       password.send_keys("admin123")
       loginbutton = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
       loginbutton.click()
       sleep(3)
# click on PIM module
       PIM=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')
       PIM.click()
       sleep(3)
# Adding employee details
       addpim=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button')
       addpim.click()
       sleep(3)
# writing firstname, lastname, employeeid values
       fname=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input')
       fname.send_keys("Arul")
       Lname=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input')
       Lname.send_keys("Sakthi")
       empid=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input')
       empid.send_keys("9865")
       print("New employee is added successfully !!!")
# class  ornagehrm url to perform all activities
obj = Orangehrm("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# Adding PIM
obj.AddPIM()