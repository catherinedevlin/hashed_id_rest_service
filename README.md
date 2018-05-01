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

### Locally

[Install Python3](http://docs.python-guide.org/en/latest/starting/installation/)

[Install Pipenv](https://docs.pipenv.org/)

At a terminal window, `cd` into the directory you have cloned or copied the code into.  For instance,

    git clone https://github.com/catherinedevlin/hashed-id-rest-service.git
    cd hashed-id-rest-service

The rest of these steps should be performed from that directory.

Create a `.env` file in your project directory.  For development use, it can look like

    DJANGO_SETTINGS_MODULE=miro_id_service.settings.local
    MIRO_ID_SALT=change-this-before-going-to-production-or-else
    DJANGO_SECRET_KEY=change-this-before-production-too

However, for production use, it should look like

    DJANGO_SETTINGS_MODULE=miro_id_service.settings.production
    MIRO_ID_SALT=make-this-unique-and-do-not-lose-it
    DJANGO_SECRET_KEY=make-this-unique-but-you-can-lose-it-if-you-want
    DJANGO_ALLOWED_HOSTS='.miro.com'

*Do not lose this `MIRO_ID_SALT`!*  If it is lost or changed, the previously generated Miro IDs *cannot* be
generated again, and you will need new Miro IDs for each external ID.

Next, run

    pipenv install
    pipenv shell
    python manage.py runserver

## Running the test suite

Using the terminal window, from the directory you have cloned or copied the code into,

    pipenv shell
    py.test

