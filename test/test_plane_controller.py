__author__ = 'daemoniclegend'
from mock import *
from plane_controller.plane_ctrl import *
from plane_controller import plane
from io_package.audio import Audio
from computation_package.collision_detection import CollisionDetection
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

    # # patch.object if the method that you are testing is in a class
    # @patch.multiple("plane_controller.plane_ctrl",
    #                 collision_detection_generator = DEFAULT,
    #                 find_highest_priority_s = DEFAULT,
    #                 get_corrective_action = DEFAULT,
    #                 dispatch_collision_alerts = DEFAULT)
    # def test_plane_controller_driver(self, collision_detection_generator,
    #                                  find_highest_priority_s,
    #                                  get_corrective_action,
    #                                  dispatch_collision_alerts):
    #     '''
    #      This method checks to see if the plane driver calls its correct sequence of commands
    #     '''
    #     #1. collision_detection_generator -> calculates and returns a list of all the planes on a collision course with
    #          the PA
    #     #1. find_highest_priority -> returns list of 1 or 2 planes
    #     #2. corrective action -> String command
    #     #3. dispatch event -> sends chris's audio alert
    #     # arrange
    #
    #     # action
    #     plane_controller_driver()
    #     # assert
    #     self.assertTrue(collision_detection_generator.call_count > 0)
    #     self.assertTrue(find_highest_priority_s.call_count > 0)
    #     self.assertTrue(get_corrective_action.call_count > 0)
    #     self.assertTrue(dispatch_collision_alerts > 0)
    #     # pass
    #
    # @patch.multiple("plane_controller.plane_ctrl",
    #                 convert_to_cartesian_meters = DEFAULT,
    #                 data_verify = DEFAULT,
    #                 update_plane_list = DEFAULT)
    # def test_input_data(self,convert_to_cartesian_meters
    #                     ,data_verify,update_plane_list):
    #     '''
    #      This method test to see if input_data calls its correct methods and follows the correct order
    #      convert -> data_verify -> update_plane_list
    #     '''
    #     #arrange
    #         # data_in =[id,lat,long,altitude,x,y,z]
    #         data_in =[10,111,222,2,0,1,0]
    #         c_t_c =[]
    #         plane_location, plane_velocity = [0, 0, 0], [100, 100, 100]
    #         plane_obj = self.plane_helper("0011", plane_location, plane_velocity)
    #
    #     # action
    #         input_data(data_in)
    #
    #     # assert
    #         self.assertEqual(convert_to_cartesian_meters.call_count,1)
    #         self.assertEqual(data_verify.call_count,1)
    #         self.assertEqual(update_plane_list.call_count,1)
    #         convert_to_cartesian_meters.assert_called_once_with(data_in)
    #         data_verify.assert_called_once_with(c_t_c)
    #         update_plane_list.assert_called_once_with(plane_obj)
    #     # pass
    #
    # def test_convert_to_cartesian_meters(self):
    #     '''
    #      This method test to see if the latitude longitude and elevation come back in their repsective
    #      cartesian coordinates
    #     '''
    #     original_data1 =[]
    #     c_t_c1 =[]
    #     self.assertEquals(convert_to_cartesian_meters(original_data1), c_t_c1)
    #     original_data2 =[]
    #     c_t_c2 =[]
    #     self.assertEquals(convert_to_cartesian_meters(original_data2), c_t_c2)
    #     original_data3 =[]
    #     c_t_c3 =[]
    #     self.assertEquals(convert_to_cartesian_meters(original_data3), c_t_c3)


    # def test_find_highest_priority_s(self):
    #     '''
    #     This is testing find_highest method. It sends in a list with the 10 closest planes on a collision with the PA.
    #     It will return a list containing 1 or 2 planes in the same TUC
    #
    #     '''
    #     data_in=[]
    #     data_out=[]
    #     self.assertEqual(find_highest_priority_s(data_in),data_out)
    #     data_in=[]
    #     data_out=[]
    #     self.assertEqual(find_highest_priority_s(data_in),data_out)
    #     data_in=[]
    #     data_out=[]
    #     self.assertEqual(find_highest_priority_s(data_in),data_out)
    #
    #     # pass
    #
    # def test_update_plane_list(self):
    #     '''
    #     This is testing to make sure the update_plane_list method updates the global nearby_planes_list.
    #
    #     '''
    #     global nearby_planes_list
    #     nearby_planes_list = []
    #     plane_location, plane_velocity = [0, 0, 0], [100, 100, 100]
    #     plane_obj = self.plane_helper("0011", plane_location, plane_velocity)
    #     update_plane_list(plane_obj)
    #     list = [plane_obj]
    #     self.assertEqual(nearby_planes_list, list)

    # @patch.object(Audio,"audio_alert")
    # def test_dispatch_collision_alerts(self, mock_audio_alert):
    #     '''
    #     This method tests to see if dispatch_collision_alerts sends the correct audio alert to the audio class.
    #     :param mock_audio_alert:
    #     :return:
    #     '''
    #     alert_type = 'climb'
    #     dispatch_collision_alerts(alert_type)
    #     mock_audio_alert.assert_called_once_with(alert_type)
    #

    # def test_get_corrective_action(self):
    #     '''
    #     This method tests get_corrective_action to see if the correct alert is sent to the user
    #     after it has checked for the 1 or 2 closest planes to avoid.
    #     '''
    #     global primary_aircraft
    #     p_plane_location1, p_plane_velocity1 = [0, 0, 0], [100, 100, 100]
    #     primary_aircraft = self.plane_helper("0011", p_plane_location1,p_plane_velocity1)
    #     plane_location1, plane_velocity1 = [0, 0, 0], [100, 100, 100]
    #     plane_location2, plane_velocity2 = [0, 0, 0], [100, 100, 100]
    #     plane_obj1 = self.plane_helper("0011", plane_location1, plane_velocity1)
    #     plane_obj2 = self.plane_helper("0011", plane_location2, plane_velocity2)
    #     planes_list = [plane_obj1 ,plane_obj2 ]
    #     alert_type = "ASCEND"
    #     self.assertEqual(get_corrective_action(planes_list),alert_type)

    @patch.object(CollisionDetection,
                "determine_collision")
    def test_collision_detection_generator(self, mock_determine_collision):
        global nearby_planes_list
        nearby_planes_list = []
        final_l = collision_detection_generator()
        self.assertEqual(mock_determine_collision.call_count, len(nearby_planes_list))





    # def test_update_transponder_code(self):
    #     pass

    def plane_helper(self, id_code, location_vector, velocity_vector):
        return plane.PlaneObject(id_code,
                                 location_vector[0], location_vector[1], location_vector[2],
                                 velocity_vector[0], velocity_vector[1], velocity_vector[2])



if __name__ == '__main__':
    unittest.main()
