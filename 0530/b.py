import unittest
import random
class MTestcase(unittest.TestCase):
    def test1(self):
        from selenium import webdriver
        driver=webdriver.Chrome()
        driver.get('http://localhost:5000')
        assert 'Flask Test' in driver.title

if __name__=='__main__':
    unittest.main()