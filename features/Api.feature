Feature: Api Feature

  @testapi @test_get
  Scenario: GET API Testing
    Given I am testing JSONPLACEHOLDER
    When I make a GET Request to get_posts
    Then I should see response code 200

  @testapi @test_getparam
  Scenario: GET API Testing
    Given I am testing JSONPLACEHOLDER
    When I make a GET Request to get_post_by_id
    Then I should see response code 200
    Then I should see response body has $.userId value 1 of datatype int
    Then I should see response body has $.id value 1 of datatype int

  @testapi @test_post
  Scenario: POST API Testing
    Given I am testing JSONPLACEHOLDER
    When I make a POST Request to post_post
    Then I should see response code 201
    Then I should see response body has $.userId value 2 of datatype int

  @testapi @test_post_replace
  Scenario: POST API Testing
    Given I am testing JSONPLACEHOLDER
    When I make a POST Request to post_post
    Then I replaced value of $.userId with 1 of datatype int
    Then I should see response code 201
    Then I should see response body has $.userId value 2 of datatype int

  Scenario: GET API Testing
    Given I am testing SOMEOTHERSITE
    When I make a GET Request to get_posts
    Then I should see response code 200
    Then I should see response body postResponseBody