__author__ = 'redragonx/daemoniclegend'

from plane_controller.data_verification import DataVerify
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

    def test_within_distance(self, plane1):
        return

    def test_dispatch_data_valid(self, plane):
        return

    def test_dispatch_data_not_vaild(self, alert_type):
        return


if __name__ == '__main__':
    unittest.main()
