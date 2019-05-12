
Feature: View movie details
  In order to view all the details about a certain movie
  As a user,
  I want to be provided the general information about a certain movie (release year,
  genre, actors,...) and the reviews.


  Background: There is one movie and its details
    Given Exists a user “user1” with password “password”
    And Exists a user “user2” with password “password”
    And Exists a movie
      | name      | release  | cast        |
      | Apollo 11 | 2019     | Buzz Aldrin |
    And Exists a review at movie “Apollo 11” by “user2”
      | rating | description |
      | 4      | Quite good  |
    And Exists a movie
      | name       | release      | cast           |
      | Green Book | 2019         | Viggo Mortesen |

  Scenario: View details for movie with one review
    Given I view the details for movie “Apollo 11”
    Then I'm viewing movie details including
      | name           | release  | cast        |
      | Apollo 11      | 2019     | Buzz Aldrin |
    And I'm viewing a movie reviews list containing
      | rating    | description   | user          |
      | 4/5 stars | Quite good    | user2         |
    And The list contains 1 reviews

  Scenario: View details for movie with no reviews
    Given I view the details for movie “Green Book”
    Then I'm viewing movie details including
      | name       | release      | cast           |
      | Green Book | 2019         | Viggo Mortesen |
    And I'm viewing a movie reviews list containing
      | rating          | description   | user     |
    And The list contains 0 reviews
