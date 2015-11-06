__author__ = 'group'


class PlaneObject(object):

    id_code = 0    ### single identifier

    current_lat = 0
    current_long = 0
    current_altitude = 0
    current_velocity = 0
    vector = [0, 0, 0]
    tuc_interval = -1

    def __init__(self, id_code, current_lat, current_long, current_altitude, vectorX, vectorY, vectorZ):
        self.id_code = id_code
        self.current_lat = current_lat
        self.current_long = current_long
        self.current_altitude = current_altitude
        self.vector[0] = vectorX
        self.vector[1] = vectorY
        self.vector[2] = vectorZ

    def set_tuc_interval(self, tuc):
        """
        Sets the time until the planes collide.

        DON'T CHANGE THIS OUTSIDE OF COLLISION DETECTION MODULE.

        :param tuc:
        :return:
        """
        self.tuc_interval = tuc

