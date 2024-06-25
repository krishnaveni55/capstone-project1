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
# Maximize window
        self.driver.maximize_window()

    def quit(self):
        self.driver.quit()

    def Positivelogin(self):
        self.boot()
#sleep execution check
        sleep(3)

# writing the usernamevalue
        username = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
        username.send_keys("Admin")

# writinging the password
        password = self.driver.find_element(By.XPATH,
                                            '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
        password.send_keys("admin123")

# click on login button
        loginbutton = self.driver.find_element(By.XPATH,
                                               '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
        loginbutton.click()
# Alert message
        print("The User is logged in successfully !!!")
        sleep(3)
        self.quit()


# Class Orangehrm with the URL
obj = Orangehrm("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
obj.Positivelogin()
