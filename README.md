# Backend
Backend Django app

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