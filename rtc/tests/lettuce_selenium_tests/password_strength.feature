Feature: Password strength
    In order to create an account
    The system should notify the user when the password supplied
    does not meet the minimum security requirements


Scenario Outline: Test password strength
    Given I go to the register page
    When I fill the password field with "<value>"
    Then I should see the correct password "<strength>"

    Examples:
        | value    | strength |
        | t        | Short    |
        | test     | Weak     |
        | test123  | Good     |
        | test123_ | Strong   |
