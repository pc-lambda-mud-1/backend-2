# Backend
Backend Django project for our CS build week 1 project

# Instructions 

- Deployed URL: https://lambda-mud-build.herokuapp.com/api/welcome

To run this server on your local:

- Add a .env file to the directory:

ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL="sqlite:///db.sqlite3"
SECRET_KEY={secret key}
DEBUG=True

- Set up pipenv with
 `pipenv --three`
 `pipenv install`
 `pipenv shell`

- Run the development server with `python manage.py runserver`

# Endpoints

## Registration: http://localhost:8000/registration

Accepts: POST

-Example request: `curl -X POST -H "Content-Type: application/json" -d '{"username":"testuser", "password1":"testpassword", "password2":"testpassword"}' localhost:8000/registration`

Returns: `{"key":"b68053489a3f876aa93716ba28ab437633aa8389"}`   

## Login: http://localhost:8000/login

Accepts: POST

Example request: `curl -X POST -H "Content-Type: application/json" -d '{"username":"testuser", "password":"testpassword"}' localhost:8000/login/  `

Returns: `{"key":"b68053489a3f876aa93716ba28ab437633aa8389"}`

##  Welcome: http://localhost:8000/api/welcome

Protected: requires valid token in header

Accepts: GET

Example request: `curl -X GET -H 'Authorization: Token 6b7b9d0f33bd76e75b0a52433f268d3037e42e66' localhost:8000/api/welcome/`

Returns: `{"message": "Welcome to our MUD Game"}`