Feature: Search
  Background:
    Given Open the link orange hrm
    Then input the username "Admin" and password "admin123"
    And Click login button
    And Login is successful and dashboard is opened

  Scenario: : I can searching menu
    Then input menu "time"
    And menu time is displayed
#    Examples:
#
#    | menu      |
#    | time      |
#    | my info   |
#    | leave     |

#  Scenario: I can searching menu time and displayed the board
#    When Click field search
#    And input menu "time"
#    And menu "time" is displayed
#    And click the menu
#    And board time sucessful opened
