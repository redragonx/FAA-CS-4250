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

    __bad_sample_data = "0009" \
                        "0174678922" \
                        "1045375468" \
                        "035700" \
                        "06007893" \
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
        test1_answer = False
        test2_answer = False
        test3_answer = False

        # returns a list.
        test_list = ads.parse_string(self.__sampleData)

        if test_list is None:
            test1_answer = False

        # makes sure each part of both lists are the same.
        if set(test_list) == set(self.__sample_data_list):
            test1_answer = True

        else:
            test1_answer = False

        # -----------------------------------------------------------------------------

        # testing with bad data...
            # returns a list.
        test_list = ads.parse_string(self.__bad_sample_data)

        if test_list is None:
            test2_answer = True

        # makes sure each part of both lists are not the same.
        if set(test_list) != set(self.__sample_data_list):
            test2_answer = True
        else:
            test2_answer = False

        # -----------------------------------------------------------------------------

        # tests for incomplete or missing input data
        # returns a string
        test_list = ads.parse_string(self.__incomplete_sample_data)

        if test_list is None or test_list == "INCOMPLETE":
            test3_answer = True

        print("test_parse_string_good_data: ", test1_answer)
        print("test_parse_string_bad_data: ", test2_answer)
        print("Incomplete data: ", test3_answer)


if __name__ == '__main__':
    unittest.main()
