
Feature: Users
  # This feature is to test the create, list, update and delete users

  Scenario: Create user
    When the user name "alberto" is defined in the name parameter
    And the user job "qa" is defined in the job parameter
    And the post request is sent
    Then the response code has been 201
    And the response contains the submitted name "alberto"
    And the response contains the submitted job "qa"
    And the response must contain the id field
    And the response contains a createAt field

  Scenario: List users
    When the page 2 number is established in the parameter of the request
    And the request to list all users is sent
    Then the response code has been 200
    And the response contains the submitted page 2
    And the response contains the user number per pages 6
    And the response contains the total users 12
    And the response contains the total page 2
    And the response contains a data parameter with the total user 6
    And the response contains a support parameter
    And the support parameter contains the url https://reqres.in/#support-heading field
    And the support parameter contains the text To keep ReqRes free, contributions towards server costs are appreciated! field
#
  Scenario: List an user
    When the user id 2 is defined as a parameter
    And the get request is sent
    Then the response code has been 200
    And the response must contain the id 2 sent
    And the data parameter contains the email janet.weaver@reqres.in parameter
    And the data parameter contains the first_name Janet parameter
    And the data parameter contains the last_name Weaver parameter
    And the data parameter contains the avatar https://reqres.in/img/faces/2-image.jpg parameter
    And the response contains a support parameter
    And the support parameter contains the url https://reqres.in/#support-heading field
    And the support parameter contains the text To keep ReqRes free, contributions towards server costs are appreciated! field

  Scenario: Update an user
    When the user id 2 is defined as a parameter
    And the user name "alberto" is defined in the name parameter
    And the user job "qa" is defined in the job parameter
    And the put request is sent
    Then the response code has been 200
    And the response contains the submitted name "alberto"
    And the response contains the submitted job "qa"
    And the response contains a updateAt field

  Scenario: Delete an user
    When the user id 2 is defined as a parameter
    And the delete request is sent
    Then the response code has been 204