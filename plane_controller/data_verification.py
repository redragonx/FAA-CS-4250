__author__ = 'redragonx/daemoniclegend/Alton09'

# from plane_controller.plane import PlaneObject
import re
import time
import math
from threading import Lock
from plane_controller.plane import  PlaneObject

class DataVerify():
    velocity_map = {}

    def verify_data(self, list_in):
        data_list = list_in
        idPattern = re.compile("[0-9]{4}")
        latPattern = re.compile("[01][0][0-8][0-9]{7}|[0-1][0][9][0]{7}")
        longPattern = re.compile("[0-1][0-1][0-7][0-9]{6}|[0-1][0-1][8][0]{5}")
        altitudePattern = re.compile("^[0-9]{6}")
        vectorPattern = re.compile("^[0-9]{8}")

        if idPattern.match(data_list[0]):
            if latPattern.match(data_list[1]):
                if longPattern.match(data_list[2]):
                    if altitudePattern.match(data_list[3]):
                        if vectorPattern.match(data_list[4]):
                            if vectorPattern.match(data_list[5]):
                                if vectorPattern.match(data_list[6]):
                                    # here is where the plane object itself would be returned after creation
                                    return 'True'
                                else:
                                    return 'False'
                            else:
                                return 'False'
                        else:
                            return 'False'
                    else:
                        return 'False'
                else:
                    return 'False'
            else:
                return 'False'
        else:
            return 'False'

    def within_distance(self,plane):
        id_code = plane.id_code
        velocity = self.vector_magnitude(plane.velocity_vector)
        current_time = time.time()  # In seconds
        return_val = False

        try:
            existing_value = self.velocity_map[id_code]
            existing_vel = existing_value[0]
            existing_time = existing_value[1]
        except KeyError:
            self.velocity_map[id_code] = [velocity, current_time]
            return True

        if self.__correct_acceleration(existing_vel, velocity, existing_time, current_time):
            return_val = True
        else:
            return_val = False

        return return_val

    def __correct_range(self,num):
        if 0 < num <= 30:
            return True
        else:
            return False

    def __correct_acceleration(self, velocity1, velocity2, time1, time2):
        delta_v = abs(velocity2 - velocity1)
        delta_t = abs(time2 - time1)
        if delta_t != 0:
            acceleration = delta_v / delta_t
            return self.__correct_range(acceleration)
        elif delta_t == 0:
            return False

    def vector_magnitude(self,velocity):
        if velocity.__len__() == 3:
            return math.sqrt(math.pow(velocity[0], 2) +
                         math.pow(velocity[1], 2) + math.pow(velocity[2], 2))
        else:
            return None

    def __init__(self):
        pass