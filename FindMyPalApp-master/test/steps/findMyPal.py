from behave import *
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import html5lib

''' Reachablity to website feature '''

@given(u'i am at browser')
def step_impl(context):
    context.driver = webdriver.Chrome()   
    pass	

@when(u'i enter "http://findmypal.pythonanywhere.com/" url')
def step_impl(context):
    context.driver.get("http://findmypal.pythonanywhere.com/login?")
    time.sleep(3)
    pass

@then(u'i should see findmypal signin page')
def step_impl(context):
    assert "Find My Pal" in context.driver.title
    context.driver.close()

	
''' signin to website feature  '''	
	
 #user login with valid kent e-mail scenario
  
@given(u'i am at Find My Pal signin page')
def step_impl(context):
    context.driver = webdriver.Chrome()    
    driver = context.driver
    driver.get("http://findmypal.pythonanywhere.com/login?")
    pass

@when(u'i click on "signin with google" option')
def step_impl(context):
    window_before = context.driver.window_handles[0]
    context.driver.find_element_by_id("signin-google").click()
    time.sleep(2)
    window_after = context.driver.window_handles[1]
    context.driver.switch_to_window(window_after)
    #print(context.driver.page_source)
    pass
	
@when(u'i enter valid kent e-mail and password')
def step_impl(context):
    context.elem = context.driver.find_element_by_xpath("//*[@id='identifierId']")
    context.elem.send_keys("abhoomre@kent.edu")
    time.sleep(2)
    context.driver.find_element_by_xpath("//*[@id='identifierNext']/content/span").click()
    time.sleep(2)
    context.elem = context.driver.find_element_by_id("Username")
    context.elem.send_keys("abhoomre")
    context.elem = context.driver.find_element_by_id("Password")
    context.elem.send_keys("Abhilash!0")
    context.driver.find_element_by_id("Button1").click()
    context.driver.switch_to_window(context.driver.window_handles[0])
    time.sleep(5)
	
@then(u'the page should show "My name"')
def step_impl(context):
    assert "Abhilash" in context.driver.page_source
    context.driver.close()
	
	#user signin with non-kent e-mail scenario

@when(u'i enter non-kent e-mail and password')
def step_impl(context):
    context.elem = context.driver.find_element_by_xpath("//*[@id='identifierId']")
    context.elem.send_keys("abhilashreddy396@gmail.com")
    time.sleep(2)
    context.driver.find_element_by_xpath("//*[@id='identifierNext']/content/span").click()
    time.sleep(2)
    context.elem = context.driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input")
    context.elem.send_keys("abhilash396")
    context.driver.find_element_by_xpath("//*[@id='passwordNext']/content/span").click()
    time.sleep(1)
    context.driver.switch_to_window(context.driver.window_handles[0])
    time.sleep(3)

@then(u'the page should display "Please try logging in with Kent Email Address" message')
def step_impl(context):
    display = context.driver.find_element_by_id("login_error")
    assert display.is_displayed()
    context.driver.close()
	
	
''' Profile page feature '''
 
  # navigating to profile page
