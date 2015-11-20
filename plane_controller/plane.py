__author__ = 'group'


class PlaneObject(object):
    id_code = 0  # single identifier
    location_vector = []
    velocity_vector = []
    tuc_interval = -1
    __elevation = 0
    update_time = -1.0

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

    def update_plane(self, p_plane_location, p_plane_velocity, elevation):
        self.location_vector = p_plane_location
        self.velocity_vector = p_plane_velocity
        self.elevation = elevation

