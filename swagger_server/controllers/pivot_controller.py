import connexion
from swagger_server.models.location import Location
from swagger_server.models.state import State
from swagger_server.common.constants import AX12


def change_pivot(body):
    """
    Set pivot location

    :param body: Location object
    :type body: dict | bytes

    :rtype: Location
    """
    if connexion.request.is_json:
        body = Location.from_dict(connexion.request.get_json())

    location = body.location

    AX12.pivot(location)

    return Location(location)


def change_pivot_torque(body):
    """
    Set pivot torque

    :param body: State object
    :type body: dict | bytes

    :rtype: State
    """
    if connexion.request.is_json:
        body = State.from_dict(connexion.request.get_json())

    state = body.state

    AX12.set_pivot_state(state)

    return State(state)


def read_pivot():
    """
    Get pivot location


    :rtype: Location
    """
    location = AX12.get_pivot()

    return Location(location)


def read_pivot_torque():
    """
    Get pivot torque


    :rtype: State
    """
    return State(True)
