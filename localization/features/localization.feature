Feature: TV Schedules is available after user is localized to a station

Scenario:
	Given I am on the Localization page
	When I enter <zipcode>
	And I select <station>
	Then I am able to see that station's TV schedule
	
	Examples:
		|zipcode|station  |
		|21212|MPT        |
		|21212|WETA     |
		|60602|WTTW11 |
		|60602|WYCC    |