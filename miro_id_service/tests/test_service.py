import re

from rest_framework import status
from rest_framework.test import APIClient

client = APIClient()
hex_pattern = re.compile(r'^[a-f\d]+$', re.IGNORECASE)

STUDY_ID = 'ucla-eye-function-study-2017'
STUDY_SUBJECT_ID = 'PA65000'


def test_service_functions():
    '''Verify that service exists and returns a response.'''

    resp = client.post('/', {'study_id': STUDY_ID,
                             'study_subject_id': STUDY_SUBJECT_ID})
    assert resp.status_code == status.HTTP_200_OK


def test_form_of_result():
    '''Verify that service returns a printable hexadecimal ID'''

    resp = client.post('/', {'study_id': STUDY_ID,
                             'study_subject_id': STUDY_SUBJECT_ID})
    miro_id = resp.data.get('miro_id')
    assert miro_id
    assert len(miro_id) > 7
    assert hex_pattern.search(miro_id)
