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




Overview of the Orchestrator Application Error Handling Strategy
The newly developed Orchestrator application performs three primary tasks:
1. Writing data to the database (DB)
2. Publishing messages to the service bus topic
3. Invoking specific endpoints in the Batch Manager
While executing these operations, errors may occur at various stages. This document outlines the potential points of failure during each process and details the strategies in place to handle them effectively.  These three operations are treated as atomic transactions. In the event that any one of them fails, the system must update the corresponding status as “ERROR” in the database. This ensures that the subsequent listener can identify the failed transaction and picks up the process again.  when Control-M triggers the Orchestrator application's “/processfiles” endpoint. In turn, the Orchestrator application calls the Batch Manager's “/listfiles” endpoint. The Batch Manager then queries the Azure Blob Storage to retrieve the container and file names.

Atomic Transactions and Error Handling
If the above workflow fails at any point, the corresponding entry will be marked as "ERROR" in the database. This ensures that the failed task can be retried by another listener.
Even if the file list is successfully retrieved and the record is inserted into the database, but a message fails to be sent, the response will still be marked as "ERROR."
To ensure the successful completion of a job, all three steps must be executed without errors. Any failure in this sequence will result in the job being marked as "ERROR."

Run ID Retrieval Failure Handling
If there is a failure to retrieve the “run_id”, or if the “run_id” is returned as null or any unexpected data, the process will be halted, and the status will be marked as "ERROR." And the parent table will be marked as ERROR respectively.  Status Polling by Control-M
When Control-M polls for the status, any response other than "COMPLETE" will be considered an "ERROR."

Overall Failure Management Approach In the event of a failure, the job will be re-executed by Control-M as a new file, assigned a new “instance_id”. During this the status of the file in inbound_files table is still “READY”. The files with ERROR status need to be removed from (archived) folder.


Failure Management in Message Processing and Acknowledgement
When we send a message to ASB then the message gets picked and start processing the files sequentially, the pod which is processing file restarts. the message should be still available in ASB after the lock time (5 min).The moment it is completed the message is removed. This “lock time” should be set properly based on the time the snaplogic takes to process.
Message acknowledgement occurs only after all files associated with the same “instance_id” have been successfully processed.   If the pod crashed then after the lock time expires, that message will again be available for other instances of the listener listening to that topic subscription to pick up the process where exactly it left off. 

