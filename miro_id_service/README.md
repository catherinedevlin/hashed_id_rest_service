# Miro ID Service

## Summary

RESTful web service which supplies a unique
internal participant ID
for each combination of study and participant.

The internal participant ID is determined by the supplied
external participant ID, but cannot be surmised from it.
The external participant ID is never stored.

## Usage

Send a GET request with the study ID and the external
participant ID.

    curl https://miro_id_service.com/?study=ucla-reaction-time-study-1&participan_id=8675309

## Installing

### Using Docker

### Locally

    pipenv install
    pipenv shell
    python manage.py runserver

## Testing

    py.test

