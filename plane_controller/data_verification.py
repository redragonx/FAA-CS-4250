__author__ = 'redragonx/daemoniclegend'

from plane_controller.plane import PlaneObject
import re

class DataVerify():

    def verify_data(self, list_in):
        data_list = list_in
        idPattern = re.compile("\d{4}")
        latPattern = re.compile("[0-1][0](([0-8]\d{8})|([9][0]{8}))")
        longPattern = re.compile("[0-1][0-1](([0-7]\d{8})|([8][0]{7}))")
        vectorPattern = re.compile("\d{8}")
        VALID = True
        if idPattern.match(data_list(0)):
            if latPattern.match(data_list(1)):
                if longPattern.match(data_list(2)):
                    if vectorPattern.match(data_list(3)):
                        if vectorPattern.match(data_list(4)):
                            if vectorPattern.match(data_list(5)):
                                verified_plane = PlaneObject(data_list(0), data_list(1), data_list(2), data_list(3),
                                                             data_list(4), data_list(5))
        return verified_plane, True

    def within_distance(self, plane1):
        return

    def dispatch_data_valid(self, plane):
        return

    def dispatch_data_not_vaild(self, alert_type):
        return

    def __init__(self):
        pass
