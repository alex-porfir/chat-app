# chat-app

This is a simple app that simulates a chat app for customer service. The user can start a chat and he will
automatically be connected with a random customer service employee.

## Installation

* Setup virtual environment
  * Install Python 3.12.1 or newer and Poetry
  * `poetry shell`
  * `poetry install`

If you don't want to use Poetry, just create your virtual environment however you want.

* Run `src/./manage.py migrate` to set up the sqlite3 database. This will also create the Customer Service group required for
the chat

## Setup Users for testing

* Open the app in your browser and create your user. You should create at least two users.
* Run `src/./manage.py add_to_customer_service` to add your desired users to the Customer-Service group. Leave empty if 
you want to make all the users customer service users. 
* IMPORTANT: Make sure, that at least one user does not belong to the Customer Service group, as only this user will be
able to open conversations
* After you have created the accounts you can begin testing by logging in as a Customer Service user in one browser and
as the other user (the one who does not belong to the Customer Service group) in another browser (or incognito tab)
* After the normal user starts a chat by clicking on the button, the customer service user must refresh the page,
in order to be able to join the newly created conversation
* Note: The algorithm connects the user to a random customer service employee that is available for chatting. An 
available customer service user is a user that does not have any open chats. This means that, if you create more
than one customer service user, you have to log in with the right customer service account in order to be able
to talk to the customer. The username of the random customer service employee is displayed in the chat of the 
customer.