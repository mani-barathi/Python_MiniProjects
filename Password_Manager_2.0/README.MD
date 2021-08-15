# Password Manager
* This is a simple implementation of a Password Manager, where the user will have a master Password to login. After login they can add, view, update, delete password. All the password are encrypted before they inserted into database, making it a little bit secure.

* The Master Password and key which is used for encryption and decryption is stored in the environment variables. (avoiding hardcoding sensitive information directly inside the program)

* Database model and Password Manager class is kept separately in individual files, and are  imported in app.py file.
* Database used - MySQL

Modules used:
1. cryptography - for encryption and decryption
1. pyperclip    - to directly copy the password to the clipboard
1. os           - to store and retrieve environment variables
1. sqlalchemy   - to query the database (ORM - object relational mapper)
1. getpass      - to hide the password which is typed by the user

all the requirements are listed in requirements.txt
