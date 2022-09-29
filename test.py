import unittest
from selenium import webdriver
from script import Google

class GoogleTest(unittest.TestCase):

    @classmethod #Decoradores para correr en una sola instancia del navegador
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path= 'chromedriver.exe')

    def test_search(self):
        google = Google(self.driver)
        google.open()

#        google.search('Python')

#        self.assertEqual('Python', google.keyword)

    @classmethod
    def tearDownClass(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()