import connexion
from swagger_server.models.body5 import Body5
from swagger_server.models.inline_response200 import InlineResponse200
from swagger_server.common.constants import AX12


def change_pivot(body):
    """
    Set pivot location

    :param body: Location object
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = Body5.from_dict(connexion.request.get_json())

    location = body.location

    AX12.pivot(location)

    return InlineResponse200(location)


def read_pivot():
    """
    Get pivot location


    :rtype: InlineResponse200
    """
    location = AX12.get_pivot()

    return InlineResponse200(location)
