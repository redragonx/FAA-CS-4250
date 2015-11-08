__author__ = 'daemoniclegend'
from mock import patch
from plane_controller.plane_ctrl import *

import unittest

class test_plane_controller(unittest.testcase):

    # patch.object if the method that you are testing is in a class
    @patch("plane_controller.input_data")
    def test_plane_controller_driver(mock_input_data):
        #arrange

        # action
        plane_controller_driver()
        # asser
    def test_input_data(data_in):
        pass

    def test_convert_to_cartesian_meters(list_in):
        pass

    def test_find_highest_priority_s(collsion_list):
        pass

    def test_update_plane_list(plane):
        pass

    def test_dispatch_collision_alerts(alert_type):
        pass

    def test_get_corrective_action(*planes):
        pass

    def test_update_transponder_code(new_code):
        pass


if __name__ == '__main__':
    unittest.main()