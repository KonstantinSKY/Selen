# Selen Project file
# [name of Project]

# Just import all from selen module
from selen import *


# import you credential from security file  of your project and uncomment next line
# from security import *

# Class of your Project inherits Selen class, rename it by your Project

class Project(Selen):
    # Your Project Initialization method and setting of test
    def __init__(se, wd="Chrome"):
        super().__init__(wd)
        # Web-site and tests environment settings
        se.url = "https://testpages.herokuapp.com/styled/index.html"  # URL of Project
        se.ok_assert = False  # Switch of the assertion stop during the test
        se.ok_print = True    # Switch of print message during the test

    # The main Locators of the projects
    # Example:
    # l_login_btn = (CLASS, "Navigation_login__JL_4K")

    # Example of home page of testing website
    def home(se):
        se.WD.get(se.url)  # Get page from WD
        # Wait element and check inner text
        # se.Wait(l_h1).text('Looking for a developers, UX/UI designer, QA or DevOps...or development agency?')
        # se.title('iBench - real-time developers Hiring')  # Check title
        # se.curr_url("https://ibench.net/")  # Check url
        # se.Img(check=True).stat.out()
        # Check all Images

    # Each new test in new methods
    def test_name(se):
        pass


# You can start the file, and you can check your method here
if __name__ == "__main__":
    project = Project()
    project.home()
    project.test_name()
    print('FINISHED')
