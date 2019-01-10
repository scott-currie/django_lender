# Book Lender

**Author**: Scott
**Version**: 1.0.0

## Overview
This is a web-based app for keeping track of books available for borrowing.

## Getting Started
<!-- What are the steps that a user must take in order to build this app on their own machine and get it running? -->
1. Create virtual environment: `pipenv shell`
2. Install dependencies: `pipenv install`
3. Create .env file, specifying:
    DB_NAME=postgres
    DB_USER=postgres
    DB_HOST=db
    SECRET_KEY=[copied from settings.py]
    DEBUG=True
    ALLOWED_HOSTS=127.0.0.1 0.0.0.0 localhost
4. Start Docker: `docker-compose up --build`
5. Access the site at http://localhost:8000

## Architecture
* Python >= 3.6
* Django
* Docker
* Docker Compose


## API
<!-- Provide detailed instructions for your applications usage. This should include any methods or endpoints available to the user/client/developer. Each section should be formatted to provide clear syntax for usage, example calls including input data requirements and options, and example responses or return values. -->

## Change Log
01-08-2019 18:00:00 - Basic app functionality up and running
01-09-2019 15:00:00 - Home route added
01-09-2019 18:00:00 - Model and view tests

