from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def participant_local_id(request):
    """
    Core endpoint.  Returns a printable hexadecimal that is unique to supplied parameters.

    `request` should contain two parameters, `study_id` and `study_participant_id`.
    """

    return Response({})
