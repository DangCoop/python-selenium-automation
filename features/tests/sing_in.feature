Feature: Target Sign In feature tests

  Scenario: Verify that a logged out user can navigate to Sign In
    Given Open Target main page
    When Click Sign In
    When From right side navigation menu, click Sign In
    Then Verify Sign In form opened

  Scenario: User want to login with correct credentials
    Given Open target main page
    When Click Sign In
    And From right side navigation menu, click Sign In
    And Enter email "sorenveje@gmailod.com" and password "passcod220045!"
    And Click Sign In With Password
    Then Verify user is logged in

   Scenario: User can open and close Terms and Conditions from sign in page
     Given Open Target main page
     When Click Sign In
     And From right side navigation menu, click Sign In
     And Store original window
     And Click on Target terms and conditions link
     And Switch to the newly opened window
     Then Verify Terms and Conditions page is opened
     And User can close new window
     And User can switch back to original
