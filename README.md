# Hashed ID REST Service

## Summary

RESTful web service which supplies a unique
internal participant ID (Miro ID)
for each combination of study ID and study subject ID.

The internal participant ID is determined by the supplied information,
but the supplied parameters cannot be determined from the Miro ID.

The external participant ID is never stored.

## Usage

Send a GET request with the study ID and the external
participant ID.

    curl "http://localhost:8000/?study_id=ucla-reaction-time-study-2016&study_subject_id=skwolek321"

Response (actual response depends on `MIRO_ID_SALT` environment variable):

    {"miro_id":"059292645d357d7b299a044a7557e598"}%

## Installing

### Using Docker

### Locally

[Install Python3](http://docs.python-guide.org/en/latest/starting/installation/)

[Install Pipenv](https://docs.pipenv.org/)

At a terminal window, `cd` into the directory you have cloned or copied the code into.  For instance,

    git clone https://github.com/catherinedevlin/hashed-id-rest-service.git
    cd hashed-id-rest-service

Create a `.env` file in your project directory containing a unique `MIRO_ID_SALT` environment variable:

    MIRO_ID_SALT="Do not use this! Make up your own string!"

*Do not lose this variable!*  If it is lost or changed, the previously generated Miro IDs *cannot* be
generated again, and you will need new Miro IDs for each external ID.

Install Python and Pipenv on your machine.  [Pipenv installation instructions]()

Next, run

    pipenv install
    pipenv shell
    cd miro_id_service
    python manage.py runserver

## Running the test suite

Using the terminal window, from the directory you have cloned or copied the code into,

    pipenv shell
    cd miro_id_service
    py.test

