import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Login(unittest.TestCase):

    def setUp(self):
        self.chrome= webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.get('https://the-internet.herokuapp.com/')
        self.chrome.find_element(By.LINK_TEXT, 'Form Authentication').click()

    def tearDown(self):
        self.chrome.quit()

    def test_new_url_is_correct(self):
        expected = 'https://the-internet.herokuapp.com/login'
        actual = self.chrome.current_url
        self.assertEqual(expected, actual)

    def test_page_title_is_correct(self):
        expected = 'The Internet'
        actual = self.chrome.title
        self.assertEqual(actual, expected)

    def test_text_h2_is_correct(self):
        expected = 'Login Page'
        actual = self.chrome.find_element(By.XPATH, '//h2').text
        self.assertEqual(actual, expected)

    def test_login_button_is_displayed(self):
        self.assertTrue(self.chrome.find_element(By.CLASS_NAME, 'radius').is_displayed())

    def test_href_attribute_link_is_correct(self):
        link_element = self.chrome.find_element(By.LINK_TEXT, 'Elemental Selenium')
        expected = 'http://elementalselenium.com/'
        actual = link_element.get_attribute('href')
        self.assertEqual(expected, actual)

    def test_login_no_credentials_inserted(self):
        self.chrome.find_element(By.CLASS_NAME, 'radius').click()

        error_message= self.chrome.find_element(By.ID, 'flash')

        self.assertTrue(error_message.is_displayed())

    def test_login_invalid_credentials(self):
        user = self.chrome.find_element(By.ID, 'username')
        user.send_keys('tom')
        password = self.chrome.find_element(By.ID, 'password')
        password.send_keys('ssss')

        login_btn = self.chrome.find_element(By.CLASS_NAME, 'radius')
        login_btn.click()

        error_message = self.chrome.find_element(By.ID, 'flash')
        expected = 'Your username is invalid!'

        self.assertIn(expected, error_message.text)

    def test_err_disappear_if_x_is_clicked(self):
        login_btn = self.chrome.find_element(By.TAG_NAME, 'button')
        login_btn.click()

        x_btn = self.chrome.find_element(By.XPATH, '//a[@class="close"]')
        x_btn.click()
        time.sleep(5)

        with self.assertRaises(NoSuchElementException):
            self.chrome.find_element(By.XPATH, '//div[@class="flash error"]')

    def test_label_text(self):
        labels = self.chrome.find_elements(By.TAG_NAME, 'label')

        self.assertEqual('Username', labels[0].text)
        self.assertEqual('Password', labels[1].text)

    def test_valid_credentials_login(self):
        self.chrome.find_element(By.ID, 'username').send_keys('tomsmith')
        self.chrome.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')

        self.chrome.find_element(By.CLASS_NAME, 'radius').click()

        self.assertIn('/secure', self.chrome.current_url)

        success_element = WebDriverWait(self.chrome, 4).until(EC.presence_of_element_located((By.XPATH, '//*[@class="flash success"]')))

        self.assertTrue(success_element.is_displayed())
        self.assertIn('secure area!', success_element.text)

    def test_logout_success(self):
        self.chrome.find_element(By.ID, 'username').send_keys('tomsmith')
        self.chrome.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')

        self.chrome.find_element(By.CLASS_NAME, 'radius').click()
        self.chrome.find_element(By.XPATH, '//a[@class="button secondary radius"]').click()

        expected = 'https://the-internet.herokuapp.com/login'
        self.assertEqual(expected, self.chrome.current_url)

    """
    Test  - brute force password hacking
    - Completează user tomsmith
    - Găsește elementul //h4
    - Ia textul de pe el și fă split după spațiu. Consideră fiecare cuvânt ca o
    potențială parolă.
    - Folosește o structură iterativă prin care să introduci rând pe rând
    parolele și să apeși pe login.
    - La final testul trebuie să îmi printeze fie
    ‘Nu am reușit să găsesc parola’
    ‘Parola secretă este [parola]’

    """

    def test_brute_force_password_hacking(self):
        h4_element = self.chrome.find_element(By.XPATH, '//h4')
        h4_words = h4_element.text.split()

        for possible_password in h4_words:
            username = self.chrome.find_element(By.ID, 'username')
            username.send_keys('tomsmith')

            password = self.chrome.find_element(By.ID, 'password')
            password.send_keys(possible_password)

            login_btn = self.chrome.find_element(By.CLASS_NAME, 'radius')
            login_btn.click()

            if 'secure' in self.chrome.current_url:
                print(f'Parola secreta este {possible_password}')
                break
            print('Nu am reusit sa gasesc parola!')