@given('i am at Find My Pal Home_page')
def step_impl(context):
    context.driver = webdriver.Chrome()    
    driver = context.driver
    driver.get("http://findmypal.pythonanywhere.com/login?")
    time.sleep(2)
    context.driver.execute_script("window.open('https://googlesso.kent.edu/?SAMLRequest=fVLJTsMwEL0j8Q%2BR79kKAmQ1qQoIUYklooEDt4kzSQ2OHTxOC3%2BPm4KAA70%2Bv3nLeKaz904Fa7Qkjc5YGiUsQC1MLXWbscfyKjxjs%2FzwYErQqZ7PB7fSD%2Fg2ILnAT2ri40PGBqu5AZLENXRI3Am%2BnN%2Fe8EmU8N4aZ4RRLFhcZqxSL31Xge4bUUnQlWyxFwqqVdO%2BtJ33BgUSVsiCp%2B9Yk22sBdGAC00OtPNQkp6GyXE4OSuTlB8d8%2BTkmQXFl9O51LsG%2B2JVOxLx67IswuJ%2BWY4Ca1mjvfPsjLXGtAojYbqtfQFEcu3hBhT5eHMitM4HvDCahg7tEu1aCnx8uMnYyrmeeBxvNpvoRyaG%2BBW1i7AeYhDE8nGvfKxmfy10f3D4Nmb5j%2FQ0%2FiWVf%2F3XtsbisjBKio9grpTZXFgE5zs4O%2FgKV8Z24P53S6N0RGQdNiOVD5p6FLKRWLMgzneufw%2FDn8sn&RelayState=https%3A%2F%2Faccounts.google.com%2FCheckCookie%3Fcontinue%3Dhttps%253A%252F%252Faccounts.google.com%252Fsignin%252Foauth%252Fconsent%253Fauthuser%253Dunknown%2526part%253DAJi8hAPOxCtbEAKKEo8tlw9tf3N9nF4iluWElkwLDtNUckYGUbqFvt7SF4qDVV80-TwuUqoYuM6TC9L-QLLJdWALbFL6QUg-fgCz6qS4nYZ5ZrnPYqebW31IZdMYsJUenkcWKLxKwEcO4LVQO-TY96IFeTXxWPOOojxkUS7dLaM84oK5hx0VF1JsMsbtbR8URDOY-np47DNccExnQs9z5ybV9KGBR6kBoDloOxqeBiI1RUqKAPQsbQJXS4N3jr1nYK4H9I_-F0mxet1YftMq8DVxn8SPntj9bt27DDDjMInQNrh_Dgs0ZWZnxcsmOfKVy2sCjdZBHVp3UKZapx4AXNjYPP0myRXwTWy3uoPdn_4inHgxTvLFu3n8v1c4btpwQr3duYWBSX4H_vcnyQXJnrHx1DEQJt_mDeqoptwE8YHSpBM-RDh8XrxNc3nq9QCDqfW5g-TrNsH-%2526as%253D1b92f62780adc120%2523');")
    context.driver.switch_to.window(driver.window_handles[-1])
    time.sleep(2)
    context.elem = context.driver.find_element_by_id("Username")
    context.elem.send_keys("abhoomre")
    context.elem = context.driver.find_element_by_id("Password")
    context.elem.send_keys("Abhilash!0")
    context.driver.find_element_by_id("Button1").click()
    context.driver.close();
    context.driver.switch_to_window(context.driver.window_handles[0])
    context.driver.find_element_by_id("signin-google").click()
    time.sleep(5)
	 
@given(u'signed in with valid kent e-mail')
def step_impl(context):
    context.driver.execute_script("window.open('https://googlesso.kent.edu/?SAMLRequest=fVLJTsMwEL0j8Q%2BR79kKAmQ1qQoIUYklooEDt4kzSQ2OHTxOC3%2BPm4KAA70%2Bv3nLeKaz904Fa7Qkjc5YGiUsQC1MLXWbscfyKjxjs%2FzwYErQqZ7PB7fSD%2Fg2ILnAT2ri40PGBqu5AZLENXRI3Am%2BnN%2Fe8EmU8N4aZ4RRLFhcZqxSL31Xge4bUUnQlWyxFwqqVdO%2BtJ33BgUSVsiCp%2B9Yk22sBdGAC00OtPNQkp6GyXE4OSuTlB8d8%2BTkmQXFl9O51LsG%2B2JVOxLx67IswuJ%2BWY4Ca1mjvfPsjLXGtAojYbqtfQFEcu3hBhT5eHMitM4HvDCahg7tEu1aCnx8uMnYyrmeeBxvNpvoRyaG%2BBW1i7AeYhDE8nGvfKxmfy10f3D4Nmb5j%2FQ0%2FiWVf%2F3XtsbisjBKio9grpTZXFgE5zs4O%2FgKV8Z24P53S6N0RGQdNiOVD5p6FLKRWLMgzneufw%2FDn8sn&RelayState=https%3A%2F%2Faccounts.google.com%2FCheckCookie%3Fcontinue%3Dhttps%253A%252F%252Faccounts.google.com%252Fsignin%252Foauth%252Fconsent%253Fauthuser%253Dunknown%2526part%253DAJi8hAPOxCtbEAKKEo8tlw9tf3N9nF4iluWElkwLDtNUckYGUbqFvt7SF4qDVV80-TwuUqoYuM6TC9L-QLLJdWALbFL6QUg-fgCz6qS4nYZ5ZrnPYqebW31IZdMYsJUenkcWKLxKwEcO4LVQO-TY96IFeTXxWPOOojxkUS7dLaM84oK5hx0VF1JsMsbtbR8URDOY-np47DNccExnQs9z5ybV9KGBR6kBoDloOxqeBiI1RUqKAPQsbQJXS4N3jr1nYK4H9I_-F0mxet1YftMq8DVxn8SPntj9bt27DDDjMInQNrh_Dgs0ZWZnxcsmOfKVy2sCjdZBHVp3UKZapx4AXNjYPP0myRXwTWy3uoPdn_4inHgxTvLFu3n8v1c4btpwQr3duYWBSX4H_vcnyQXJnrHx1DEQJt_mDeqoptwE8YHSpBM-RDh8XrxNc3nq9QCDqfW5g-TrNsH-%2526as%253D1b92f62780adc120%2523');")

