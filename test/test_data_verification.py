__author__ = 'redragonx/daemoniclegend/Alton09'

from plane_controller.data_verification import DataVerify
from plane_controller.plane import PlaneObject
import unittest
import time
from threading import Thread

class test_data_verification(unittest.TestCase):
    id_code = "0001"

    def test_verify_data(self):
        dv = DataVerify()
        __good_data_list = ["0001", "0074678922", "1045375468", "035700", "06007890", "46539201", "57890345"]
        __alpha_list = ["0A01", "0074678922", "1045375468", "035700", "06007890", "46539201", "57890345"]
        __bad_lat_list1 = ["0001", "0094678922", "1045375468", "035700", "06007890", "46539201", "57890345"]
        __bad_lat_list2 = ["0001", "2074678922", "1045375468", "035700", "06007890", "46539201", "57890345"]
        __bad_long_list1 = ["0001", "0074678922", "1085375468", "035700", "06007890", "46539201", "57890345"]
        __bad_long_list2 = ["0001", "0074678922", "2045375468", "035700", "06007890", "46539201", "57890345"]

        self.assertEqual('True', dv.verify_data(__good_data_list), 'Test 1 failed')
        self.assertEqual('False', dv.verify_data(__alpha_list), 'Test 2 failed')
        self.assertEqual('False', dv.verify_data(__bad_lat_list1), 'Test 3 failed')
        self.assertEqual('False', dv.verify_data(__bad_lat_list2), 'Test 4 failed')
        self.assertEqual('False', dv.verify_data(__bad_long_list1), 'Test 5 failed')
        self.assertEqual('False', dv.verify_data(__bad_long_list2), 'Test 6 failed')

    def test_within_distance_new_vel_entry(self):
        id_code = self.id_code
        velocity_map = DataVerify.velocity_map
        plane = self.plane_helper(id_code, [0, 0, 0], [2, 0, 0])
        plane2 = self.plane_helper(id_code, [0, 0, 0], [10, 0, 0])

        time.sleep(1)
        self.assertTrue(DataVerify.within_distance(plane))
        self.assertTrue(DataVerify.within_distance(plane2))

    def test_within_distance_no_accel(self):
        id_code = self.id_code
        velocity_map = DataVerify.velocity_map
        plane = self.plane_helper(id_code, [0, 0, 0], [5, 5, 5])
        velocity_map[id_code] = [DataVerify.vector_magnitude([5, 5, 5]), time.time()]

        time.sleep(5)
        self.assertFalse(DataVerify.within_distance(plane))

    def test_within_distance_accel_1(self):
        id_code = self.id_code
        velocity_map = DataVerify.velocity_map
        plane = self.plane_helper(id_code, [0, 0, 0], [19, 0, 0])
        velocity_map[id_code] = [DataVerify.vector_magnitude([18, 0, 0]), time.time()]

        time.sleep(1)
        self.assertTrue(DataVerify.within_distance(plane))


    def test_within_distance_accel_2(self):
        id_code = self.id_code
        velocity_map = DataVerify.velocity_map
        plane = self.plane_helper(id_code, [0, 0, 0], [0, 0, 1])
        velocity_map[id_code] = [DataVerify.vector_magnitude([0, 0, 30]), time.time()]

        time.sleep(1)
        self.assertTrue(DataVerify.within_distance(plane))

    def test_within_distance_accel_3(self):
        id_code = self.id_code
        velocity_map = DataVerify.velocity_map
        plane = self.plane_helper(id_code, [0, 0, 0], [0, 61, 0])
        velocity_map[id_code] = [DataVerify.vector_magnitude([0, 1, 0]), time.time()]

        time.sleep(2)
        self.assertTrue(DataVerify.within_distance(plane))

    def test_within_distance_accel_4(self):
        id_code = self.id_code
        velocity_map = DataVerify.velocity_map
        plane = self.plane_helper(id_code, [0, 0, 0], [2, 0, 0])
        velocity_map[id_code] = [DataVerify.vector_magnitude([34, 0, 0]), time.time()]

        time.sleep(1)
        self.assertFalse(DataVerify.within_distance(plane))

    def plane_helper(self, id_code, location_vector, velocity_vector):
        return PlaneObject(id_code,
                                 location_vector[0], location_vector[1], location_vector[2],
                                 velocity_vector[0], velocity_vector[1], velocity_vector[2])

if __name__ == '__main__':
    unittest.main()
