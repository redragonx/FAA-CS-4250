__author__ = 'redragonx/daemoniclegend'

from plane_controller.data_verification import DataVerify
from plane_controller.plane import PlaneObject
import unittest


class test_data_verification(unittest.TestCase):
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

    def test_within_distance_no_accel(self):
        dv = DataVerify()
        velocity_map_test = {"0001": [[1, 0, 0], 0]}
        plane = self.plane_helper("0001", [0, 0, 0], [1, 0, 0])
        dv.velocity_map = velocity_map_test

        self.assertFalse(dv.within_distance(plane))

    def test_within_distance_accel_1(self):
        dv = DataVerify()
        velocity_map_test = {"0001": [[0, 0, 0], 0]}
        plane = self.plane_helper("0001", [0, 0, 0], [0, 1, 0])
        dv.velocity_map = velocity_map_test

        self.assertTrue(dv.within_distance(plane))

    def test_within_distance_accel_2(self):
        dv = DataVerify()
        velocity_map_test = {"0001": [[0, 0, 1], 0]}
        plane = self.plane_helper("0001", [0, 0, 0], [0, 0, 30])
        dv.velocity_map = velocity_map_test

        self.assertTrue(dv.within_distance(plane))

    def test_within_distance_accel_3(self):
        dv = DataVerify()
        velocity_map_test = {"0001": [[0, 0, 1], 0]}
        plane = self.plane_helper("0001", [0, 0, 0], [0, 0, 31])
        dv.velocity_map = velocity_map_test

        self.assertTrue(dv.within_distance(plane))

    def test_within_distance_accel_4(self):
        dv = DataVerify()
        velocity_map_test = {"0001": [[2, 0, 0], 0]}
        plane = self.plane_helper("0001", [0, 0, 0], [33, 0, 0])
        dv.velocity_map = velocity_map_test

        self.assertFalse(dv.within_distance(plane))

    def test_within_distance_accel_neg(self):
        dv = DataVerify()
        velocity_map_test = {"0001": [[0, 30, 0], 0]}
        plane = self.plane_helper("0001", [0, 0, 0], [0, 15, 0])
        dv.velocity_map = velocity_map_test

        self.assertTrue(dv.within_distance(plane))

    def test_dispatch_data_valid(self, plane):
        return

    def test_dispatch_data_not_vaild(self, alert_type):
        return

    def plane_helper(self, id_code, location_vector, velocity_vector):
        return PlaneObject(id_code,
                                 location_vector[0], location_vector[1], location_vector[2],
                                 velocity_vector[0], velocity_vector[1], velocity_vector[2])

if __name__ == '__main__':
    unittest.main()
