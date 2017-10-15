Feature: Reachablity of website


Scenario: Reaching website using browser
   Given i am at browser
    when i enter "http://findmypal.pythonanywhere.com/" url
    Then i should see findmypal signin page