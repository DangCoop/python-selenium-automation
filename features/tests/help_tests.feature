Feature: Tests for Help pages

  Scenario: User can select Help Topic Promotions & Coupons
    Given Open Help page for Returns
    Then Verify help Returns page opened
    When Select Help topic Promotions & Coupons
    Then Verify help Current promotions page opened


Scenario: User can select Help Topic Partner Programs
    Given Open Help page for Returns
    Then Verify help Returns page opened
    When Select Help topic Partner Programs
    Then Verify help Ulta Beauty at Target page opened