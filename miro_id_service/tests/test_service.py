import re

from hypothesis import given
from hypothesis.strategies import text
from rest_framework import status
from rest_framework.test import APIClient

client = APIClient()
hex_pattern = re.compile(r'^[a-f\d]+$', re.IGNORECASE)

STUDY_ID = 'ucla-eye-function-study-2017'
STUDY_SUBJECT_ID = 'PA65000'


def test_service_functions():
    '''Verify that service exists and returns a response.'''

    resp = client.get('/', {'study_id': STUDY_ID,
                            'study_subject_id': STUDY_SUBJECT_ID})
    assert resp.status_code == status.HTTP_200_OK

    resp = client.get('/', {'study_id': STUDY_ID,
                            'study_subject_id': STUDY_SUBJECT_ID})
    assert resp.status_code == status.HTTP_200_OK


def test_form_of_result():
    '''Verify that service returns a printable hexadecimal ID'''

    resp = client.get('/', {'study_id': STUDY_ID,
                            'study_subject_id': STUDY_SUBJECT_ID})
    miro_id = resp.data.get('miro_id')
    assert miro_id
    assert len(miro_id) > 7
    assert hex_pattern.search(miro_id)


def test_input_ids_not_in_output_id():
    '''Verify that supplied parameters are not in response ID'''

    resp = client.get('/', {'study_id': STUDY_ID,
                            'study_subject_id': STUDY_SUBJECT_ID})
    miro_id = resp.data.get('miro_id')

    assert STUDY_ID.lower() not in miro_id.lower()
    assert STUDY_SUBJECT_ID.lower() not in miro_id.lower()


def _pieces(original, fragment_length):
    '''Given a string, yield all contiguous fragments

    >>> list(_pieces('dogs cats', 3))
    ['dog', 'ogs', 'gs ', 's c', ' ca', 'cat']
    '''

    for start_pos in range(len(original) - fragment_length):
        yield original[start_pos:start_pos + fragment_length]


def test_input_id_fragments_not_in_output_id():
    '''Verify that no fragment of supplied parameters is in response ID'''

    resp = client.get('/', {'study_id': STUDY_ID,
                            'study_subject_id': STUDY_SUBJECT_ID})
    miro_id = resp.data.get('miro_id')
    lower_miro_id = miro_id.lower()

    for piece in _pieces(STUDY_ID + STUDY_SUBJECT_ID, 3):
        assert piece.lower() not in lower_miro_id


def test_deterministic_result():
    '''Verify that same input generates consistent output'''

    results = set()

    for i in range(10):
        resp = client.get('/', {'study_id': STUDY_ID,
                                'study_subject_id': STUDY_SUBJECT_ID})
        miro_id = resp.data.get('miro_id')
        results.add(miro_id)

    assert len(results) == 1


def test_result_varies_by_inputs():
    '''Verify that differings input generates differing output'''

    results = set()

    for i in range(10):
        resp = client.get('/', {'study_id': STUDY_ID + str(i),
                                'study_subject_id': STUDY_SUBJECT_ID})
        miro_id = resp.data.get('miro_id')
        results.add(miro_id)
    for i in range(10):
        resp = client.get('/', {'study_id': STUDY_ID,
                                'study_subject_id': STUDY_SUBJECT_ID + str(i)})
        miro_id = resp.data.get('miro_id')
        results.add(miro_id)

    assert len(results) == 20


@given(text(), text())
def property_based_test(study_id, study_subject_id):
    '''Uses Hypothesis library to verify that a variety of nasty edge cases do not crash server.

    Hypothesis: https://hypothesis.readthedocs.io/'''

    resp = client.get('/', {'study_id': study_id,
                            'study_subject_id': study_subject_id})
    miro_id = resp.data.get('miro_id')
    assert miro_id
    assert miro_id != study_id + study_subject_id