@when(u'i click on "profile area" option')
def step_impl(context):
    context.driver.find_element_by_id("profile_picture").click()
    time.sleep(3)
    pass
	   

@then(u'i should see "proile info" page')
def step_impl(context):
    assert "Profile Info" in context.driver.title
    context.driver.close()
	
	# displaying user profile scenario

@then(u'i should see "My personal details" and "interests"')
def step_impl(context):
    first_name  = context.driver.find_element_by_id("firstname").get_attribute('value')
    middle_name = context.driver.find_element_by_id("middlename").get_attribute('value')
    last_name   = context.driver.find_element_by_id("lastname").get_attribute('value')
    nick_name   = context.driver.find_element_by_id("nickname").get_attribute('value')
    graduate_status = context.driver.find_element_by_xpath("//*[@id='profilePic']/div[3]/div[1]/input[2]").get_attribute('checked')
    education_year = context.driver.find_element_by_xpath("//*[@id='profilePic']/div[3]/div[2]/input[5]").get_attribute('checked')
    interested_category1 = context.driver.find_element_by_xpath("//*[@id='profilePic']/div[3]/div[3]/input[1]").get_attribute('checked')
    interested_category2 = context.driver.find_element_by_xpath("//*[@id='profilePic']/div[3]/div[3]/input[2]").get_attribute('checked')
    interested_category3 = context.driver.find_element_by_xpath("//*[@id='profilePic']/div[3]/div[3]/input[3]").get_attribute('checked')
	
    assert first_name == 'Abhilash reddy'
    assert middle_name== ''
    assert last_name  == 'Bhoomreddy'
    assert nick_name  == 'Abhilash'
    assert graduate_status == 'true'
    assert education_year == 'true'	
    assert interested_category1 == 'true'
    assert interested_category2 == 'true'
    assert interested_category3 == 'true'
    time.sleep(3)
    context.driver.close()
	
	
	# updating user profile scenario

@when(u'i update "My presonal details" and "interest"')
def step_impl(context):
             
	 #Changing first_name "Abhilash reddy to Abhilash"
    context.elem = context.driver.find_element_by_id("firstname")
    context.elem.clear()    
    context.elem.send_keys("Abhilash")
	
    #Changing nick_name "Abhilash to Abhi
    context.elem = context.driver.find_element_by_id("nickname")
    context.elem.clear()		
    context.elem.send_keys("Abhi")
	
	#setting gender to "Male"
    context.driver.find_element_by_xpath("//*[@id='gender']/option[2]").click()
	
	
	#adding "pool to interested catogiry""
    if (context.driver.find_element_by_xpath("//*[@id='profilePic']/div[3]/div[3]/input[4]").get_attribute('checked') != 'true'):
        context.driver.find_element_by_xpath("//*[@id='profilePic']/div[3]/div[3]/input[4]").click()

	
@when(u'click on "save changes" button')
def step_impl(context):
   
    context.driver.find_element_by_id("update_profile").click()

@then(u'page should display "Your Profile has been Updated!!!" message')
def step_impl(context):
    display = context.driver.find_element_by_xpath("//*[@id='profilePic']/div[1]")
    print(display.is_displayed())
    assert display.is_displayed()

@then(u'i should see updated "personal details" and "interests"')
def step_impl(context):
    first_name  = context.driver.find_element_by_id("firstname").get_attribute('value')
    nick_name   = context.driver.find_element_by_id("nickname").get_attribute('value')
    gender = context.driver.find_element_by_xpath("//*[@id='gender']/option[2]").get_attribute('value')
    updated_category = context.driver.find_element_by_xpath("//*[@id='profilePic']/div[3]/div[3]/input[4]").get_attribute('checked')
    assert first_name == 'Abhilash'
    assert nick_name == 'Abhi'
    assert gender == 'Male'
    assert updated_category == 'true'
    time.sleep(3)
    context.driver.close()
	
	
	
''' create activity feature '''

  #reachablity to  creating an activity scenario
