
Feature: List movies
  In order to keep myself up to date about latest movie,
  As a user,
  I want to view the last movie.

  Background: There are 10 registered movies
    Given Exist movies registered
      | name            | release  |
      | The First       | 1970     |
      | The Second      | 1970     |
      | The Third       | 1970     |
      | The Fourth      | 1970     |
      | The Fifth       | 1970     |
      | The Sixth       | 1970     |
      | The Seventh     | 1970     |
      | The Eighth      | 1970     |
      | The Ninth       | 1970     |
      | The Tenth       | 1970     |

  Scenario: List movies
    When I list movies
    Then I´m viewing a list containing
       | name            |
       | The First       |
       | The Second      |
       | The Third       |
       | The Fourth      |
       | The Fifth       |
       | The Sixth       |
       | The Seventh     |
       | The Eighth      |
       | The Ninth       |
       | The Tenth       |
    And The list contains 10 movies
