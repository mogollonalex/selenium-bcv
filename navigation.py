import unittest
from selenium import webdriver
from time import sleep

class Tables(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= "chromedriver.exe")
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://www.google.com/")

    def test_browser_navigation(self):
       driver = self.driver

       search_file = driver.find_element_by_name('q')
       search_file.clear()
       search_file.send_keys('pytronicca')
       search_file.submit()

       driver.back()
       sleep(3)
       driver.forward()
       sleep(3)
       driver.refresh()
       sleep(3)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()