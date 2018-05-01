from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .helpers import hash


@api_view(['GET', ])
def participant_local_id(request):
    """
    Core endpoint.  Returns a printable hexadecimal that is unique to supplied parameters.

    `request` should contain two parameters, `study_id` and `study_subject_id`.
    """

    try:
        hash_me = request.GET['study_id'] + request.GET['study_subject_id']
    except KeyError:
        return Response(
            {'Missing paramter':
             'Parameters `study_id` and `study_subject_id` are required.'},
            status=status.HTTP_400_BAD_REQUEST)
    return Response({'miro_id': hash(hash_me)})
