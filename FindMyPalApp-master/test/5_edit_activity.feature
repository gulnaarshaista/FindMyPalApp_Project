Feature: editing a posted activity

Scenario: Having editing feature to posted activity
   Given i am at Find My Pal Home_page
    when i click on "Created Activities" option on home page
    Then i should see the "Edit" option on every event
	
Scenario: editing my posted activity
   Given i am at Find My Pal Home_page
    when i click on "Created Activities" option on home page 
	And  i click on edit event for one of events
    And  i edit my post and save changes
	Then i should see "Event has been edited successfully" message
	Then i should see the changes in "Created Activities" ,"Joined Activities" and "All Activities"