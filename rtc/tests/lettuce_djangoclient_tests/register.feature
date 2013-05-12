Feature: Register
    In order to get access to app 
    A user should be able to register


Scenario: User is able to register with valid data
    Given I go to the register page
    When I fill register form with:
        | username | email       | password1 | password2 |
        | rtc      | rtc@rtc.com | secret    | secret    |
    And I submit the data
    Then I should see "You are now registered. Activation email sent."
    And I should receive an email at "rtc@rtc.com" with the subject "Account activation on example.com"
    And I activate the account
    Then I should see "Your account is now activated."


Scenario Outline: Users are able to login
    Given following users with "<username>" and "<password>" exist
    When I go to the login page
    And I login as "<username>" with "<password>"
    Then I should see "<message>"

    Examples:
        | username | password | message                               |
        | foo      | bar      | Welcome, foo. Thanks for logging in.  |
        | rtc      | secret   | Welcome, rtc. Thanks for logging in.  |
        | danu     | test123  | Welcome, danu. Thanks for logging in. |
