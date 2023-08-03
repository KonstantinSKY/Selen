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
        se.url = "https://letcode.in/test"  # URL of Project
        se.ok_assert = False  # Switch of the assertion stop during the test
        se.ok_print = True    # Switch of print message during the test

    # The main Locators of the projects
    # Example:
    # l_login_btn = (CLASS, "Navigation_login__JL_4K")

    # Example of home page of testing website
    def test_input_field(se):
        se.WD.get(se.url)  # Get page from WD
        se.WD.title()

        se.Find(CLASS, "card-footer-item")
        print("WTF")
        se.click()
        print("WTF2")
        se.text("Edit")
        # # se.Wait(TAG, "title").out()
        # #
        # # se.title("Selenium Test Pages")
        # # se.check_page()
        # se.check_links()

        # Wait element and check inner text
        # se.Wait(l_h1).text('Looking for a developers, UX/UI designer, QA or DevOps...or development agency?')
        # se.title('iBench - real-time developers Hiring')  # Check title
        # se.curr_url("https://ibench.net/")  # Check url
        # se.Img(check=True).stat.out()
        # Check all Images
        se.WD.close()
    # Each new test in new methods
    def test_name(se):
        pass

    # Add Your tests .....

    
# You can start the file, and you can check your method here
if __name__ == "__main__":
    project = Project("Firefox")
    project.test_input_field()
    # project.test_name()
    print('FINISHED')