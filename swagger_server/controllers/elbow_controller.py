import connexion
from swagger_server.models.location import Location
from swagger_server.models.state import State
from swagger_server.common.constants import AX12


def change_elbow(body):
    """
    Set elbow location

    :param body: Location object
    :type body: dict | bytes

    :rtype: Location
    """
    if connexion.request.is_json:
        body = Location.from_dict(connexion.request.get_json())

    location = body.location

    AX12.elbow(location)

    return Location(location)


def change_elbow_torque(body):
    """
    Set elbow torque

    :param body: State object
    :type body: dict | bytes

    :rtype: State
    """
    if connexion.request.is_json:
        body = State.from_dict(connexion.request.get_json())

    state = body.state

    AX12.set_elbow_state(state)

    return State(state)


def read_elbow():
    """
    Get elbow location


    :rtype: Location
    """
    location = AX12.get_elbow()

    return Location(location)


def read_elbow_torque():
    """
    Get elbow torque


    :rtype: State
    """
    return State(True)
