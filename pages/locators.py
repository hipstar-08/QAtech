from selenium.webdriver.common.by import By


class ToDoPageLocators(object):
    CSS = By.CSS_SELECTOR
    XPATH = By.XPATH
    SEARCH_BAR = 'input.new-todo'
    SELECT_ALL_DROPDOWN ='.main label'

    CHECKBOX_LIST = '.todo-list > li'

    CHECKBOX_SINGLE_ELEMENT = '.toggle'

    CHECKBOX = '.todo-list > li:nth-child(1) > div:nth-child(1) > input:nth-child(1)'
    # .view > label: nth - child(2)
    TODO='.todo-list > li:nth-child(1) > div:nth-child(1) > label:nth-child(2)'
    TODO_RADIO ='.todo-list > li:nth-child(1) > div:nth-child(1) > input:nth-child(1)'

    FIRST_TODO = '.todo-list > li:nth-child(1) > div:nth-child(1) > label:nth-child(2)'
    SECOND_TODO = '.todo-list > li:nth-child(2) > div:nth-child(1) > label:nth-child(2)'

    CHECKBOX_ELEMENT_1 = '.todo-list > li:nth-child('
    CHECKBOX_ELEMENT_2 = ') > div:nth-child(1) > input:nth-child(1)'

    NO_OF_TODOS_SELECTED = '.todo-count > strong:nth-child(1)'
    ITEM_S = '.todo-count > span:nth-child(3)'

    SELECT_ALL = '.filters > li:nth-child(1) > a:nth-child(1)'
    SELECT_ACTIVE = '.filters > li:nth-child(3) > a:nth-child(1)'
    SELECT_COMPLETED = '.filters > li:nth-child(5) > a:nth-child(1)'
    SELECT_COMPLETED_ACTIVE_TODOS = '.todo-list'
    CLEAR_COMPLETED = "//button[@class='clear-completed']"
