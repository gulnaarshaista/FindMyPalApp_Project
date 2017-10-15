Feature: join and unjoin to activity

Scenario: joining to an activity
   Given i am at Find My Pal Home_page
    when i click on "All Activities" on home page
    And  i click one of the Events
    And click on "Join Activity"
    Then i should see the added activity in Joined Activities 
	
Scenario: unjoin from an activity
   Given i am at Find My Pal Home_page
    when i click on "joined activities" option on home page 
	And  i click one of the Events
	And  i click on Unjoin Activity for the activity
    Then i should not see the activity in "joined activities"
