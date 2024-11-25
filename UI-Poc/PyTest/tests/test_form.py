from PyTest.page.xpath import XpathPracticePage
from PyTest.utils.baseclass import BaseClass
from PyTest.utils.config import BASE_URL
from PyTest.utils.logger import logger, get_logger

logger = get_logger()
#TC_02 - Validate form submission functionality
def test_form_submission():
    #initialize WebDriver instance using BaseClass
    driver = BaseClass().get_driver()
    driver.get(BASE_URL)
    #create instance of XpathPracticePage class to access its elements
    page = XpathPracticePage(driver)

    #test data for form submission
    email = "nganesamoorthy@altimetrik.com"
    password = "Nandakumar123"
    company = "Altimetrik"
    phnumber = "9688758312"
    #fill the form fields using the page object model
    page.fill_form(email, password, company, phnumber)
    #assert that the current URL is still the form page after submission
    assert driver.current_url == "https://selectorshub.com/xpath-practice-page/", logger.critical("URL did not match!")
    logger.info("TC_02 - Form submission test passed!")
    driver.quit()