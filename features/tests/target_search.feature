Feature: Target main page search tests
  # Enter feature description here

  Scenario: User can search for a product o target
    Given Open Target main page
    When Search for product
    Then Verify search worked

  Scenario: Verifies that “Your cart is empty” message is shown on the cart icon
    Given Open Target main page
    When Click on Cart icon
    Then Verify “Your cart is empty” message is shown

  Scenario: Verify that a logged out user can navigate to Sign In
    Given Open Target main page
    When Click Sign In
    Then From right side navigation menu, click Sign In
    Then Verify Sign In form opened

