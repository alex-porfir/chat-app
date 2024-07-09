# chat-app

This is a simple app that simulates a chat app for customer service. The user can open a start a chat, and he will
automatically be connected with a random customer service employee.

## Installation

* Setup virtual environment
  * Install Python 3.12.1 or newer and Poetry
  * `poetry shell`
  * `poetry install`

If you don't want to use Poetry, just create your virtual environment however you want
* `src/./manage.py migrate` to setup the sqlite3 database. This will also create the Customer Service group required for
the chat

## Setup Users for testing

* Open the app in your browser and create your user
* Run `src/./manage.py add_to_customer_service` to add your desired users to the Customer-Service group