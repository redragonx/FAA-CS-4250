__author__ = 'daemoniclegend'
from mock import *
from plane_controller.plane_ctrl import *
from plane_controller import plane
import unittest

'''
.return_value=#Value you want it to equal
.side_effect=[]#irretable thing
.call_count #{returns How times called}
mock_name.assert_called_once_with(name of paremeter)
'''

class TestPlaneController(unittest.TestCase):

    # patch.object if the method that you are testing is in a class
    def test_plane_controller_driver(self,mock_input_data):
        # arrange
        # action
        # assert
        pass

    @patch.multiple("plane_ctrl",
                    convert_to_cartesian_meters = DEFAULT,
                    data_verify = DEFAULT,
                    update_plane_list = DEFAULT)
    def test_input_data(self,convert_to_cartesian_meters
                        ,data_verify,update_plane_list):
        #arrange
            # data_in =[id,lat,long,altitude,x,y,z]
            data_in =[10,111,222,2,0,1,0]
            c_t_c =[]
            plane_location, plane_velocity = [0, 0, 0], [100, 100, 100]
            plane_obj = self.plane_helper("0011", plane_location, plane_velocity)

        # action
            input_data(data_in)

        # assert
            self.assertEqual(convert_to_cartesian_meters.call_count,1)
            self.assertEqual(data_verify.call_count,1)
            self.assertEqual(update_plane_list.call_count,1)
            convert_to_cartesian_meters.assert_called_once_with(data_in)
            data_verify.assert_called_once_with(c_t_c)
            update_plane_list.assert_called_once_with(plane_obj)
        # pass

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

    def plane_helper(self, id_code, location_vector, velocity_vector):
        return plane.PlaneObject(id_code,
                                 location_vector[0], location_vector[1], location_vector[2],
                                 velocity_vector[0], velocity_vector[1], velocity_vector[2])



if __name__ == '__main__':
    unittest.main()