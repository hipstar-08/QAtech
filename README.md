# QAtech

There github repo has two testing projects
 - Selenium Todo https://jsonplaceholder.typicode.com/todos/
 - REST API https://jsonplaceholder.typicode.com/posts

## Info
Download the project from github https://github.com/hipstar-08/QAtech
This project was implemented to perform BDD testing

# Prerequisites
### Built With:
Python 3.9

## Installing and Running the project 
1. Download the project
2. pip -r install requirements.txt
3. On the terminal, you can run BDD project
    * Selenium Tests :- behave tests/features/todo_app.feature
    * API Tests     :- behave tests/features/api_testing.feature 

***
    - Selenium
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
***
    - API Feature File
    Feature: API testing
    Background:
      Given Base endpoint
    
      Scenario: "Get requests to posts endpoint"
        Given Set a GET request to "posts" endpoint
        When Send a "GET" request to posts endpoint
        Then Assert Response code "GET" is "200"
        Then Return True for Response "GET" json body matches the posts file in resources
    
      Scenario: "POST requests to posts endpoint"
        Given Set a POST request to "posts" endpoint
        When Send a "POST" request to posts endpoint
        Then Assert Response code "POST" is "201"
        Then Return True for Response "POST" json body matches the posts file in resources



#### Author
Sony James