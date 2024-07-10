Feature: Tests for Cart functionality

  Scenario: Verifies that “Your cart is empty” message is shown on the cart icon
    Given Open Target main page
    When Click on Cart icon
    Then Verify “Your cart is empty” message is shown