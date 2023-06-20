import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Keyboard(unittest.TestCase):

    def setUp(self):
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.get("https://the-internet.herokuapp.com/login")
        self.chrome.implicitly_wait(3)

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_various_keys(self):
        # trimitem valori de la tastatura in browser
        user = self.chrome.find_element(By.ID, "username")
        user.send_keys("anton")
        time.sleep(2)

        user.clear()
        user.send_keys("tomsmith")
        time.sleep(2)

        # daca vreau ca dupa ce am scris tomsmith in casuta pentru username
        # sa fac ctrl + a pe acesta:

        # trebuie sa importam clasa Keys din selenium.webdriver.common.keys
        user.send_keys(Keys.CONTROL, "a")
        time.sleep(2)
        user.send_keys(Keys.BACKSPACE)
        time.sleep(2)

        user.send_keys(Keys.SHIFT, 2)
        time.sleep(2)