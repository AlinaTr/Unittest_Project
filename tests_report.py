import unittest
import HtmlTestRunner

from Formy_Project_Website.Web_Form import CompleteWebForm
from The_Internet_Website.context_menu import TestContextMenu
from The_Internet_Website.direct_auth import AuthenticationInFirefox
from The_Internet_Website.js_alert import Alerts
from The_Internet_Website.keys import Keyboard
from The_Internet_Website.login_page import Login


class TestSuites(unittest.TestCase):

    def test_suite(self):
        run_tests = unittest.TestSuite()
        run_tests.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(CompleteWebForm),
                           unittest.defaultTestLoader.loadTestsFromTestCase(TestContextMenu),
                           unittest.defaultTestLoader.loadTestsFromTestCase(AuthenticationInFirefox),
                           unittest.defaultTestLoader.loadTestsFromTestCase(Alerts),
                           unittest.defaultTestLoader.loadTestsFromTestCase(Keyboard),
                           unittest.defaultTestLoader.loadTestsFromTestCase(Login)
                           ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title='Test Execution Report',
            report_name='Test Results for Formy-Project and The-Internet websites'
        )

        runner.run(run_tests)
