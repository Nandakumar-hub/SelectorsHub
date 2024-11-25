from selenium.webdriver.support.ui import Select
from PyTest.utils.baseclass import BaseClass
from PyTest.page.xpath import XpathPracticePage
from PyTest.utils.config import BASE_URL
from PyTest.utils.logger import logger, get_logger

logger = get_logger()
#TC_01 - Validate car dropdown selection functionality
def test_dropdown_selection():
    #initialize WebDriver instance using BaseClass
    driver = BaseClass().get_driver()
    driver.get(BASE_URL)
    #create instance of XpathPracticePage class to access its elements
    page = XpathPracticePage(driver)

    cars_dropdown = driver.find_element(*page.cars_dropdown)#find cars dropdown element using the locator from the XpathPracticePage class, unpack the tuple into two arguments: By.ID and "cars"
    select = Select(cars_dropdown)#create Select object to interact with the dropdown
    select.select_by_value("audi")#select "audi" option in the dropdown using its value

    #get the selected option's value from the dropdown
    selected_car = select.first_selected_option.get_attribute("value")
    #assert that the selected value is "audi"
    assert selected_car == "audi", logger.critical(f"Expected 'audi', but got {selected_car}.")
    logger.info("TC_01 - Dropdown selection test passed!")
    driver.quit()