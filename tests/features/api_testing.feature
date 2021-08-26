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