@when(u'i click on "create a new activity" option on home page')
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@id='activity-container']/div[1]/div/div[2]/p").click()
    context.driver.find_element_by_xpath("//*[@id='activity-container']/div[1]/div/div[2]/ul/li[3]").click()
	
@then(u'i should see "Create a new event"')
def step_impl(context):
    assert "Create a new Event" in context.driver.page_source
    time.sleep(3)
    context.driver.close()
	
   # entering details and posting event scenario
@when(u'i enter Title,Category,Description,Location,Time,Date')
def step_impl(context):
     #Setting "Title to SEM Presentation", "category to library", "Description to SEM Final presentation preparation", 
	 #    "Location to library-206","time to 17:00" and "date to 10-05-2017"
    context.elem = context.driver.find_element_by_id("event-title")
    context.elem.send_keys("SEM Presentation")
    context.driver.find_element_by_xpath("//*[@id='event-category']/option[2]").click()
    context.elem = context.driver.find_element_by_id("event-description")
    context.elem.send_keys("SEM Final Presentation preparation")
    context.elem = context.driver.find_element_by_id("event-location")
    context.elem.send_keys("library-206")
    context.elem = context.driver.find_element_by_id("event-time")
    context.elem.send_keys("1700")
    context.elem = context.driver.find_element_by_id("event-date")
    context.elem.send_keys("10052017")
	
@when(u'i click on "Post Event" button')
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0,50);")
    time.sleep(3)
    postEvent_button = context.driver.find_element_by_xpath("//*[contains(text(),'Post Event')]")
    postEvent_button.click()
    time.sleep(3)
    context.driver.execute_script("window.scrollTo(0,0);")
   
@then(u'i should see "Event has been Posted successfully" message')
def step_impl(context):
    time.sleep(1)
    display = context.driver.find_element_by_id("eventMessage")
    assert display.is_displayed()
    time.sleep(3)
	
@then(u'i should see the post in "Created Activities","Joined Activities and "All Activities"')
def step_impl(context):
  
       #checking in created activities
    context.driver.find_element_by_xpath("//*[@id='activity-container']/div[1]/div/div[2]/p").click()
    context.driver.find_element_by_xpath("//*[@id='activity-container']/div[1]/div/div[2]/ul/li[1]").click()
    time.sleep(5)
    catogiry_name = context.driver.find_element_by_xpath("//*[@id='categoryLabel']")
    title   = context.driver.find_element_by_xpath("//*[@id='newEvent']/li[1]/ul/li[2]")
    description = context.driver.find_element_by_xpath("//*[@id='newEvent']/li[1]/ul/li[3]")
    assert catogiry_name.text == "Library"
    assert title.text == "Title:SEM Presentation"
    assert description.text == "Description:SEM Final Presentation preparation"
	
	   #Checking in Joined Activities
    context.driver.find_element_by_xpath("//*[contains(text(),'Joined Activites')]").click()
    time.sleep(3)
    parent = context.driver.find_elements_by_xpath("//*[contains(text(),'Title:SEM Presentation')]/..") 
    assert len(parent) != 0
	
	   #Checking in all activities
    context.driver.find_element_by_xpath("//*[@id='activity-container']/div[1]/div/div[1]/p").click()
    context.driver.find_element_by_xpath("//*[@id='activity-container']/div[1]/div/div[1]/ul/li[1]").click()
    time.sleep(5)
    parent = context.driver.find_element_by_xpath("//*[contains(text(),'Title:SEM Presentation')]/..")
    items = parent.find_elements_by_tag_name("li")
    catogiry_name = items[0]
    title = items[1]
    description = items[2]
    assert catogiry_name.text == "Library"
    assert title.text == "Title:SEM Presentation"
    assert description.text == "Description:SEM Final Presentation preparation"
    time.sleep(3)
    context.driver.close()
 
	
   # entering empty details and posting event scenario
@when(u'i miss any of Title,Category,Description,Location,Time,Date')
def step_impl(context):
    data = context.table
    for row in data:
        time.sleep(2)
        context.driver.execute_script("window.scrollTo(0,50);")
        time.sleep(3)
        context.driver.find_element_by_xpath("//*[@id='activity-container']/div[2]/div[2]/div/button[2]").click()
        time.sleep(3)
        context.driver.execute_script("window.scrollTo(0,0);")
        title = row['Title']
        description = row['Description']
        location = row['Location']
        given_time = row['Time']
        date = row['Date']
        context.elem = context.driver.find_element_by_id("event-title")
        context.elem.send_keys(title)
        context.driver.find_element_by_xpath("//*[@id='event-category']/option[2]").click()
        context.elem = context.driver.find_element_by_id("event-description")
        context.elem.send_keys(description)
        context.elem = context.driver.find_element_by_id("event-location")
        context.elem.send_keys(location)
        context.elem = context.driver.find_element_by_id("event-time")
        context.elem.send_keys(given_time)
        context.elem = context.driver.find_element_by_id("event-date")
        context.elem.send_keys(date)
        context.execute_steps(u""" when i click on "Post Event" button """)
        context.execute_steps(u""" then it should display "Please fill the form" message """)		
    pass

