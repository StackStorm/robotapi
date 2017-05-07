import connexion
from swagger_server.models.location import Location
from swagger_server.models.state import State
from swagger_server.common.constants import AX12


def change_grip(body):
    """
    Set grip location

    :param body: Location object
    :type body: dict | bytes

    :rtype: Location
    """
    if connexion.request.is_json:
        body = Location.from_dict(connexion.request.get_json())

    location = body.location

    AX12.grip(location)

    return Location(location)


def change_grip_torque(body):
    """
    Set grip torque

    :param body: State object
    :type body: dict | bytes

    :rtype: State
    """
    if connexion.request.is_json:
        body = State.from_dict(connexion.request.get_json())

    state = body.state

    AX12.set_grip_state(state)

    return State(state)


def read_grip():
    """
    Get grip location


    :rtype: Location
    """
    location = AX12.get_grip()

    return Location(location)


def read_grip_torque():
    """
    Get grip torque


    :rtype: State
    """
    return State(True)
