
from rest_framework.test import APIClient
from rest_framework import status

client = APIClient()

def test_service_functions():
    '''Verify that service exists and returns a response.'''

    STUDY_ID = 'ucla-eye-function-study-2017'
    STUDY_SUBJECT_ID = 'PA65000'
    resp = client.post('/', {'study_id': STUDY_ID, 'study_subject_id': STUDY_SUBJECT_ID})
    assert resp.status_code == status.HTTP_200_OK


