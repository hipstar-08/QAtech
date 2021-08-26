from behave import given, when, then

from pages.todo_page import TodoPage


class TestTodoPage(TodoPage):

    @given(u'Load the browser')
    def load_browser(self):
        self.driver = TodoPage()

    @then(u'Title is "{title_browser}"')
    def get_title(self, title_browser):
        title = TodoPage.get_title(self.driver)
        assert title == title_browser

    @then(u'Close the browser')
    def close_browser(self):
        TodoPage.close_driver(self.driver)

    @when(u'Todo item "{todo_item}" is added')
    def add_single_element(self, todo_item):
        TodoPage.add_todos_elements(self.driver, todo_item)
        TodoPage.enter_todo_list(self.driver)

    @then(u'Assert todo item "{todo_item}" is present')
    def verify_single_element_present(self, todo_item):
        assert todo_item == TodoPage.find_element_todo_text(self.driver).text

    @then(u'Assert single item todo count "{1}" is present')
    def add_single_element_count(self, one):
        assert one == TodoPage.find_element_todos_selected_count(self.driver).text

    @then(u'Assert item/items "{word}" is present')
    def add_single_element_item(self, word):
        assert word == TodoPage.find_element_item_or_items(self.driver).text

    @when(u'Click the select All dropdown')
    def single_element_select_dropdown(self):
        TodoPage.find_element_dropdown(self.driver).click()

    @then(u'Assert items "{0}" is present after clicking selectAll dropdown')
    def single_element_select_dropdown(self, zero):
        assert zero == TodoPage.find_element_todos_selected_count(self.driver).text

    @when(u'Click the Active todos button')
    def select_active_todos(self):
        TodoPage.find_element_select_active(self.driver).click()

    @when(u'Click the Completed todos button')
    def select_completed_todos(self, todo_text='test'):
        TodoPage.find_element_select_completed(self.driver).click()

    @then(u'Assert todo item is not present')
    def select_completed_todos(self):
        assert False.__eq__(TodoPage.show_completed_when_active_todo_present(self.driver))

    @when(u'Delete the todo item from list')
    def delete_added_completed_todo(self):
        TodoPage.find_element_clear_completed(self.driver).click()
