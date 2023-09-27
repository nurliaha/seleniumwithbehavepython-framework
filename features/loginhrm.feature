Feature: orangeHRM Logo
  Scenario: Login with valid credential
    Given Launch the browser
    Then Open the https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
    When Verify that the logo present
    Then Input valid username "Admin" and password "admin123"
    Then Click login button
    And Login is successful and dashboard is opened
    And browser close


