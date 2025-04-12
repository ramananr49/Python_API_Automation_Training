Feature: Library API Test with Requests

  Scenario: Validate Get Book By Author API status
    Given the Get book by Author API is available
    When I request the user info for Lewis Hamilton
    Then the response status code should be 200 and book details fetched

  Scenario Outline: Validate Get Book By ID API
    Given the Get Book By ID API is Available
    When I request the book <IDs>
    Then the response status code is 200 and desire book details fetched
    Examples:
      |IDs      |
      |RRAY0021 |
      |RRAY0022 |
      |RRAY0023 |

  @focus
  Scenario: Validate Add Book API
    Given the Add Book API is available
    When execute the post request to add the book
    Then the book should added successfully and status code is 200

    Given the Delete Book API is available
    When execute the post request to delete the book
    Then the book should deleted successfully and status code is 200