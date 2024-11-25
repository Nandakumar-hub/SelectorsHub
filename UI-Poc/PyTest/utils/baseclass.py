from selenium import webdriver

#BaseClass to manage WebDriver instance
class BaseClass:
    #constructor initializes WebDriver instance with specific settings
    def __init__(self):
        options = webdriver.ChromeOptions()
        #disable cookies by setting appropriate preference in ChromeOptions. This prevents cookies from being stored during the browser session
        options.add_experimental_option("prefs", {"profile.default_content_settings.cookies": 2})
        #instantiate Chrome WebDriver with configured options
        self.driver = webdriver.Chrome(options=options)
        #maximize the browser window after it is initialized
        self.driver.maximize_window()

    #method to retrieve WebDriver instance
    def get_driver(self):
        return self.driver
