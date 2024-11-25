from selenium.webdriver.support.ui import WebDriverWait

#WaitUtils class to encapsulate utility methods for wait
class WaitUtils:
    #static method to wait for new window
    @staticmethod
    def wait_for_new_window(driver, original_window_handle, timeout=10):
        #create an instance of WebDriverWait to wait for specific conditions
        wait = WebDriverWait(driver, timeout)
        #wait until a new window handle appears
        wait.until(lambda d: len(d.window_handles) > len(original_window_handle))
        return driver.window_handles[-1]  #return the handle of new window