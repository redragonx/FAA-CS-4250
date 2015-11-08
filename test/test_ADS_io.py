import unittest
from io_package.ADS_io import ADSIO

__author__ = 'redragonx/daemoniclegend'

# 4 digit id
# 10 digit lat/longs  can have leading zeros format (+/-)XXX.XXXXXX first digit is 0 or 1 sign bit
# 6 digit altitude
# 4 digit velocity


class TestADS_Io(unittest.TestCase):
    __sampleData = "0001" \
                   "0174678922" \
                   "1045375468" \
                   "035700" \
                   "06007890" \
                   "46539201" \
                   "57890345"

    __bad_sample_data = "0001" \
                        "0174678922" \
                        "10453754684" \
                        "035700" \
                        "06007890" \
                        "46539201" \
                        "57890345"

    __incomplete_sample_data = "0009" \
                               "0174678922" \
                               "1045375468" \
                               "035700" \
                               "06007890" \
                               "46539201" \
                               "5789034"

    __sample_data_list = ["0001", "0174678922", "1045375468", "035700", "06007890", "46539201", "57890345"]

    def test_parse_string(self):
        ads = ADSIO()

        # makes sure each part of both lists are the same.
        self.assertEqual(self.__sample_data_list, ads.parse_string(self.__sampleData), 'Test 1 failed.')

        # -----------------------------------------------------------------------------

        # testing with bad data...
        # returns a list.

        self.assertFalse(ads.parse_string(self.__bad_sample_data), 'Test 2 failed.')

        # -----------------------------------------------------------------------------

        # tests for incomplete or missing input data
        # returns a string

        self.assertFalse(ads.parse_string(self.__incomplete_sample_data), 'Test 3 failed.')


if __name__ == '__main__':
    unittest.main()
