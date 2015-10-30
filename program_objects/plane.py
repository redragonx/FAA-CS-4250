__author__ = 'group'


class PlaneObject(object):

    transponder_code = 0

    name = ''

    current_lat = 0

    current_long = 0

    current_altitude = 0

    current_velocity = 0

    previous_velocity = 0

    previous_lat = 0

    previous_long = 0

    previous_altitude = 0

    def __init__(self, transponder_code, name, current_lat, current_long, current_altitude, current_velocity):
        self.current_altitude = current_altitude
        self.current_lat = current_lat
        self.current_long = current_long
        self.name = name
        self.transponder_code = transponder_code
        self.current_velocity = current_velocity
