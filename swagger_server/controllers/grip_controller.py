import connexion
from swagger_server.models.body import Body
from swagger_server.models.inline_response200 import InlineResponse200
from swagger_server.common.constants import AX12


def change_grip(body):
    """
    Set grip location

    :param body: Location object
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = Body.from_dict(connexion.request.get_json())

    location = body.location

    AX12.grip(location)

    return InlineResponse200(location)


def read_grip():
    """
    Get grip location


    :rtype: InlineResponse200
    """
    location = AX12.get_grip()

    return InlineResponse200(location)
