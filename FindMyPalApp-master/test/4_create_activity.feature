Feature: create activity 


Scenario: reachablity to  creating an activity
   Given i am at Find My Pal Home_page
    when i click on "create a new activity" option on home page 
    Then i should see "Create a new event"
	
Scenario: entering details and posting event  
   Given i am at Find My Pal Home_page
    when i click on "create a new activity" option on home page 
	And i enter Title,Category,Description,Location,Time,Date
	And i click on "Post Event" button
    Then i should see "Event has been Posted successfully" message
    And i should see the post in "Created Activities","Joined Activities and "All Activities"
	
Scenario: entering empty details and posting event  
   Given i am at Find My Pal Home_page
    when i click on "create a new activity" option on home page 
    And i miss any of Title,Category,Description,Location,Time,Date
     |   Title         |      Description                 |  Location | Time | Date     |
     |                 |SEM Final Presentation preparation|library-206|1700  | 10052017 |
     | SEM Presentation|                                  |library-206|1700  | 10052017 |
     | SEM Presentation|SEM Final Presentation preparation|           |1700  | 10052017 |
     | SEM Presentation|SEM Final Presentation preparation|library-206|      | 10052017 |
     | SEM Presentation|SEM Final Presentation preparation|library-206|1700  |          |
    And i click on "Post Event" button
    Then it should display "Please fill the form" message

