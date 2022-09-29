from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Google(object):
    def __init__(self,driver):
        self._driver = driver
        self._url = 'http://www.bcv.org.ve/'
        self.search_locator = 'q'

    @property #Propiedad para busqueda
    def is_loaded(self):
        WebDriverWait(self._driver , 10).until(EC.presence_of_element_located((By.NAME, 'q')))
        return True

    @property
    def keyword(self):
        input_field = self._driver.find_element_by_name('q')
        return input_field.get_attribute('value')

    def open(self):
        self._driver.get(self._url)

    def test_search_text_field(self):
        bcv = self._driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[1]/div[1]/section[1]/div/div[2]/div/div[7]/div/div/div[2]/strong')
        print(bcv)
        return bcv.input_field.get_attribute('value')
        
    
    # def type_search(self, keyword):
    #     input_field = self._driver.find_element_by_name('q')
    #     input_field.send_keys(keyword)

    # def click_submit(self):
    #     button_submit = self._driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[2]/div[1]/div[1]/div/div[1]/div/span/svg')
    #     button_submit.click()

    # def search(self, keyword):
    #     self.type_search(keyword)
    #     self.click_submit