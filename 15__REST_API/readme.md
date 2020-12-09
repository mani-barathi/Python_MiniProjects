# Rest API
A Basic Movie REST API where user can,
* add movie by posting a movie name (POST request)
* view details about a specific movie based on id (GET request)
* like a movie based on id (POST request)        
* get all movies (GET request)

## modules used
1. **flask_sqlalchemy** to connect and communicate with database.
2. **flask_marshmallow** to convert Video object to JSON (serialize).

#### To run this project on local machine
* clone the repo
* install all modules listed in the requiremets.txt by typing _pip install -r requirements.txt_ in your console
* run app.py
* use test.py to send request to the server
