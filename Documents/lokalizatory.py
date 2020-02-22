from selenium import webdriver
from time import sleep
import unittest
from selenium.webdriver.support.ui import Select

email = 'aaa@sjd.pl'
firstname = "ania"
lastname = "nowak"
invalid_password = 'k'
birthday = '19'
bithmonth = 'June'
birthyear = '1995'

class APRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get('http://automationpractice.com/index.php')
    def testCorrectRegistration(self):
        #kliknij sign in
        driver = self.driver
        sign_in = driver.find_element_by_class_name('login')
        sign_in.click()
        email_input=driver.find_element_by_id('email_create')
        email_input.send_keys(email)
        create_btn = driver.find_element_by_id('SubmitCreate')
        create_btn.click()
        sleep(3)
        driver.find_element_by_id('id_gender1').click()
        sleep(5)
        driver.find_element_by_id('customer_firstname').send_keys(firstname)
        driver.find_element_by_id('customer_lastname').send_keys(lastname)
        email_text = driver.find_element_by_id('email').get_attribute('value')
        assert email_text == email
        driver.find_element_by_id('passwd').send_keys(invalid_password)
        day_of_birth_select = Select(driver.find_element_by_id('days'))
        day_of_birth_select.select_by_value(birthday)
        sleep(3)
    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main(verbosity=2)
