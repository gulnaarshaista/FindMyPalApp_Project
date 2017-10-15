Feature: deleting a posted activity
	
Scenario: Having deleting feature to posted activity
   Given i am at Find My Pal Home_page
    when i click on "Created Activities" option on home page
    Then i should see the "delete" option on every event
	
Scenario: deleting my posted activity
   Given i am at Find My Pal Home_page
    when i click on "Created Activities" option on home page
	And  i click on "delete event" option for an event
	Then i should not see the activity in in "Created Activities","Joined Activities" and "All Activities"