Feature: Validation of Pet Store API's

  Scenario: Validate Create User API
    Given the create user api details are available
    When I execute the create user api with valid data
    Then The API call should be successful and user is created

  Scenario: Validate Get User by Username API
    Given the get user by username api details are available
    When I execute the get user api with valid data
    Then The API call should be successful and user is fetched

  Scenario: Validate Update User API
    Given the Update api details are available
    When I execute the update user api with valid data
    Then The API call should be successful and user is updated

  Scenario: Validate Delete User API
    Given the delete api details are available
    When I execute the delete user api with valid data
    Then The API call should be successful and user is deleted