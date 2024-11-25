from selenium.webdriver.common.action_chains import ActionChains
from PyTest import page
from PyTest.utils.baseclass import BaseClass
from PyTest.utils.config import BASE_URL
from PyTest.utils.logger import logger, get_logger
from PyTest.utils.wait import WaitUtils
from PyTest.page.xpath import XpathPracticePage

logger = get_logger()

#TC_03 - Validate checkout dropdown functionality using mouse hover
def test_action_chains():
    #initialize WebDriver instance using BaseClass
    driver = BaseClass().get_driver()
    driver.get(BASE_URL)
    #create instance of XpathPracticePage class to access its elements
    page = XpathPracticePage(driver)
    #create an instance of ActionChains to perform mouse
    action = ActionChains(driver)
    dropdown = driver.find_element(*page.checkout_dropdown)#find checkout dropdown element using the locator from the XpathPracticePage class, unpack the tuple arguments
    action.move_to_element(dropdown).perform()#hover over the checkout dropdown to reveal options
    #locate the "Join Training" link and click on it
    join_training = driver.find_element(*page.training_link)
    action.move_to_element(join_training).click().perform()

    #get the original window handle
    original_window_handle = driver.window_handles
    #wait for a new window to open
    WaitUtils.wait_for_new_window(driver, original_window_handle)
    window_handles = driver.window_handles
    assert len(window_handles) > 1, logger.critical("New window was not opened!")
    logger.info("TC_03 - Action chains test passed!")
    driver.quit()