import time

from core.conf.config import configs
from selenium import webdriver


class BasePage:

    def __init__(self):
        if str(configs['browser']).lower() == "firefox":
            self.driver = webdriver.Firefox()
        elif str(configs['browser']).lower() == "chrome":
            self.driver = webdriver.Chrome()
        elif str(configs['browser']).lower() == "opera":
            self.driver = webdriver.Opera()
        self.driver.get(configs['ui_url'])
        self.driver.maximize_window()
        time.sleep(3)

    def get_driver(self):
        return self.driver

    # def maximize_browser(self):
    #     return self.driver.maximize_window()

    def get_title(self):
        return self.driver.title

    def close_driver(self):
        self.driver.close()
        self.driver.quit()
