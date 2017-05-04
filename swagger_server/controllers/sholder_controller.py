import connexion
from swagger_server.models.body4 import Body4
from swagger_server.models.inline_response200 import InlineResponse200
from swagger_server.common.constants import AX12


def change_sholder(body):
    """
    Set sholder location

    :param body: Location object
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = Body4.from_dict(connexion.request.get_json())

    location = body.location

    AX12.sholder(location)

    return InlineResponse200(location)


def read_sholder():
    """
    Get sholder location


    :rtype: InlineResponse200
    """
    location = AX12.get_sholder()

    return InlineResponse200(location)
