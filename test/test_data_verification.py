import unittest
from mock import patch
import plane_controller.data_verification
import plane_controller.plane

__author__ = 'group'


class TestDataVerification(unittest.TestCase):

    def setUp(self):
        pass

    def test_within_distance_true(self):
        my_class = plane_controller.data_verification

        plane1 = plane_controller.plane
        plane1.current_long = -65.41584
        plane1.current_lat = -104.48541
        plane1.current_vel = 180

        plane2 = plane_controller.plane
        plane2.current_long = -70.41584
        plane2.current_lat = -115.48541
        plane2.current_vel = 162

        self.assertTrue(my_class.within_distance(plane1))
        self.assertTrue(my_class.within_distance(plane2))

    def test_within_distance_false(self):
        my_class = plane_controller.data_verification
        plane3 = plane_controller.plane
        plane4 = plane_controller.plane
        self.assertFalse(my_class.within_distance(plane3))
        self.assertFalse(my_class.within_distance(plane4))

    @patch('computation_package.data_verification.dispatch_data_vaild')
    def test_verify_data_true(self, mock):
        my_class = plane_controller.data_verification
        plane5 = plane_controller.plane
        plane6 = plane_controller.plane
        self.assertFalse(my_class.verify_data(plane5))
        self.assertFalse(my_class.verify_data(plane6))
        self.assertTrue(mock.called)

    @patch('computation_package.data_verification.dispatch_data_not_vaild')
    def test_verify_data_false(self, mock):
        my_class = plane_controller.data_verification
        plane7 = plane_controller.plane
        plane8 = plane_controller.plane
        self.assertFalse(my_class.verify_data(plane7))
        self.assertFalse(my_class.verify_data(plane8))
        self.assertTrue(mock.called)

if __name__ == '__main__':
    unittest.main()