print('selenium based Testing')

import unittest
from selenium import webdriver

class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('https://www.google.com/intl/en/about/')
        self.assertEqual('Google', self.browser.title)
        print(self.browser.title)
     
if __name__ == '__main__':
    unittest.main(verbosity=2)