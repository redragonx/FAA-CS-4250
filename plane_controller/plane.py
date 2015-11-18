__author__ = 'group'


class PlaneObject(object):
    id_code = 0  # single identifier
    location_vector = []
    velocity_vector = []
    tuc_interval = -1
    elevation = 0

    def __init__(self, id_code, loc_x, loc_y, loc_z, vec_x, vec_y, vec_z, elevation=-1):
        self.id_code = id_code
        self.location_vector = [loc_x, loc_y, loc_z]
        self.velocity_vector = [vec_x, vec_y, vec_z]
        self.elevation = elevation

    def set_tuc_interval(self, tuc):
        """
        Sets the time until the planes collide.

        DON'T CHANGE THIS OUTSIDE OF COLLISION DETECTION MODULE.

        :param tuc:
        :return:
        """
        self.tuc_interval = tuc
