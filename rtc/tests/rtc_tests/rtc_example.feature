Feature: RTC Example
    As a presenter
    I want to show the ability of BDD


Scenario: Show audience a simple shopping cart
    Given I have welcomed the audience
    When I choose the following products:
        | product | price |
        | water   | 10.00 |
        | book    | 15.00 |
    And I calculate the total price
    Then I should see a total of "25.00"
