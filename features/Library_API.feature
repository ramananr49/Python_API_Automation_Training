Feature: Library API Test with Requests

  Scenario: Validate Get Book By ID API status
    Given the Get book by Author API is available
    When I request the user info for Lewis Hamilton
    Then the response status code should be 200 and book details fetched