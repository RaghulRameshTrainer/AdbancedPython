import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
browser=webdriver.Chrome('chromedriver.exe')
class WebTesting(unittest.TestCase):
    def testBrowser(self):
        browser.get('http://www.google.com')
        assert 'Google' in browser.title
#
    def testSearch(self):
        sb=browser.find_element(By.NAME, "name")
        sb.send_keys('Google News' + Keys.RETURN)
        self.assertIn('Google', browser.title)
# browser.quit()