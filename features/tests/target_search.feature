Feature: Target main page search tests

  Scenario: User can search for a tea
    Given Open Target main page
    When Search for tea
    Then Verify search results shown for tea
    Then Verify correct search results URL opens for tea

Scenario: User can search for a cue
    Given Open Target main page
    When Search for cue
    Then Verify search results shown for cue
    Then Verify correct search results URL opens for cue

Scenario: User can search for a speaker
    Given Open Target main page
    When Search for speaker
    Then Verify search results shown for speaker
    Then Verify correct search results URL opens for speaker

Scenario Outline: User can search for product
    Given Open Target main page
    When Search for <product>
    Then Verify search results shown for <expected_result>
    Then Verify correct search results URL opens for <expected_result>
    Examples:
    |product   |expected_result     |
    |tea       |tea                 |
    |cue       |cue                 |
    |speaker   |speaker             |