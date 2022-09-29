from email import header
import unittest
from selenium import webdriver
from time import sleep

class Tables(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= "chromedriver.exe")
        driver = self.driver
        driver.get("http://www.bcv.org.ve/")
#        driver.find_element_by_link_text("Sortable Data Tables").click()

    def test_sort_tables(self):
        driver = self.driver
        bcv = driver.find_element_by_xpath('//*[@id="dolar"]/div/div/div[2]/strong').text
        bcv = bcv.replace(",", ".")
        bcv = round(float(bcv), 2)
        print(bcv)
        self.assertEqual(8.15, bcv)
        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()