@then(u'it should display "Please fill the form" message')
def step_impl(context):
    display = context.driver.find_element_by_id("eventMessage")
    assert display.is_displayed()
    time.sleep(3)

''' editing posted activity feature '''

 # Having editing feature to posted activity scenario
@when(u'i click on "Created Activities" option on home page')
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@id='activity-container']/div[1]/div/div[2]/p").click()
    context.driver.find_element_by_xpath("//*[@id='activity-container']/div[1]/div/div[2]/ul/li[1]").click()
	
@then(u'i should see the "Edit" option on every event')
def step_impl(context):
    no_Edit = len(context.driver.find_elements_by_xpath("//*[contains(text(),'Edit Event')]"))
    assert no_Edit != 0
    context.driver.close()
 # editing my posted activity scenario
@when(u'i click on edit event for one of events')
def step_impl(context):
    parent = context.driver.find_element_by_xpath("//*[contains(text(),'Title:SEM Presentation')]/..")
    time.sleep(2)
    parent.find_element_by_xpath("//*[contains(text(),'Edit Event')]").click()
    time.sleep(2)
	
@when(u'i edit my post and save changes')
def step_impl(context):
      #Editing event-description, event-location and time 
    context.elem = context.driver.find_element_by_id("event-description")
    context.elem.clear()
    context.elem.send_keys("Edited-SEM Final Presentation preparation")
    context.elem = context.driver.find_element_by_id("event-location")
    context.elem.clear()
    context.elem.send_keys("Media_pod3")
    context.elem = context.driver.find_element_by_id("event-time")
    context.elem.send_keys("1730")
    time.sleep(2)
    context.driver.execute_script("window.scrollTo(0,50);")
    context.driver.find_element_by_xpath("//*[@id='activity-container']/div[2]/div[2]/div/button[1]").click()
    time.sleep(2)
	
@then(u'i should see "Event has been edited successfully" message')
def step_impl(context):
    display = context.driver.find_element_by_id("eventMessage")
    assert display.is_displayed()
	
@then(u'i should see the changes in "Created Activities" ,"Joined Activities" and "All Activities"')
def step_impl(context):
    
	  #Checking in Created Activities
    context.driver.find_element_by_xpath("//*[@id='activity-container']/div[1]/div/div[2]/ul/li[1]").click()
    time.sleep(2)
    parent = context.driver.find_element_by_xpath("//*[contains(text(),'Title:SEM Presentation')]/..")
    items = parent.find_elements_by_tag_name("li")
    description = items[2]
    location= items[3]
    given_time = items[4]
    assert description.text == "Description:Edited-SEM Final Presentation preparation"
    assert location.text == "Location:Media_pod3"
    assert given_time.text == "Time:17:30"
	 
	   #Checking in Joined Activities
    context.driver.find_element_by_xpath("//*[contains(text(),'Joined Activites')]").click()
    time.sleep(3)
    parent = context.driver.find_element_by_xpath("//*[contains(text(),'Title:SEM Presentation')]/..")
    items = parent.find_elements_by_tag_name("li")
    description = items[2]
    location= items[3]
    given_time = items[4]
    assert description.text == "Description:Edited-SEM Final Presentation preparation"
    assert location.text == "Location:Media_pod3"
    assert given_time.text == "Time:17:30"
    print(description.text)
    print(location.text)
    print(given_time.text)
	
	  #checking in all activities
    context.driver.find_element_by_xpath("//*[@id='activity-container']/div[1]/div/div[1]/p").click()
    context.driver.find_element_by_xpath("//*[@id='activity-container']/div[1]/div/div[1]/ul/li[1]").click()
    time.sleep(5)
    parent = context.driver.find_element_by_xpath("//*[contains(text(),'Title:SEM Presentation')]/..")
    items = parent.find_elements_by_tag_name("li")
    description = items[2]
    location= items[3]
    given_time = items[4]
    assert description.text == "Description:Edited-SEM Final Presentation preparation"
    assert location.text == "Location:Media_pod3"
    assert given_time.text == "Time:17:30"	
    time.sleep(3)
    context.driver.close()
	
 	
