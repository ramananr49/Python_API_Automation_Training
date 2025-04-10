Feature: API Test with Requests

  Scenario: Validate GitHub API status
    Given the GitHub API is available
    When I request the user info for "octocat"
    Then the response status code should be 200