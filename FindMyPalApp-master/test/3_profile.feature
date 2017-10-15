Feature: Profile page 

Scenario: navigating to profile page
   Given i am at Find My Pal Home_page
    when i click on "profile area" option 
    Then i should see "proile info" page
	
Scenario: displaying user details at profile page
   Given i am at Find My Pal Home_page
    when i click on "profile area" option 
    Then  i should see "My personal details" and "interests"  	
	
Scenario: updating profile 
   Given i am at Find My Pal Home_page
    when i click on "profile area" option 
    And i update "My presonal details" and "interest"
    And click on "save changes" button
    Then  page should display "Your Profile has been Updated!!!" message
    And i should see updated "personal details" and "interests"
 
   