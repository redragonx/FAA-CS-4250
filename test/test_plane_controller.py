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
mock_name.call_args_list =>
                        returns a list of all the parameter that was passed in to the method
                        have to be used with {call(paremater checking)

'''

class TestPlaneController(unittest.TestCase):

    # patch.object if the method that you are testing is in a class
    @patch.multiple("plane_controller.plane_ctrl",
                    collision_detection_generator = DEFAULT,
                    find_highest_priority_s = DEFAULT,
                    get_corrective_action = DEFAULT,
                    dispatch_collision_alerts = DEFAULT)
    def test_plane_controller_driver(self, collision_detection_generator,
                                     find_highest_priority_s,
                                     get_corrective_action,
                                     dispatch_collision_alerts):
        #1. find_highest_priority -> returns list of 1 or 2 planes
        #2. corrective action -> String command
        #3. dispatch event -> sends chris's audio alert
        # arrange

        # action
        plane_controller_driver()
        # assert
        self.assertTrue(collision_detection_generator.call_count > 0)
        self.assertTrue(find_highest_priority_s.call_count > 0)
        self.assertTrue(get_corrective_action.call_count > 0)
        self.assertTrue(dispatch_collision_alerts > 0)
        # pass

    @patch.multiple("plane_controller.plane_ctrl",
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

    def test_convert_to_cartesian_meters(self):
        original_data1 =[]
        c_t_c1 =[]
        self.assertEquals(convert_to_cartesian_meters(original_data1), c_t_c1)
        original_data2 =[]
        c_t_c2 =[]
        self.assertEquals(convert_to_cartesian_meters(original_data2), c_t_c2)
        original_data3 =[]
        c_t_c3 =[]
        self.assertEquals(convert_to_cartesian_meters(original_data3), c_t_c3)

    @patch("plane_controller.plane_ctrl.")
    def test_find_highest_priority_s(self):
        plane_location1, plane_velocity1 = [0, 0, 0], [100, 100, 100]
        plane_location2, plane_velocity2 = [0, 0, 0], [100, 100, 100]
        plane_location3, plane_velocity3 = [0, 0, 0], [100, 100, 100]
        plane_obj1 = self.plane_helper("0011", plane_location1, plane_velocity1)
        plane_obj2 = self.plane_helper("0011", plane_location2, plane_velocity2)
        plane_obj3 = self.plane_helper("0011", plane_location3, plane_velocity3)
        data_in_collision_list = [plane_obj1,plane_obj2,plane_obj3]
        pass
    #
    # def test_update_plane_list(plane):
    #     pass
    #
    # def test_dispatch_collision_alerts(alert_type):
    #     pass
    #
    # def test_get_corrective_action(*planes):
    #     pass
    #
    # def test_update_transponder_code(new_code):
    #     pass
    #
    # def test_collision_collision_detection_generator(self):
    #     pass


    def plane_helper(self, id_code, location_vector, velocity_vector):
        return plane.PlaneObject(id_code,
                                 location_vector[0], location_vector[1], location_vector[2],
                                 velocity_vector[0], velocity_vector[1], velocity_vector[2])



if __name__ == '__main__':
    unittest.main()
