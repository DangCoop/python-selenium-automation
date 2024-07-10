Feature: Target Sign In feature tests

  Scenario: Verify that a logged out user can navigate to Sign In
    Given Open Target main page
    When Click Sign In
    Then From right side navigation menu, click Sign In
    Then Verify Sign In form opened
