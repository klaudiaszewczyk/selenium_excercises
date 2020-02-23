from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest
firstname = 'julia'
lastname = 'nowak'
gender = 'male'
country_code="+48"
valid_phone_number = 112233445
adres_mailowy = 'justyna.gmail.com'
haslo_uzytkownika = 'trudnehasl0'
valid_country = 'Polska'


class WizzairRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://wizzair.com/pl-pl#/')
        '''
        Warunki wstepne
        '''
    def tearDown(self):
        self.driver.quit()
        '''
        Sprzatanie po tescie
        '''
    def testWrongEmail(self):
        #kliknij w prawym gornym rogu przycis zaloguj
        driver = self.driver
        zaloguj_btn = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.XPATH, '//button[@data-test="navigation-menu-signin"]')))
        zaloguj_btn.click()

        #kliknij rejestracja

        WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Rejestracja "]'))).click()
        time.sleep(3)
        # wprowadz imie

        fn = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.NAME, 'firstName')))
        fn.send_keys(firstname)

        #wprowadz nazwisko
        driver.find_element_by_name('lastName').send_keys(lastname)
        #wprowadz plec
        if gender == 'male':
            m = driver.find_element_by_xpath ('//label[@data-test = "register-gendermale"]')
            fn.click()
            m.click()

        else:
            driver.find_element_by_xpath('//label[@data-test="register-genderfemale"]').click()
        time.sleep(4)

        #wprowadz kod kraju
        cc = driver.find_element_by_xpath('//div[@data-test="booking-register-country-code"]')
        cc.click()
        cc2 = driver.find_element_by_xpath('//input[@name="phone-number-country-code"]')
        cc2.send_keys(country_code)
        country_to_choose = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//li[@data-test='PL']")))
        country_to_choose.click()
        time.sleep(4)
        #wpisz numer telefonu
        nmb = driver.find_element_by_name("phoneNumberValidDigits").send_keys(valid_phone_number)
        time.sleep(4)
        #wpisz nieprawidlowy adres email
        mail = driver.find_element_by_xpath('//input[@data-test="booking-register-email"]')
        mail.send_keys(adres_mailowy)
        time.sleep(3)
        #wpisz haslo
        haslo = driver.find_element_by_xpath('//input[@data-test="booking-register-password"]')
        haslo.send_keys(haslo_uzytkownika)
        time.sleep(4)
        #wybierz narodowosc
        country_field = driver.find_element_by_xpath('//input[@data-test="booking-register-country"]')
        country_field.click()
        # Wyszukaj kraje
        country_to_choose = driver.find_element_by_xpath("//div[@class='register-form__country-container__locations']")
        # Poszukaj elementow "label" wewnatrz listy "countries"
        countries = country_to_choose.find_elements_by_tag_name("label")
        # Iteruj po kazdym elemencie w liscie "countries"
        for label in countries:
            # Wewnatrz "label" znajdz element "strong"
            option=label.find_element_by_tag_name('strong')
            # Jesli tekst elementu jest taki jak zadany w valid_country
            if option.get_attribute("innerText") == valid_country:
                # Przewin do tego elementu
                option.location_once_scrolled_into_view
                # Kliknij
                option.click()
                # Wyjdz z petli - juz znalazlem i kliknalem
                break
        #marketing
        driver.find_element_by_xpath('//label[for="registration-privacy-policy-checkbox"][@class="rf-checkbox__label"]').click()
        sleep(4)




        '''
        test case 1 - niepoprawny adres email
        '''



if __name__ =='__main__':
    print('main')
    unittest.main(verbosity=2)
