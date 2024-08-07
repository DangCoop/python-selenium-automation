Feature: Tests for Cart functionality

  Scenario: Verifies that “Your cart is empty” message is shown on the cart icon
    Given Open Target main page
    When Click on Cart icon
    Then Verify “Your cart is empty” message is shown

   Scenario: Verifies that item can be added to the cart
      Given Open Target main page
      When Search for cue
      And Select the first product from the search results
      And Add the product to the cart
      Then Verify that the cue is in the cart