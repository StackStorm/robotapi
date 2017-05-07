import connexion
from swagger_server.models.location import Location
from swagger_server.models.state import State
from swagger_server.common.constants import AX12


def change_hand(body):
    """
    Set hand location

    :param body: Location object
    :type body: dict | bytes

    :rtype: Location
    """
    if connexion.request.is_json:
        body = Location.from_dict(connexion.request.get_json())

    location = body.location

    AX12.hand(location)

    return Location(location)


def change_hand_torque(body):
    """
    Set hand torque

    :param body: State object
    :type body: dict | bytes

    :rtype: State
    """
    if connexion.request.is_json:
        body = State.from_dict(connexion.request.get_json())

    state = body.state

    AX12.set_hand_state(state)

    return State(state)


def read_hand():
    """
    Get hand location


    :rtype: Location
    """
    location = AX12.get_hand()

    return Location(location)


def read_hand_torque():
    """
    Get hand torque


    :rtype: State
    """
    return State(True)
