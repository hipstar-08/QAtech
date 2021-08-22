from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.locators import *
from selenium.webdriver.common.keys import Keys


class TodoPage(BasePage):

    def __init__(self):
        self.locator = ToDoPageLocators
        super(TodoPage, self).__init__()

    def find_element_search(self):
        self.driver.find_element(by=self.locator.CSS, value=self.locator.SEARCH_BAR)
        # return web_element

    def add_todos_elements(self, todo_text="abc"):
        web_element = self.driver.find_element(by=self.locator.CSS, value=self.locator.SEARCH_BAR)
        web_element.send_keys(todo_text)

    def enter_todo_list(self):
        self.driver.find_element(by=self.locator.CSS, value=self.locator.SEARCH_BAR).send_keys(Keys.RETURN)

    def find_element_todo_text(self):
        web_element = self.driver.find_element(by=self.locator.CSS, value=self.locator.FIRST_TODO)
        return web_element

    def find_element_todo_count(self):
        web_element = self.driver.find_element(by=self.locator.CSS, value=self.locator.NO_OF_TODOS_SELECTED)
        return web_element

    def find_element_dropdown(self):
        web_element = self.driver.find_element(by=self.locator.CSS, value=self.locator.SELECT_ALL_DROPDOWN)
        return web_element

    def find_element_checkbox_list(self):
        self.driver.find_elements(by=self.locator.CSS, value=self.locator.CHECKBOX_LIST)

    def find_element_single_web_element(self):
        web_element = self.driver.find_element(by=self.locator.CSS, value=self.locator.CHECKBOX_SINGLE_ELEMENT)
        return web_element

    def find_element_checkbox(self):
        web_element = self.driver.find_element(by=self.locator.CSS, value=self.locator.CHECKBOX)
        print(web_element.text)
        return web_element

    # def find_element_one_by_one(self, length_of_todos=len(self.driver.find_element(
    #         by=self.locator.CSS, value=self.locator.CHECKBOX_LIST))):
    #     for counter in range(1, length_of_todos + 1):
    #         self.find_element(str(*self.locator.CHECKBOX_ELEMENT_1) + str(
    #             counter) + str(*self.locator.CHECKBOX_ELEMENT_2))

    def find_element_todos_selected_count(self):
        web_element = self.driver.find_element(by=self.locator.CSS, value=self.locator.NO_OF_TODOS_SELECTED)
        return web_element

    def find_element_item_or_items(self):
        web_element = self.driver.find_element(by=self.locator.CSS, value=self.locator.ITEM_S)
        return web_element

    def find_element_select_all(self):
        self.driver.find_element(by=self.locator.CSS, value=self.locator.SELECT_ALL)

    def find_element_select_active(self):
        web_element = self.driver.find_element(by=self.locator.CSS, value=self.locator.SELECT_ACTIVE)
        return web_element

    def find_element_select_completed(self):
        web_element = self.driver.find_element(by=self.locator.CSS, value=self.locator.SELECT_COMPLETED)
        return web_element

    def find_element_completed_when_active_present(self):
        try:
            self.driver.find_element(by=self.locator.CSS, value=self.locator.CHECKBOX_LIST)
        except NoSuchElementException:
            return False

    def find_element_clear_completed(self):
        self.driver.find_element(by=self.locator.XPATH, value=self.locator.CLEAR_COMPLETED)
