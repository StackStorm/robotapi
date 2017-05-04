import connexion
from swagger_server.models.body3 import Body3
from swagger_server.models.inline_response200 import InlineResponse200
from swagger_server.common.constants import AX12


def change_elbow(body):
    """
    Set elbow location

    :param body: Location object
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = Body3.from_dict(connexion.request.get_json())

    location = body.location

    AX12.elbow(location)

    return InlineResponse200(location)


def read_elbow():
    """
    Get elbow location


    :rtype: InlineResponse200
    """
    location = AX12.get_elbow()

    return InlineResponse200(location)
