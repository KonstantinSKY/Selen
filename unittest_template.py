import unittest
import HtmlTestRunner

# Import your Project class from project module
# Change to your project Name
from project_template import Project


class ChromePositiveTest(unittest.TestCase):
    browser_name = "Chrome"

    # Set up of unittests
    def setUp(self) -> None:
        self.project = Project(self.browser_name)

    # Example of test home page
    def test_home_page(self):
        self.project.home()

    # Add Each new test in simple methods
    def test_name(self):
        self.project.test_name()


# Classes for others browsers and web drivers
class FirefoxPositiveTest(ChromePositiveTest):
    browser_name = "Firefox"


class EdgePositiveTest(ChromePositiveTest):
    browser_name = "Edge"


class OperaPositive(ChromePositiveTest):
    browser_name = "Opera"


if __name__ == "__main__":
    # HTML report for the test
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./HtmlReport'))
