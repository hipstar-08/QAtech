from behave import given, when, then
from pages.todo_page import TodoPage

# scenarios('../features/todo_app.feature', example_converters=dict(phrase=str))


class TestTodoPage(TodoPage):

    # @given('Load the browser')
    def __init__(self):
        super(TestTodoPage, self).__init__()

    # @when('pass')
    def when_test(self):
        pass

    # @then('Check the title "{React • TodoMVC}" is present')
    def get_title(self):
        title = TodoPage.get_title(self)
        assert title == "React • TodoMVC"

    def add_single_element(self, todo_text='test'):
        TodoPage.add_todos_elements(self, todo_text)
        TodoPage.enter_todo_list(self)
        assert todo_text == TodoPage.find_element_todo_text(self).text

    def add_single_element_count(self, todo_text='test'):
        TodoPage.add_todos_elements(self, todo_text)
        TodoPage.enter_todo_list(self)
        assert '1' == TodoPage.find_element_todos_selected_count(self).text

    def add_single_element_item(self, todo_text='test'):
        TodoPage.add_todos_elements(self, todo_text)
        TodoPage.enter_todo_list(self)
        assert 'item' == TodoPage.find_element_item_or_items(self).text

    def add_single_element_select_count(self, todo_text='test'):
        TodoPage.add_todos_elements(self, todo_text)
        TodoPage.enter_todo_list(self)
        TodoPage.find_element_dropdown(self).click()
        assert '0' == TodoPage.find_element_todos_selected_count(self).text

    def add_single_element_select_active(self, todo_text='test'):
        TodoPage.add_todos_elements(self, todo_text)
        TodoPage.enter_todo_list(self)
        TodoPage.find_element_select_active(self).click()
        assert todo_text == TodoPage.find_element_todo_text(self).text
        assert '1' == TodoPage.find_element_todos_selected_count(self).text

    def add_single_element_select_completed(self, todo_text='test'):
        TodoPage.add_todos_elements(self, todo_text)
        TodoPage.enter_todo_list(self)
        TodoPage.find_element_select_completed(self).click()
        assert False.__eq__(TodoPage.show_completed_when_active_todo_present(self))
        assert '1' == TodoPage.find_element_todos_selected_count(self).text

    def delete_added_single_clear_completed(self, todo_text='test'):
        TodoPage.add_todos_elements(self, todo_text)
        TodoPage.enter_todo_list(self)
        TodoPage.find_element_dropdown(self).click()
        TodoPage.find_element_clear_completed(self).click()
        assert False.__eq__(TodoPage.show_completed_when_active_todo_present(self))

    def add_double_element(self, todo_text='test'):
        TodoPage.add_todos_elements(self, 'test1')
        TodoPage.enter_todo_list(self)
        TodoPage.add_todos_elements(self, 'test2')
        TodoPage.enter_todo_list(self)
        assert todo_text == TodoPage.find_element_todo_text(self).text


# scenario('Test title is \"React • TodoMVC\" of the website')