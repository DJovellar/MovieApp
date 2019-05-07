Feature: List movies
  In order to keep myself up to date about latest movie,
  As a user,
  I want to view the last movie.

  Background: There are 10 registered movies
    Given Exists a user "user" with password "password"
    And Exists movies registered 
      | name            | date        |
      | The First       | 1970-01-01  |
      | The Second      | 1970-01-02  |
      | The Third       | 1970-01-03  |
      | The Fourth      | 1970-01-04  |
      | The Fifth       | 1970-01-05  |
      | The Sixth       | 1970-01-05  |
      | The Seventh     | 1970-01-05  |
      | The Eighth       | 1970-01-05  |
      | The Ninth       | 1970-01-05  |
      | The Tenth       | 1970-01-05  |

  
  Scenario: List movies
    When I list the last movies
    Then I´m viewing a list containing
       | name            |
       | The Tenth            |
       | The Ninth            |
       | The Eighth            |
       | The Seventh      |
       | The Sixth            |
       | The Fifth       |
       | The Fourth      |
       | The Third       |
       | The Second      |
       | The First       |
    And The list contains 10 movies


