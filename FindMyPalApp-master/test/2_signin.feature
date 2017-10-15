Feature: signin to website


Scenario: user signin with valid kent e-mail
   Given i am at Find My Pal signin page
    when i click on "signin with google" option 
     And i enter valid kent e-mail and password 	
    Then the page should show "My name"


Scenario: user signin with non-kent e-mail
   Given i am at Find my Pal signin page
    when i click on "signin with google" option
    And i enter non-kent e-mail and password
	Then the page should display "Please try logging in with Kent Email Address" message


	
   
	   
	 
