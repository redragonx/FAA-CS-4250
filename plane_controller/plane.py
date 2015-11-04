__author__ = 'group'


class PlaneObject(object):

    id_code = 0    ### single identifier

    current_lat = 0
    current_long = 0
    current_altitude = 0
    current_velocity = 0
    vectorX = 0
    vectorY = 0
    vectorZ = 0

    def __init__(self, id_code, current_lat, current_long, current_altitude, vectorX, vectorY, vectorZ,):
        self.id_code = id_code
        self.current_lat = current_lat
        self.current_long = current_long
        self.current_altitude = current_altitude
        self.x = vectorX
        self.y = vectorY
        self.z = vectorZ
