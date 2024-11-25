from selenium.webdriver.common.by import By

class XpathPracticePage:
    #constructor initializes  page elements and store WebDriver instance
    def __init__(self, driver):
        self.driver = driver #Store WebDriver instance to interact with browser
        self.email_input = (By.XPATH, "//input[@placeholder='Enter email']")
        self.password_input = (By.XPATH, "//input[@id='pass']")
        self.company_input = (By.XPATH, "(//input[@placeholder='Enter your company'])[1]")
        self.mobile_input = (By.XPATH, "(//input[@placeholder='Enter your mobile number'])[1]")
        self.submit_button = (By.CSS_SELECTOR, "button[value='Submit']")
        self.cars_dropdown = (By.ID, "cars")
        self.checkout_dropdown = (By.XPATH, "//button[@class='dropbtn']")
        self.training_link = (By.LINK_TEXT, "Join Training")
        self.result_table_rows = (By.XPATH, "//table[@id='resultTable']//tbody//tr")

    #method to fill the form with provided data and submit
    def fill_form(self, email, password, company, phnumber):
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.company_input).send_keys(company)
        self.driver.find_element(*self.mobile_input).send_keys(phnumber)
        self.driver.find_element(*self.submit_button).click()