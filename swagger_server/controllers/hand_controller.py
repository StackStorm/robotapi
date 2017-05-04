import connexion
from swagger_server.models.body2 import Body2
from swagger_server.models.inline_response200 import InlineResponse200
from swagger_server.common.constants import AX12


def change_hand(body):
    """
    Set hand location

    :param body: Location object
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = Body2.from_dict(connexion.request.get_json())

    location = body.location

    AX12.hand(location)

    return InlineResponse200(location)


def read_hand():
    """
    Get hand location


    :rtype: InlineResponse200
    """
    location = AX12.get_hand()

    return InlineResponse200(location)
