__author__ = 'redragonx/daemoniclegend'

# from plane_controller.plane import PlaneObject
import re


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

    def within_distance(self, plane1):
        raise Exception("Not Yet Implemented.")
        # pass
    def dispatch_data_valid(self, plane):
        return

    def dispatch_data_not_vaild(self, alert_type):
        return

    def __init__(self):
        pass
