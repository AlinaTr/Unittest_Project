import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class TestContextMenu(unittest.TestCase):

    def setUp(self):
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.get("https://the-internet.herokuapp.com/context_menu")
        self.chrome.implicitly_wait(3)

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_context_menu(self):
        action = ActionChains(self.chrome)

        element = self.chrome.find_element(By.ID, "hot-spot")

        action.context_click(element).perform()

        alert = self.chrome.switch_to.alert
        text = alert.text

        self.assertEqual(text, "You selected a context menu")
        alert.accept()