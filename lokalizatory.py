from selenium import webdriver
from time import sleep
import unittest

class APRegistration(unittest.TestCase):
    def setUP(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get('http://automationpractice.com/index.php')


    def testCorrectRegistration(self):
        #kliknij sign in
        driver = self.driver
        sign_in = driver.find_element_by_class_name('login')
        sign_in.click()
        sleep(5)
    def tearDown(self):
        pass

if __name__='__main__':
    unittest.main(verbosity=2)
