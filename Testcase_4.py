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

    def EditPIM(self):
        self.boot()
        sleep(3)
        username = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
# writing the username
        username.send_keys("Admin")
        password = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
# writing password
        password.send_keys("admin123")
        loginbutton = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
        loginbutton.click()
        sleep(3)
# Click on PIM module
        PIM = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')
        PIM.click()
        sleep(3)
# Searching the added employee name
        emp_name=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input')
        emp_name.send_keys("Arul Sakthi")
        sleep(2)
        search=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]')
        search.click()
        sleep(3)
# Edit the found employee details
        edit=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[2]')
        sleep(3)
        edit.click()
        sleep(5)
        nickname=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input')
        nickname.send_keys("jo")
        sleep(2)
        print("sucessfully updated ")
# class orangehrm to perform all the commands
obj = Orangehrm("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
obj.EditPIM()