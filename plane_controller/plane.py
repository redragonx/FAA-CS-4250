__author__ = 'group'


class PlaneObject(object):

    id_code = 0    ### single identifier

    current_lat = 0
    current_long = 0
    current_altitude = 0
    current_velocity = 0

    previous_velocity = 0
    previous_lat = 0
    previous_long = 0
    previous_altitude = 0

    def __init__(self, id_code, current_lat, current_long, current_altitude, current_velocity):
        self.id_code = id_code
        self.current_lat = current_lat
        self.current_long = current_long
        self.current_altitude = current_altitude
        self.current_velocity = current_velocity
