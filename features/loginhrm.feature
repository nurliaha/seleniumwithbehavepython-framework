Feature: Login
  Background:
    Given Launch the browser
    Then Open the https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
    When Verify that the logo present

  @valid_login
  Scenario: Login with valid credential
    Then Provide the username "Admin" and password "admin123"
    And Click login button
    And Login is successful and dashboard is opened
    And browser close

    Scenario Outline: Login with invalid credential'
    And Provide the username "<username>" and password "<password>"
    And Click login button
    Then Login is failed with invalid credential
    And browser close
    Examples:
      | username  | password |
      | abcd      | 1234     |
      | qwerty    | @13dw    |

  Scenario: Login with empty username
    And Provide the passsword "admin123"
    And Click login button
    Then Login is failed and empty username error is displayed
    And browser close

  Scenario: Login with empty password
    And Provide the username "Admin"
    And Click login button
    Then Login is failed and empty password error is displayed
    And browser close




