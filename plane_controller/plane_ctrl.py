
__corrective_actions = ["ASCEND", "MAINTAIN ALTITUDE", "DESCEND"]

"""
The set of planes that the ADS-B send in.
"""
__nearby_planes_list = {}


def plane_controller_driver(list_in):
    """
    This thread runs in all of the computations for detecting collisions and generates relevant alerts.

    :param list_in:
    :return:
    """
    pass


def input_data(data_in):
    """
    Takes the data from the plane_controller_driver and sends that information to data_verification

    :param data_in:
    :return:
    """
    pass

def convert_to_cartesian_meters(list_in):
    """
    Converts the list of data from latitude, longitude, and elevation to cartesian coordinates.

    :param list_in: the initial list of data in elevation, latitude, and longitude.
    :return: the same list converted
    """
    pass

def find_highest_priority_s(collsion_list):
    """
    Finds the plane or planes, when applicable, with the highest priority and returns them as list to the caller.

    :param collsion_list: the list of the potential collisions
    :return: high_priority_list: the the collisions with the highest priority
    """
    pass

def data_verify(list):
    pass


def update_plane_list(plane):
    """
    Adds or updates the plane to the nearby_plane_list

    :param plane:
    :return:
    """

    pass

def dispatch_collision_alerts(alert_type):
    """

    :return:
    """
    # rel_x = PA[loc_x] - new_plane[loc_x]
    # rel_y = PA[loc_y] - new_plane[loc_y]
    # rel_z = PA[loc_z] - new_plane[loc_z]



def get_corrective_action(*planes):
    """
    Calculates the corrective action of the primary aircraft, will ascend or descend or maintain elevation based
    upon the GPS location of the PA relative to other Aircraft.

    :param planes: planes
    :return: ASCEND, MAINTAIN ALTITUDE, DESCEND
    """
    pass

#    constructor can go here. each piece can be accessed using   data_in[x]
#    plane.__init__(data_in[0], data_in[1], data_in[2], data_in[3], data_in[4], data_in[5], data_in[6],)

# function to take in a new transponder code for itself from the user keypad
def update_transponder_code(new_code):
    """
    Updates the transponder code with the new code entered by the user.

    :param new_code:
    :return:
    """
    pass
    # new_trans_code = new_code