'''  Joining and Un joininng to an Activity feature  '''

  #Joining to an activity scenario
@when(u'i click on "All Activities" on home page')
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@id='activity-container']/div[1]/div/div[1]/p").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("//*[@id='activity-container']/div[1]/div/div[1]/ul/li[1]").click()
    time.sleep(5)

@when(u'i click one of the Events')
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0,500);")
    time.sleep(2)
    event = context.driver.find_element_by_xpath("//*[contains(text(),'Title:Bahubali 2')]")
    event.click()
    time.sleep(3)
       
@when(u'click on "Join Activity"')
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0,0);")
    time.sleep(5)
    join_button = context.driver.find_element_by_xpath("//*[contains(text(),'Join Activity')]")
    join_button.click()
    time.sleep(3)
	
@then(u'i should see the added activity in Joined Activities')
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@id='activity-container']/div[1]/div/div[2]/p").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("//*[@id='activity-container']/div[1]/div/div[2]/ul/li[2]").click()
    time.sleep(5)
    parent = context.driver.find_element_by_xpath("//*[contains(text(),'Title:Bahubali 2')]/..")
    items = parent.find_elements_by_tag_name("li")
    catogiry_name = items[0]
    title = items[1]
    description = items[2]
    assert catogiry_name.text == "Movies"
    assert title.text == "Title:Bahubali 2"
    assert description.text == "Description:bahubali on may 10th"
    time.sleep(3)
    context.driver.close()

  #Unjoining from an activity scenario
@when(u'i click on "joined activities" option on home page')
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@id='activity-container']/div[1]/div/div[2]/p").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("//*[@id='activity-container']/div[1]/div/div[2]/ul/li[2]").click()
    time.sleep(5)
    
@when(u'i click on Unjoin Activity for the activity')
def step_impl(context):
    time.sleep(2)
    unjoin_button = context.driver.find_element_by_xpath("//*[contains(text(),'Un Join')]")
    unjoin_button.click()
    time.sleep(3)

@then(u'i should not see the activity in "joined activities"')
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@id='activity-container']/div[1]/div/div[2]/ul/li[2]").click()
    time.sleep(5)
    parent = context.driver.find_elements_by_xpath("//*[contains(text(),'Title:Bahubali 2')]/..") 
    assert len(parent) == 0
    time.sleep(3)
    context.driver.close()
	
'''  deleting a posted activity feature  '''

  # Having deleting feature to posted activity scenario
@then(u'i should see the "delete" option on every event')
def step_impl(context):
    no_delete = len(context.driver.find_elements_by_xpath("//*[contains(text(),'Delete Event')]"))
    #print(no_delete)
    assert no_delete != 0
    time.sleep(3)
    context.driver.close()
  
  # Deleting my posted activity scenario
@when(u'i click on "delete event" option for an event')
def step_impl(context):
    parent = context.driver.find_element_by_xpath("//*[contains(text(),'Title:SEM Presentation')]/..")
    parent.find_element_by_xpath("//*[contains(text(),'Delete Event')]").click()
    time.sleep(2)
    alert = context.driver.switch_to_alert()
    alert.accept()
@then(u'i should not see the activity in in "Created Activities","Joined Activities" and "All Activities"')
def step_impl(context):   
       #checking in created activities
    context.driver.find_element_by_xpath("//*[@id='activity-container']/div[1]/div/div[2]/ul/li[1]").click()
    time.sleep(5)
    parent = context.driver.find_elements_by_xpath("//*[contains(text(),'Title:SEM Presentation')]/..") 
    assert len(parent) == 0
	
      #Checking in Joined Activities
    context.driver.find_element_by_xpath("//*[contains(text(),'Joined Activites')]").click()
    time.sleep(3)
    parent = context.driver.find_elements_by_xpath("//*[contains(text(),'Title:SEM Presentation')]/..") 
    assert len(parent) == 0
	
      #Checking in all activities
    context.driver.find_element_by_xpath("//*[@id='activity-container']/div[1]/div/div[1]/p").click()
    context.driver.find_element_by_xpath("//*[@id='activity-container']/div[1]/div/div[1]/ul/li[1]").click()
    time.sleep(5)
    parent = context.driver.find_elements_by_xpath("//*[contains(text(),'Title:SEM Presentation')]/..")
    assert len(parent) == 0
    time.sleep(3)
    context.driver.close()

