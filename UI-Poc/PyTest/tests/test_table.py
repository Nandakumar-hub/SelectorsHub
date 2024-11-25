from PyTest.page.xpath import XpathPracticePage
from PyTest.utils.baseclass import BaseClass
from PyTest.utils.config import BASE_URL
from PyTest.utils.logger import logger, get_logger

logger = get_logger()

#TC_04 - Verify usernames containing "Jo" in the table data
def test_table_data():
    #initialize WebDriver instance using BaseClass
    driver = BaseClass().get_driver()
    driver.get(BASE_URL)
    #create instance of XpathPracticePage class to access its elements
    page = XpathPracticePage(driver)
    #find all rows in the user's table using the locator defined in the page object model
    rows = driver.find_elements(*page.result_table_rows)
    #extract the text content of each row and store it in a list of usernames
    usernames = [row.text for row in rows]
    #count the number of rows where the username contains the string 'Jo'
    jo_count = sum(1 for username in usernames if "Jo" in username)
    assert jo_count <= 3, logger.critical(f"'Jo' count exceeded: {jo_count}")
    logger.info(f"Count of rows containing 'Jo': {jo_count}")
    driver.quit()