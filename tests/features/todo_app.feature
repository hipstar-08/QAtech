Feature: To Do App testing with smoke and regression
  Background:
    Given Load the browser

  Scenario: "Check the title of the website"
    Then Title is "React • TodoMVC"
    Then Close the browser

  Scenario: "Add a single item to ToDo list and assert the Todo element is present"
    When Todo item "test" is added
    Then Assert todo item "test" is present
    Then Close the browser


  Scenario: "Add a single item to ToDo list and check the count of the added Todo element"
    When Todo item "test" is added
    Then Assert single item todo count "1" is present
    Then Close the browser

  Scenario: "Add a single item to ToDo list and check the presence of item word in sentence"
    When Todo item "test" is added
    Then Assert item/items "item" is present
    Then Close the browser

  Scenario: "Add a single item to list and click the selectAll todos dropdown"
    When Todo item "test" is added
    When Click the select All dropdown
    Then Assert items "0" is present after clicking selectAll dropdown
    Then Close the browser

  Scenario: "Add a single item to list and click the Active button"
    When Todo item "test" is added
    When Click the Active todos button
    Then Assert todo item "test" is present
    Then Assert single item todo count "1" is present
    Then Close the browser

  Scenario: "Add a single item to list and click the Completed Button"
    When Todo item "test" is added
    When Click the Completed todos button
    Then Assert todo item is not present
    Then Assert single item todo count "1" is present
    Then Close the browser

  Scenario: "Add a single item to list, complete it and delete it"
    When Todo item "test" is added
    When Click the select All dropdown
    When Delete the todo item from list
    Then Assert todo item is not present
    Then Close the browser