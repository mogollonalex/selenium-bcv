from re import search
import unittest
from selenium import webdriver
from time import sleep

class Tables(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= "chromedriver.exe")
        driver = self.driver
        driver.maximize_window()
        driver.get("http://www.mercadolibre.com/")

    def test_search_ps4(self): 
        driver = self.driver

        country = driver.find_element_by_id('VE')
        country.click()

        search_field = driver.find_element_by_name('as_word')
        search_field.click()
        search_field.clear()
        search_field.send_keys('Play station 4')
        search_field.submit()
        sleep(3)

        location = driver.find_element_by_partial_link_text('Distrito Capital')
        location.click()
        sleep(3)

        # condition = driver.find_element_by_xpath('/html/body/main/div/div[2]/aside/section[2]/div[2]/ul/li[1]/a/span[1]')
        # condition.click()
        # sleep(3)

        order_menu = driver.find_element_by_class_name('andes-dropdown__display-values')
        order_menu.click()
        higher_price = driver.find_element_by_xpath('//*[@id="andes-dropdown-más-relevantes-list-option-price_desc"]')
        higher_price.click()
        sleep(3)

        articles = []
        prices = []

        for i in range(5):
            article_name = driver.find_element_by_xpath(f'/html/body/main/div/div[2]/section/ol/li[{i + 1}]/div/div/div[2]/div[1]/a/h2').text
            articles.append(article_name)
            article_price = driver.find_element_by_xpath(f'/html/body/main/div/div[2]/section/ol/li[{i + 1}]/div/div/div[2]/div[2]/div[1]/div/div/div/div/span[1]/span[2]/span[2]').text
            prices.append(article_price)

        print(articles, prices)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()