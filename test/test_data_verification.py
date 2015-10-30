import unittest
import computation_package.data_verification
import program_objects.plane

__author__ = 'group'


class TestDataVerification(unittest.TestCase):

    def setUp(self):
        pass

    def test_within_distance_true(self):
        my_class = computation_package.data_verification

        plane1 = program_objects.plane
        plane1.current_long = -65.41584
        plane1.current_lat = -104.48541
        plane1.current_vel = 180

        plane2 = program_objects.plane
        plane2.current_long = -70.41584
        plane2.current_lat = -115.48541
        plane2.current_vel = 162

        self.assertTrue(my_class.within_distance(plane1))
        self.assertTrue(my_class.within_distance(plane2))

    def test_within_distance_false(self):
        my_class = computation_package.data_verification
        plane3 = program_objects.plane
        plane4 = program_objects.plane
        self.assertFalse(my_class.within_distance(plane3))
        self.assertFalse(my_class.within_distance(plane4))

    def test_verify_data_true(self):
        my_class = computation_package.data_verification
        plane5 = program_objects.plane
        plane6 = program_objects.plane
        self.assertFalse(my_class.verify_data(plane5))
        self.assertFalse(my_class.verify_data(plane6))

    def test_verify_data_false(self):
        my_class = computation_package.data_verification
        plane7 = program_objects.plane
        plane8 = program_objects.plane
        self.assertFalse(my_class.verify_data(plane7))
        self.assertFalse(my_class.verify_data(plane8))


if __name__ == '__main__':
    unittest.main()