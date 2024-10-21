# FindMyPalApp
Application and Test source code for FindMyPal web application as a part of Software Engineering Methodologies class project.

Features Completed till Now:
1. User Login
2. User Profile view and update
3. Activity Creation
4. Activities and Categories Listing
5. CRUD operations on Activities
6. User can Join Activity
7. Showing the people who registered for Activity

Test Case 1: Verify Successful Execution of Atomic Transactions
Description: Ensure that all three atomic operations (writing to the DB, publishing messages, invoking Batch Manager endpoint) are executed successfully.
Preconditions: The orchestrator application and all dependent services are operational.
Steps:

Trigger the orchestrator application via Control-M.
Verify that the data is written to the database.
Confirm that the message is published to the service bus topic.
Check that the Batch Manager endpoint is invoked successfully.
Expected Result: All operations complete without errors, and no entries are marked as "ERROR" in the database.
