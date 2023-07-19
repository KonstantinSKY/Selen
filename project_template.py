# Selen Project file
# [name of Project]

# Just import all from selen module
from selen import *


# import you credential from security file  of your project and uncomment next line
# from security import *

# Class of project inherits Selen class, rename it by your Project

class Project(Selen):

    def __init__(se, wd="Chrome"):
        super().__init__(wd)
        # Web-site and tests environment settings
        se.url = "https://ibench.net/"
        se.ok_assert = False
        se.ok_print = True

    # locators
    l_login_btn = (CLASS, "Navigation_login__JL_4K")
    l_login_fields = ((CLASS, "Login_form__2mvFD"), (TAG, "input"))

    l_fp_registration = (CLASS, "FrontPage_registrationLinks__2DkiO")
    l_btn_wrap = (CLASS, "FrontPage_btnWrapper__2Q75S")
    l_check_button = (CLASS, 'FrontPage_btnWrapper__2Q75S')
    l_btn = (TAG, "a")

    def home(se):
        se.WD.get(se.url)  # Get page from WD
        # Wait element and check inner text
        se.Wait(l_h1).text('Looking for a developers, UX/UI designer, QA or DevOps...or development agency?')
        se.title('iBench - real-time developers Hiring')  # Check title
        se.curr_url("https://ibench.net/")  # Check url
        se.Img(check=True).stat.out()
        # Check all Images

    def login(se):
        lc_submit_button = ((CLASS, "Login_submit_wrapper__2-PYe"), (TAG, "button"))  # Submit button locator

        se.home()  # Start main page
        se.Contains("Log in").click().Wait(l_h2).text("Log in")  # Click to login and wait for new page header with tex
        se.curr_url("https://ibench.net/login").title("Log in | iBench - real-time developers Hiring")
        # se.Img(check=True).check_links()

        # Enter email and password with checking for update 'value' attribute and green checkmarks
        se.Find(NAME, "email").type(EMAIL).sleep(0.2).attr('value', EMAIL).out()
        se.parent(2).tag("span").attr('class', 'validation_status_ok')
        # se.Find(NAME, "email").xpath_query().out("XPath")
        se.Find(NAME, "password").type(PASSW).sleep(0.2).attr('value', PASSW)
        se.parent(2).tag("span").attr('class', 'validation_status_ok')

        # se.Find(*lc_submit_button).click().sleep(2)  #click submit button
        se.Tag('button').click().sleep(2, 4)

        se.Wait(l_h1).text("Daily updates")
        se.curr_url("https://ibench.net/stats").title("Daily updates | iBench - real-time developers Hiring")
        # se.WD.close()# se.Img(check=True).check_links()

        # sleep(5)

    def about(se):
        se.Wait(l_h1).text(
            """iBench is an easy hiring way to find new highly-skilled Remote developers in 2-3 business days after your request.""")
        se.curr_url('https://ibench.net/about').title('About | iBench - real-time developers Hiring')
        se.Img(check=True).check_links()

    def blog(se):
        se.Wait(CLASS, "breadcrumbs").Tag("span", 1).text("Blog")
        se.curr_url('https://ibench.net/blog/').title('iBench - iBench - real-time developers Hiring')
        se.Img(check=True).check_links()

    def hire_remote_team(se):
        se.Wait(l_h1).text('Hire remote developers team')
        se.title().out("Title :")
        se.title("iBench - real-time developers Hiring")
        se.curr_url('https://ibench.net/team-search')  # .title('About | iBench - real-time developers Hiring')
        se.Img(check=True).check_links()

    def support_slack(se):
        se.Wait(CLASS, 'c-link').img().attr("alt", "Slack")

    def privacy(se):
        se.Wait(l_h1).text('Privacy Notice')
        se.curr_url('https://ibench.net/privacy-policy').title('Privacy Notice | iBench - real-time developers Hiring')
        se.Img(check=True).check_links()

    def cookie(se):
        se.Wait(l_h1).text('Cookie Policy')
        se.curr_url('https://ibench.net/cookie-policy').title('Cookie Policy | iBench - real-time developers Hiring')
        se.Img(check=True).check_links()

    def terms(se):
        se.Wait(l_h1).text('Terms Of Use')
        se.curr_url('https://ibench.net/terms-of-use').title('Terms Of Use | iBench - real-time developers Hiring')
        se.Img(check=True).check_links()

    def nav_menu(se, locator):
        texts = [elem.text for elem in se.Wait(locator).elems]
        for text in texts:
            se.Find(locator).contains(text)
            func = text.lower().replace(" ", "_")
            print("Checking menu element... ", func)
            old_url = se.curr_url()
            se.click()
            eval(f"se.{func}()")
            if old_url != se.curr_url():
                se.WD.back()
            sleep(1)

    def head_nav_menu(se):
        se.WD.get(se.url)  # Get page from WD
        se.Wait(CLASS, 'Navigation_menu__Xg4DA').tag('a')
        se.nav_menu(((CLASS, 'Navigation_menu__Xg4DA'), (TAG, 'a')))

    def foot_nav_menu(se):
        se.WD.get(se.url)  # Get page from WD
        se.Wait(CLASS, "cookieinfo-close").click()
        se.nav_menu(((CLASS, 'Footer_menu__3wGBS'), (TAG, 'a')))

    def login_cookies(se):
        se.add_cookies()
        se.WD.get(se.url + 'stats')
        sleep(20)
        # self.main_page()

    def registration(se):
        se.WD.get(se.url)
        se.WD.maximize_window()
        se.Wait(CLASS, "Navigation_btn__3RPM8").text("Register").out("Message: ")
        se.title("iBench - real-time developers Hiring").curr_url("https://ibench.net/")
        # se.Cls("Navigation_auth_buttons__29gW3").contains("Register").click()
        se.Contains("Register").click()
        se.Wait(TAG, "h2").text("Create your iBench account")
        se.title("Registration | iBench - real-time developers Hiring").curr_url("https://ibench.net/registration")
        # se.Img(check=True)
        se.Xpath("/html/body[1]/div[2]/span[1]/img[1] ").display()
        # se.Img(check=True)
        # se.check_links()
        se.Contains("Client").click()
        se.Find(NAME, "email").type("qa@smarttech.com").sleep(2).attr("value", "qa@smarttech.com").parent(2)
        se.tag("span").attr('class', 'validation_status_ok')
        se.Find(NAME, "company_name").type("Smart Technologies").attr("value", "Smart Technologies").parent(2)
        se.tag("span").attr('class', 'validation_status_ok')
        se.Find(NAME, "password").type("Serena2232").attr("value", "Serena2232").parent(2)
        se.tag("span").attr('class', 'validation_status_ok')
        se.Find(NAME, "password_copy").click(action=True).type("Serena2232").attr("value", "Serena2232").parent(2)
        se.tag("span").attr('class', 'validation_status_ok')
        se.Find(NAME, "country").dropdown_select("United States").click()
        se.Find(NAME, "terms_accepted").click(action=True)
        se.Contains("Try iBench").click(action=True)
        se.sleep(5)
        # se.Cls("validation_status_ok").attr("class", "validation_status_ok")

    def recovery_password(se):
        se.WD.get(se.url + "login")
        se.Wait(l_h2).text('Log in')
        se.Cls("Login_recovery_link__1asIj").sleep(1, 3).click()
        se.Wait(l_h1).text("Recovery password")
        se.title().out()
        se.curr_url("https://ibench.net/krecovery").title("Recovery password | iBench - real-time developers Hiring")
        se.Img(check=True)
        se.check_links()
        se.Contains({"name": "email", "type": "email"}).out()

    def find_it_company(se):
        se.WD.get(se.url)
        # se.WD.maximize_window()
        se.login()
        # se.Find(XPATH, "//li/a[contains(text(),'Find IT companies')]").click()
        # se.Contains("Find IT companies").click()
        se.Cls("DashboardMenu_menuLink__JkSw7", 3).click()
        se.curr_url('https://ibench.net/outsource').title("Outsource | iBench - real-time developers Hiring").sleep(3)
        se.Wait(l_h1).text("Find IT companies")
        se.Cls("Outsource_freeSlot__7mxFS").click()
        se.Find(NAME, "vetted").dropdown_select("1").click()
        se.parent(2).tag("span").attr('class', 'validation_status_ok')
        # se.Find(CLASS, "rw-input-reset").type("United States" + Keys.ENTER + "Canada" + Keys.ENTER)
        se.Find(NAME, "location").dropdown_multiselect(random_max=3)
        se.Find(NAME, "name").type("QA Project")
        se.Find(CLASS, "ql-editor").type("Our project is a software ")
        se.Find(NAME, "markets").dropdown_multiselect(random_max=4)
        # old not updated version of the script works in key-chains
        # se.Contains({"aria-owns":"rw_4_listbox rw_4_notify_area rw_4_taglist"}).type("Information Technology" + Keys.ENTER + "Technology" + Keys.ENTER)
        se.Tag("html").elem.send_keys(Keys.PAGE_DOWN)
        se.Tag("input").contains({"name": "budget"}).click(random=True)
        se.Tag("input").contains({"name": "project_start"}).click(random=True)
        # - #version with higher level of hierarchy for random click
        # se.Find((CLASS, "OutsourceAdding_radioGrouptWrapper__23Y0R", 1),(CLASS, "RadioButton_wrapper__3Q5Rq")).click(random=True)
        se.Find(NAME, "links").type('https://www.linkedin.com/')
        se.Cls("OutsourceAdding_submit__1o3MH").click(action=True)
        se.sleep(5)

    def find_employee(se):
        # se.WD.get(se.url + "login")
        se.login()
        se.Cls("DashboardMenu_menuLink__JkSw7", 2).click()
        se.curr_url('https://ibench.net/search-employee-slots').title(
            "Developers | iBench - real-time developers Hiring").sleep(2)
        # se.Cls("DashboardMenu_menuLink__JkSw7").contains("Find Employee").click()
        se.Cls("FreelancerSlots_free_slot__6EdsB").click()
        se.Find(NAME, "vetted").dropdown_select(2).click()
        # se.Find(CLASS, "rw-input-reset").type("United States" + Keys.ENTER) # working for one country
        se.Find(NAME, "location").dropdown_multiselect(random_max=2)
        se.Find(NAME, "job_title_id").dropdown_select(3).click()
        se.Find(CLASS, "ql-editor", 0).type(
            "Our company is currently looking for a talented  Developer to join our team.").sleep(2)
        se.Cls("SimpleEditor_label__3TQYk").click()
        se.Find(CLASS, "ql-editor", 1).type("Excellent problem-solving skills and attention to detail.")
        se.Find(NAME, "rate_month").type("100")
        se.Find(NAME, "position_level_id").dropdown_select(3).click()
        se.Find(NAME, "experience").dropdown_select(3).click()
        se.Find(NAME, "english_level_id").dropdown_select(4).click()
        se.Cls("label").attr("class", "form_control undefined validation_ok")
        se.Find(NAME, "skills").dropdown_multiselect(random_max=5)
        se.Contains("Activate").click(action=True)
        se.sleep(5)

    def find_contractors(se):
        # se.WD.get(se.url + "login")
        se.login()
        se.Cls("DashboardMenu_menuLink__JkSw7", 1).click()
        se.curr_url('https://ibench.net/search-slots').title("Developers | iBench - real-time developers Hiring").sleep(
            2)
        se.Cls("StartupSlots_free_slot__24a0Q").click()
        se.Find(NAME, "vetted").dropdown_select(2).click()
        se.Find(NAME, "slot_name").type("Name" + Keys.ENTER)
        se.Find(NAME, "location").dropdown_multiselect(random_max=2)
        se.Find(NAME, "job_title_id").dropdown_select(3).click()
        se.Contains("Maximum hourly rate").click()
        se.Find(XPATH, "//input[contains(@name,'rate_to')]").type("1000")  # boundary values 65535
        se.Find(NAME, "position_level_id").dropdown_select(3).click()
        se.Find(NAME, "experience").dropdown_select(3).click()
        se.Find(NAME, "english_level_id").dropdown_select(4).click()
        se.Cls("label").attr("class", "form_control undefined validation_ok")
        se.Find(NAME, "skills").dropdown_multiselect(random_max=5)
        se.Find(XPATH, "//div[contains(@class,'ql-editor ql-blank')]").type(
            "Our company is currently looking for a talented  Developer to join our team. " * 2).sleep(2)
        se.Contains("Activate").click(action=True)
        se.sleep(5)

    # Check registration with any random not existing email and not requires email confirmation as client
    def nt_registration_not_exist_email(se):
        se.WD.get(se.url)
        se.WD.maximize_window()
        se.Wait(CLASS, "Navigation_btn__3RPM8").text("Register").out("Message: ")
        se.title("iBench - real-time developers Hiring").curr_url("https://ibench.net/")
        # se.Cls("Navigation_auth_buttons__29gW3").contains("Register").click()
        se.Contains("Register").click()
        se.Wait(TAG, "h2").text("Create your iBench account")
        se.title("Registration | iBench - real-time developers Hiring").curr_url("https://ibench.net/registration")
        # se.Img(check=True)
        se.Xpath("/html/body[1]/div[2]/span[1]/img[1] ").display()
        # se.Img(check=True)
        # se.check_links()
        se.Contains("Client").click()
        se.Find(NAME, "email").type("9173454815@strange.email").sleep(2).attr("value",
                                                                              "9173454815@strange.email").parent(2)
        se.tag("span").attr('class', 'validation_status_ok')
        se.Find(NAME, "company_name").type("Smart Technologies").attr("value", "Smart Technologies").parent(2)
        se.tag("span").attr('class', 'validation_status_ok')
        se.Find(NAME, "password").type("Serena2232").attr("value", "Serena2232").parent(2)
        se.tag("span").attr('class', 'validation_status_ok')
        se.Find(NAME, "password_copy").click(action=True).type("Serena2232").attr("value", "Serena2232").parent(2)
        se.tag("span").attr('class', 'validation_status_ok')
        se.Find(NAME, "country").dropdown_select("United States").click()
        se.Find(NAME, "terms_accepted").click(action=True)
        se.Contains("Try iBench").click(action=True)
        se.sleep(5)

    # Check registration with any random password that contains of 201 symbol
    def nt_registration_200_symbol_pswd(se):
        se.WD.get(se.url)
        se.WD.maximize_window()
        se.Wait(CLASS, "Navigation_btn__3RPM8").text("Register").out("Message: ")
        se.title("iBench - real-time developers Hiring").curr_url("https://ibench.net/")
        # se.Cls("Navigation_auth_buttons__29gW3").contains("Register").click()
        se.Contains("Register").click()
        se.Wait(TAG, "h2").text("Create your iBench account")
        se.title("Registration | iBench - real-time developers Hiring").curr_url("https://ibench.net/registration")
        # se.Img(check=True)
        se.Xpath("/html/body[1]/div[2]/span[1]/img[1] ").display()
        # se.Img(check=True)
        # se.check_links()
        se.Contains("Client").click()
        se.Find(NAME, "email").type("TechForMed@medicalgr.com").sleep(2).attr("value",
                                                                              "TechForMed@medicalgr.com").parent(2)
        se.tag("span").attr('class', 'validation_status_ok')
        se.Find(NAME, "company_name").type("Smart Technologies").attr("value", "Smart Technologies").parent(2)
        se.tag("span").attr('class', 'validation_status_ok')
        se.Find(NAME, "password").type(
            "1" * 10 + "2" * 10 + "3" * 10 + "4" * 10 + "5" * 10 + "6" * 10 + "7" * 10 + "8" * 10 + "9" * 10 + "0" * 10 + "1").attr(
            "value",
            "1" * 10 + "2" * 10 + "3" * 10 + "4" * 10 + "5" * 10 + "6" * 10 + "7" * 10 + "8" * 10 + "9" * 10 + "0" * 10 + "1").parent(
            2)
        se.tag("span").attr('class', 'validation_status_ok')
        se.Find(NAME, "password_copy").click(action=True).type(
            "1" * 10 + "2" * 10 + "3" * 10 + "4" * 10 + "5" * 10 + "6" * 10 + "7" * 10 + "8" * 10 + "9" * 10 + "0" * 10 + "1").attr(
            "value",
            "1" * 10 + "2" * 10 + "3" * 10 + "4" * 10 + "5" * 10 + "6" * 10 + "7" * 10 + "8" * 10 + "9" * 10 + "0" * 10 + "1").parent(
            2)
        se.tag("span").attr('class', 'validation_status_ok')
        se.Find(NAME, "country").dropdown_select("United States").click()
        se.Find(NAME, "terms_accepted").click(action=True)
        se.Contains("Try iBench").click(action=True)
        se.sleep(5)

    # Check registration with any random password and other random password copy to verify allowance of different passwords
    def nt_registration_with_not_matched_pswds(se):
        se.WD.get(se.url)
        se.WD.maximize_window()
        se.Wait(CLASS, "Navigation_btn__3RPM8").text("Register").out("Message: ")
        se.title("iBench - real-time developers Hiring").curr_url("https://ibench.net/")
        # se.Cls("Navigation_auth_buttons__29gW3").contains("Register").click()
        se.Contains("Register").click()
        se.Wait(TAG, "h2").text("Create your iBench account")
        se.title("Registration | iBench - real-time developers Hiring").curr_url("https://ibench.net/registration")
        # se.Img(check=True)
        se.Xpath("/html/body[1]/div[2]/span[1]/img[1] ").display()
        # se.Img(check=True)
        # se.check_links()
        se.Contains("Client").click()
        se.Find(NAME, "email").type("TechForMed@medicalgr.com").sleep(2).attr("value",
                                                                              "TechForMed@medicalgr.com").parent(2)
        se.tag("span").attr('class', 'validation_status_ok')
        se.Find(NAME, "company_name").type("Smart Technologies").attr("value", "Smart Technologies").parent(2)
        se.tag("span").attr('class', 'validation_status_ok')
        se.print("FAIL", "doesn't match `Password`")
        se.Find(NAME, "password").type("1234567").attr("value", "1234567").parent(2)
        se.tag("span").attr('class', 'validation_status_ok')
        try:
            se.Find(NAME, "password_copy").click(action=True).type("7654321").attr("value", "7654321").parent(2)
            se.tag("span").attr('class', 'validation_status_ok')
        except NoSuchElementException:
            se.print("FAIL", "doesn't match `Password`")
        se.Find(NAME, "country").dropdown_select("United States").click()
        se.Find(NAME, "terms_accepted").click(action=True)
        se.Contains("Try iBench").click(action=True)
        se.title("Daily updates | iBench - real-time developers Hiring")
        try:
            se.title("Daily updates | iBench - real-time developers Hiring")
        except NoSuchElementException:
            print("FAIL", "Maching passwords are required for registrations to pass")
        se.sleep(5)

    # Check registration pass without accepted terms
    def nt_registration_with_not_accepted_terms(se):
        se.WD.get(se.url)
        se.WD.maximize_window()
        se.Wait(CLASS, "Navigation_btn__3RPM8").text("Register").out("Message: ")
        se.title("iBench - real-time developers Hiring").curr_url("https://ibench.net/")
        # se.Cls("Navigation_auth_buttons__29gW3").contains("Register").click()
        se.Contains("Register").click()
        se.Wait(TAG, "h2").text("Create your iBench account")
        se.title("Registration | iBench - real-time developers Hiring").curr_url("https://ibench.net/registration")
        # se.Img(check=True)
        se.Xpath("/html/body[1]/div[2]/span[1]/img[1] ").display()
        # se.Img(check=True)
        # se.check_links()
        se.Contains("Client").click()
        se.Find(NAME, "email").type("TechForMed@medicalgr.com").sleep(2).attr("value",
                                                                              "TechForMed@medicalgr.com").parent(2)
        se.tag("span").attr('class', 'validation_status_ok')
        se.Find(NAME, "company_name").type("Smart Technologies").attr("value", "Smart Technologies").parent(2)
        se.tag("span").attr('class', 'validation_status_ok')
        se.Find(NAME, "password").type("1234567").attr("value", "1234567").parent(2)
        se.tag("span").attr('class', 'validation_status_ok')
        se.Find(NAME, "password_copy").click(action=True).type("1234567").attr("value", "1324567").parent(2)
        se.tag("span").attr('class', 'validation_status_ok')
        se.Find(NAME, "country").dropdown_select("United States").click()
        se.Contains("Try iBench").click(action=True)
        try:
            se.title("Daily updates | iBench - real-time developers Hiring")
        except NoSuchElementException:
            print("FAIL", "Terms acceptance is required for registrations to pass")
        se.sleep(5)

    def sell_lead(se):
        se.login()
        se.Cls("DashboardMenu_menuLink__JkSw7").contains("Sell leads").click()
        se.check_page({"wait": (TAG, "h1"),
                       "url": "https://ibench.net/sell-leads",
                       "title": "Developers | iBench - real-time developers Hiring"
                       })

        se.Find(CLASS, "SellLeadButton_sellLeadsButton__3c0L8").click('')
        se.check_page({"wait": (TAG, "form"),
                       "url": "https://ibench.net/add-lead",
                       "title": "Sell leads | iBench - real-time developers Hiring"
                       })

        se.Wait(NAME, "vetted").dropdown_select()
        se.Cls("LeadForm_leadType__XWd1z").tag("span").click(random=True)
        se.Cls("LeadForm_qualificationLevelType__3PXrP").tag("span").click(random=True)
        se.Find(NAME, "fixed_price").type("10000")
        se.Find(NAME, "lead_sales_comment").type("Test comments 1")
        se.Find(NAME, "country").dropdown_select()
        se.Tag("button").contains("Next").click()
        se.Wait(CLASS, "LeadForm_aboutProject__OxQEz").text("About Project")
        se.Find(NAME, "project_type_id").dropdown_select()
        se.Find(NAME, "project_name").type("Project1")
        se.Find(NAME, "project_description").type("Project descr")
        se.Find(NAME, "budget").type(23423)
        se.Find(CLASS, "ant-picker-input").tag("input").elem.send_keys("04/06/2023")
        se.Find(NAME, "description_link").type("ibench.us")
        se.Find(NAME, "additional_comment").type("additional comment")
        se.Find(CLASS, "LeadForm_submit__1Ax9Y").click()
        se.Wait(CLASS, "CongratsModal_modalHeader__yA0p6").text("Congrats!")
        se.Find(CLASS, "CongratsModal_gotItButton__tJFaf").click()

        se.check_page({"wait": (TAG, "h1"),
                       "url": "Marketplace / Leads | iBench - real-time developers Hiring",
                       "title": "Sell leads | iBench - real-time developers Hiring"})

    # Verify system not accepts certain inserted value (digits only) into "User profile"(Base info)
    def adhoc_system_not_accepts_certain_value_digits(se):
        se.login()
        # se.sleep(8)
        se.Cls("Navigation_profile__hWSiK").click()
        # se.Find(XPATH, "//header/nav[1]/ul[1]/li[3]/a[1]").click(action=True)
        # se.Tag("ul").contains("Smart Technologies, Smart Technologies").click(action=True)
        se.check_page({"wait": (TAG, "h1"),
                       "url": "https://ibench.net/profile",
                       "title": "Startup profile | iBench - real-time developers search"})
        # se.Find(CLASS, "Profile_subMenuWrapper__fmpJL").attr("href", "/profile-edit").click(action=True)
        se.Find(XPATH, "//a[contains(text(),'Edit profile')]").click(action=True)
        se.check_page({"wait": (TAG, "h1"),
                       "url": "https://ibench.net/profile-edit",
                       "title": "Profile editing | iBench - real-time developers Hiring"})
        se.Find(NAME, "representative_name").type("1234567890" * 5)
        se.Find(NAME, "position").type("1234567890")
        se.Tag("button").contains("Submit").click(action=True).count()
        se.sleep(10)

    # Verify system not accepts certain inserted value (symbols only) into "User profile"(Company)
    def adhoc_system_not_accepts_certain_value_symbols(se):
        se.login()
        se.Cls("Navigation_profile__hWSiK").click()
        se.check_page({"wait": (TAG, "h1"),
                       "url": "https://ibench.net/profile",
                       "title": "Startup profile | iBench - real-time developers search"})
        # se.Find(CLASS, "Profile_subMenuWrapper__fmpJL").attr("href", "/profile-edit").click(action=True)
        se.Find(XPATH, "//a[contains(text(),'Edit profile')]").click(action=True)
        se.check_page({"wait": (TAG, "h1"),
                       "url": "https://ibench.net/profile-edit",
                       "title": "Profile editing | iBench - real-time developers Hiring"})
        se.Tag("ul").contains("Company").click(action=True)
        se.Find(NAME, "company_name").type(",").parent(2)
        se.tag("span").attr('class', 'validation_status_ok')
        se.Find(NAME, "site").type(",").parent(2)
        se.tag("span").attr('class', 'validation_status_ok')
        se.Find(NAME, "business_phone").type(",").parent(2)
        se.tag("span").attr('class', 'validation_status_ok')
        se.Find(NAME, "city").type(",").parent(2)
        se.tag("span").attr('class', 'validation_status_ok')
        se.Find(NAME, "address").type(",").parent(2)
        se.tag("span").attr('class', 'validation_status_ok')
        se.Tag("button").contains("Submit").click(action=True).count()
        se.sleep(10)

    # Verify system not accepts certain inserted value (symbols only) into "User profile"(Base info)
    def adhoc_system_has_restrictions_on_field_symbol_amount(se):
        se.login()
        se.Cls("Navigation_profile__hWSiK").click()
        se.check_page({"wait": (TAG, "h1"),
                       "url": "https://ibench.net/profile",
                       "title": "Startup profile | iBench - real-time developers search"})
        # se.Find(CLASS, "Profile_subMenuWrapper__fmpJL").attr("href", "/profile-edit").click(action=True)
        se.Find(XPATH, "//a[contains(text(),'Edit profile')]").click(action=True)
        se.check_page({"wait": (TAG, "h1"),
                       "url": "https://ibench.net/profile-edit",
                       "title": "Profile editing | iBench - real-time developers Hiring"})
        se.Tag("ul").contains("Additional info").click(action=True)
        se.Find(CLASS, "ql-editor").type("123")
        se.Find(NAME, "market_id").dropdown_select().parent(2)
        se.tag("span").attr('class', 'validation_status_ok')
        se.Find(NAME, "telegram").type("123").parent(2)
        se.tag("span").attr('class', 'validation_status_ok')
        se.Find(NAME, "linkedin").type("78").parent(2)
        se.tag("span").attr('class', 'validation_status_ok')
        se.Find(NAME, "twitter").type("123").parent(2)
        se.tag("span").attr('class', 'validation_status_ok')
        se.Find(NAME, "facebook").type("132").parent(2)
        se.tag("span").attr('class', 'validation_status_ok')
        se.Tag("button").contains("Submit").click(action=True).count()
        se.sleep(10)

    # Verify system not accepts certain inserted value (any symbols except digits) into "Fixed price" field (Sell lead)
    def adhoc_system_has_restrictions_on_field_fixed_price(se):
        se.login()
        se.Cls("DashboardMenu_menuLink__JkSw7").contains("Sell leads").click()
        se.check_page({"wait": (TAG, "h1"),
                       "url": "https://ibench.net/sell-leads",
                       "title": "Developers | iBench - real-time developers Hiring"
                       })

        se.Find(CLASS, "SellLeadButton_sellLeadsButton__3c0L8").click('')
        se.check_page({"wait": (TAG, "form"),
                       "url": "https://ibench.net/add-lead",
                       "title": "Sell leads | iBench - real-time developers Hiring"
                       })

        se.Wait(NAME, "vetted").dropdown_select()
        se.Cls("LeadForm_leadType__XWd1z").tag("span").click(random=True)
        se.Cls("LeadForm_qualificationLevelType__3PXrP").tag("span").click(random=True)
        se.Find(NAME, "fixed_price").type("1").type("fkjdfl$&^&*^$").parent(2).sleep(8)
        try:
            se.tag("span").attr('class',
                                'validation_status_ok')  # TODO = write script that'll check valid or invalid entry for the argument
        except NoSuchElementException:
            error = se.tag("span").attr('class', 'validation_status_error')
            required = se.tag('div').attr('class', 'validation_message').print('is required')
            print("Error", error)
            print("Is required", required)
        se.Find(NAME, "lead_sales_comment").type("Test comments 1")
        se.Find(NAME, "country").dropdown_select()
        se.Tag("button").contains("Next").click()
        se.Wait(CLASS, "LeadForm_aboutProject__OxQEz").text("About Project")
        se.Find(NAME, "project_type_id").dropdown_select()
        se.Find(NAME, "project_name").type("Project1")
        se.Find(NAME, "project_description").type("Project descr")
        se.Find(NAME, "budget").type(23423)
        se.Find(CLASS, "ant-picker-input").tag("input").elem.send_keys("04/06/2023")
        se.Find(NAME, "description_link").type("ibench.us")
        se.Find(NAME, "additional_comment").type("additional comment")
        se.Find(CLASS, "LeadForm_submit__1Ax9Y").click()
        se.Wait(CLASS, "CongratsModal_modalHeader__yA0p6").text("Congrats!")
        se.Find(CLASS, "CongratsModal_gotItButton__tJFaf").click()

        se.check_page({"wait": (TAG, "h1"),
                       "url": "Marketplace / Leads | iBench - real-time developers Hiring",
                       "title": "Sell leads | iBench - real-time developers Hiring"})

    # checking boundary value 0
    def bt_1_find_contractors(se):
        # se.WD.get(se.url + "login")
        se.login()
        se.Cls("DashboardMenu_menuLink__JkSw7", 1).click()
        se.curr_url('https://ibench.net/search-slots').title("Developers | iBench - real-time developers Hiring").sleep(
            2)
        se.Cls("StartupSlots_free_slot__24a0Q").click()
        se.Find(NAME, "vetted").dropdown_select(2).click()
        se.Find(NAME, "slot_name").type("Name" + Keys.ENTER)
        se.Find(NAME, "location").dropdown_multiselect(random_max=2)
        se.Find(NAME, "job_title_id").dropdown_select(3).click()
        se.Contains("Maximum hourly rate").click()
        se.Find(XPATH, "//input[contains(@name,'rate_to')]").type("0")  # boundary values 65535
        se.Find(NAME, "position_level_id").dropdown_select(3).click()
        se.Find(NAME, "experience").dropdown_select(3).click()
        se.Find(NAME, "english_level_id").dropdown_select(4).click()
        se.Cls("label").attr("class", "form_control undefined validation_ok")
        se.Find(NAME, "skills").dropdown_multiselect(random_max=5)
        se.Find(XPATH, "//div[contains(@class,'ql-editor ql-blank')]").type(
            "Our company is currently looking for a talented  Developer to join our team. " * 2).sleep(2)
        se.Contains("Activate").click(action=True)
        se.sleep(5)

    # checking boundary value 1
    def bt_2_find_contractors(se):
        # se.WD.get(se.url + "login")
        se.login()
        se.Cls("DashboardMenu_menuLink__JkSw7", 1).click()
        se.curr_url('https://ibench.net/search-slots').title(
            "Developers | iBench - real-time developers Hiring").sleep(
            2)
        se.Cls("StartupSlots_free_slot__24a0Q").click()
        se.Find(NAME, "vetted").dropdown_select(2).click()
        se.Find(NAME, "slot_name").type("Name" + Keys.ENTER)
        se.Find(NAME, "location").dropdown_multiselect(random_max=2)
        se.Find(NAME, "job_title_id").dropdown_select(3).click()
        se.Contains("Maximum hourly rate").click()
        se.Find(XPATH, "//input[contains(@name,'rate_to')]").type("1")  # boundary values 65535
        se.Find(NAME, "position_level_id").dropdown_select(3).click()
        se.Find(NAME, "experience").dropdown_select(3).click()
        se.Find(NAME, "english_level_id").dropdown_select(4).click()
        se.Cls("label").attr("class", "form_control undefined validation_ok")
        se.Find(NAME, "skills").dropdown_multiselect(random_max=5)
        se.Find(XPATH, "//div[contains(@class,'ql-editor ql-blank')]").type(
            "Our company is currently looking for a talented  Developer to join our team. " * 2).sleep(2)
        se.Contains("Activate").click(action=True)
        se.sleep(5)

    # checking boundary value 5643
    def bt_3_find_contractors(se):
        # se.WD.get(se.url + "login")
        se.login()
        se.Cls("DashboardMenu_menuLink__JkSw7", 1).click()
        se.curr_url('https://ibench.net/search-slots').title(
            "Developers | iBench - real-time developers Hiring").sleep(
            2)
        se.Cls("StartupSlots_free_slot__24a0Q").click()
        se.Find(NAME, "vetted").dropdown_select(2).click()
        se.Find(NAME, "slot_name").type("Name" + Keys.ENTER)
        se.Find(NAME, "location").dropdown_multiselect(random_max=2)
        se.Find(NAME, "job_title_id").dropdown_select(3).click()
        se.Contains("Maximum hourly rate").click()
        se.Find(XPATH, "//input[contains(@name,'rate_to')]").type("5643")  # boundary values 65535
        se.Find(NAME, "position_level_id").dropdown_select(3).click()
        se.Find(NAME, "experience").dropdown_select(3).click()
        se.Find(NAME, "english_level_id").dropdown_select(4).click()
        se.Cls("label").attr("class", "form_control undefined validation_ok")
        se.Find(NAME, "skills").dropdown_multiselect(random_max=5)
        se.Find(XPATH, "//div[contains(@class,'ql-editor ql-blank')]").type(
            "Our company is currently looking for a talented  Developer to join our team. " * 2).sleep(2)
        se.Contains("Activate").click(action=True)
        se.sleep(5)

    # checking boundary value 65535
    def bt_4_find_contractors(se):
        # se.WD.get(se.url + "login")
        se.login()
        se.Cls("DashboardMenu_menuLink__JkSw7", 1).click()
        se.curr_url('https://ibench.net/search-slots').title(
            "Developers | iBench - real-time developers Hiring").sleep(
            2)
        se.Cls("StartupSlots_free_slot__24a0Q").click()
        se.Find(NAME, "vetted").dropdown_select(2).click()
        se.Find(NAME, "slot_name").type("Name" + Keys.ENTER)
        se.Find(NAME, "location").dropdown_multiselect(random_max=2)
        se.Find(NAME, "job_title_id").dropdown_select(3).click()
        se.Contains("Maximum hourly rate").click()
        se.Find(XPATH, "//input[contains(@name,'rate_to')]").type("65535")  # boundary values 65535
        se.Find(NAME, "position_level_id").dropdown_select(3).click()
        se.Find(NAME, "experience").dropdown_select(3).click()
        se.Find(NAME, "english_level_id").dropdown_select(4).click()
        se.Cls("label").attr("class", "form_control undefined validation_ok")
        se.Find(NAME, "skills").dropdown_multiselect(random_max=5)
        se.Find(XPATH, "//div[contains(@class,'ql-editor ql-blank')]").type(
            "Our company is currently looking for a talented  Developer to join our team. " * 2).sleep(2)
        se.Contains("Activate").click(action=True)
        se.sleep(5)

    # checking boundary value 65536
    def bt_5_find_contractors(se):
        # se.WD.get(se.url + "login")
        se.login()
        se.Cls("DashboardMenu_menuLink__JkSw7", 1).click()
        se.curr_url('https://ibench.net/search-slots').title(
            "Developers | iBench - real-time developers Hiring").sleep(
            2)
        se.Cls("StartupSlots_free_slot__24a0Q").click()
        se.Find(NAME, "vetted").dropdown_select(2).click()
        se.Find(NAME, "slot_name").type("Name" + Keys.ENTER)
        se.Find(NAME, "location").dropdown_multiselect(random_max=2)
        se.Find(NAME, "job_title_id").dropdown_select(3).click()
        se.Contains("Maximum hourly rate").click()
        se.Find(XPATH, "//input[contains(@name,'rate_to')]").type("65536")  # boundary values 65535
        se.Find(NAME, "position_level_id").dropdown_select(3).click()
        se.Find(NAME, "experience").dropdown_select(3).click()
        se.Find(NAME, "english_level_id").dropdown_select(4).click()
        se.Cls("label").attr("class", "form_control undefined validation_ok")
        se.Find(NAME, "skills").dropdown_multiselect(random_max=5)
        se.Find(XPATH, "//div[contains(@class,'ql-editor ql-blank')]").type(
            "Our company is currently looking for a talented  Developer to join our team. " * 2).sleep(2)
        se.Contains("Activate").click(action=True)
        se.sleep(5)

    def main(se):
        pass


# You can start the file, and you can check your method here
if __name__ == "__main__":


    
    # iBench('Edge').foot_nav_menu()
    # iBench().login()
    # iBench().head_nav_menu()
    # iBench('Seleniumwire').login()
    # iBench().registration()
    # iBench().find_employee()
    # iBench().pt_find_contractors()
    # iBench().find_it_company()
    # iBench().login_cookies()
    # iBench().nt_registration_not_exist_email()
    # iBench().nt_registration_200_symbol_pswd()
    # iBench().nt_registration_with_not_accepted_terms()
    # iBench().adhoc_system_not_accepts_certain_value_digits()
    iBench().adhoc_system_not_accepts_certain_value_symbols()
    # iBench().adhoc_system_has_restrictions_on_field_symbol_amount()
    # iBench().adhoc_system_has_restrictions_on_field_fixed_price()
    # iBench().bt_5_find_contractors()
    print('FINISHED')
