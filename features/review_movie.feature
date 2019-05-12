
Feature: Review movie
  In order to share my opinion about a movie,
  As a user,
  I want to register, modify or delete my opinion on a certain movie by giving a rating and an optional comment.

  Background: There is a registered user and movie
    Given Exists a user "user1" with password "password"
    And Exists a user "user2" with password "password"
    And Exists a movie
      | name            | release    | cast          |
      | Interstellar    | 2014       | Anne Hathaway |

  Scenario: Register review with rating and comment
    Given I login as user "user1" with password "password"
    When I register a review at movie "Interstellar"
      | rating          | description   |
      | 4               | Quite good    |
    Then I'm viewing movie details including
      | name            | release    | cast          |
      | Interstellar    | 2014       | Anne Hathaway |
    And I'm viewing a movie reviews list containing
      | rating          | description   | user          |
      | 4/5 stars       | Quite good    | user1         |
    And The list contains 1 reviews

  Scenario: Try to register review but not logged in
    Given I'm not logged in
    When I view the movie "Interstellar" details
    Then There is no "review" link available

  Scenario: User new review on same movie replaces previous review
    Given Exists a review at movie "Interstellar" by "user1"
      | rating          | description   |
      | 4               | Quite good    |
    And I login as user "user1" with password "password"
    When I register a review at movie "Interstellar"
      | rating          | description    |
      | 2               | Not so happy   |
    Then I'm viewing movie details including
      | name            | release    | cast          |
      | Interstellar    | 2014       | Anne Hathaway |
    And I'm viewing a movie reviews list containing
      | rating          | description   | user        |
      | 2/5 stars       | Not so happy  | user1       |
    And The list contains 1 reviews

  Scenario: Edit owned review
    Given I login as user "user1" with password "password"
    And Exists a review at movie "Interstellar" by "user1"
      | rating          | description   |
      | 4               | Quite good    |
    When I view the movie "Interstellar" details
    And I edit the current review as "user1" for "Interstellar"
      | rating          | description       |
      | 1               | Changed my mind   |
    Then I'm viewing movie details including
      | name            | release    | cast          |
      | Interstellar    | 2014       | Anne Hathaway |
    And I'm viewing a movie reviews list containing
      | rating          | description       | user    |
      | 1/5 stars       | Changed my mind   | user1   |
    And The list contains 1 reviews

  Scenario: Try to edit review but not logged in
    Given I'm not logged in
    When I view the movie "Interstellar" details
    Then There is no "edit" link available

  Scenario: Try to edit review but not the owner
    Given I login as user "user2" with password "password"
    When I view the movie "Interstellar" details
    Then There is no "edit" link available
