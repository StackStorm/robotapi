import connexion
from swagger_server.models.body1 import Body1
from swagger_server.models.inline_response200 import InlineResponse200
from swagger_server.common.constants import AX12


def change_wrist(body):
    """
    Set wrist location

    :param body: Location object
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = Body1.from_dict(connexion.request.get_json())

    location = body.location

    AX12.wrist(location)

    return InlineResponse200(location)


def read_wrist():
    """
    Get wrist location


    :rtype: InlineResponse200
    """
    location = AX12.get_wrist()

    return InlineResponse200(location)
