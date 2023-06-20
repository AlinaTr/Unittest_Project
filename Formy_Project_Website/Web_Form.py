from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class CompleteWebForm(unittest.TestCase):

    def setUp(self) -> None:
        self.firefox = webdriver.Firefox()
        self.firefox.maximize_window()
        self.firefox.get('https://formy-project.herokuapp.com/')
        website = self.firefox.find_element(By.LINK_TEXT, 'Complete Web Form')
        website.click()
        self.firefox.implicitly_wait(5)

    def tearDown(self) -> None:
        self.firefox.quit()

    def test_url(self):
        expected = 'https://formy-project.herokuapp.com/form'
        actual = self.firefox.current_url
        self.assertEqual(expected, actual)

    def test_h1(self):
        expected= 'Complete Web Form'
        actual = self.firefox.find_element(By.XPATH, '//h1[text()="Complete Web Form"]').text
        self.assertEqual(expected, actual)

    def test_page_title(self):
        expected = 'Formy'
        actual = self.firefox.title
        self.assertEqual(expected, actual)

    def test_hyperlink(self):
        expected = 'https://formy-project.herokuapp.com/'
        self.firefox.find_element(By.XPATH, '//*[@id="logo"]').click()
        actual = self.firefox.current_url
        self.assertEqual(expected, actual)

    def test_complete_form(self):
        self.firefox.find_element(By.ID, 'first-name').send_keys('Ana')
        self.firefox.find_element(By.ID, 'last-name').send_keys('Matei')
        self.firefox.find_element(By.ID, 'job-title').send_keys('Tester')
        self.firefox.find_element(By.XPATH, '//*[@id="radio-button-2"]').click()
        self.firefox.find_element(By.XPATH, '//*[@id="checkbox-2"]').click()
        self.firefox.find_element(By.XPATH, '//*[@value="3"]').click()
        self.firefox.find_element(By.ID, 'datepicker').send_keys('05/12/2022')
        self.firefox.find_element(By.XPATH, '//*[@role="button"]').click()

    def test_new_url(self):
        initial_url= self.firefox.current_url
        self.firefox.get('https://formy-project.herokuapp.com/thanks')
        new_url = self.firefox.current_url
        self.assertEqual(new_url, 'https://formy-project.herokuapp.com/thanks' )


    def test_h1_text_on_new_url_is_correct(self):
        self.firefox.get('https://formy-project.herokuapp.com/thanks')
        expected = 'Thanks for submitting your form'
        h1_text = self.firefox.find_element(By.XPATH, '//h1')
        actual = h1_text.text
        self.assertEqual(expected, actual)

    def test_success_message(self):
        self.firefox.get('https://formy-project.herokuapp.com/thanks')
        expected = 'The form was successfully submitted!'
        success_message= self.firefox.find_element(By.XPATH, '//*[@class="alert alert-success"]')
        actual = success_message.text
        self.assertEqual(expected, actual)








