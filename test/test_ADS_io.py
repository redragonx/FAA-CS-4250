import unittest
from io_package.ADS_io import ADSIO

__author__ = 'group'


# 4 digit id
# 10 digit lat/longs  can have leading zeros format +/-XXX.XXXXXX first digit is 0 or 1 sign bit
# 6 digit altitude
# 4 digit velocity

class TestADS_Io(unittest.TestCase):
    __sampleData = "0001" \
                   "0174678922" \
                   "1045375468" \
                   "035700" \
                   "0600"

    __bad_sample_data = "0009" \
                        "0174678922" \
                        "1045375468" \
                        "035700" \
                        "0602"

    __incomplete_sample_data = "0009" \
                               "0174678922" \
                               "1045375468" \
                               "035700" \
                               "060"

    __sample_data_list = ["0001", "0174678922", "1045375468", "035700", "0600"]

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

            # testing with bad data...
            # returns a list.
        test_list = ads.parse_string(self.__bad_sample_data)

        if test_list == None:
            test2_answer = True

        # makes sure each part of both lists are not the same.
        if set(test_list) != set(self.__sample_data_list):
            test2_answer = True
        else:
            test2_answer = False

        test_list = ads.parse_string(self.__incomplete_sample_data)

        if test_list == None or test_list == "INCOMPLETE":
            test3_answer = True

        print("test_parse_string_good_data: ", test1_answer)
        print("test_parse_string_bad_data: ", test2_answer)
        print("Incomplete data: ", test3_answer)


'''    input_stream = None
    parsed_data = None
    id = None
    lat, long = None
    altitude = None
    velocity = None

    def setUp(self):
        pass

def input_listener(self):
    pass

# just a  test , not the method
def parse_string(self):
    self.input_stream = raw_input("0001017467892210453754680357000600")
    parsed_data = None

    if len(self.input_stream) == 34:
        id = self.input_stream[0:-30]
        lat = self.input_stream[4:13]
        long = self.input_stream[14:23]
        altitude = self.input_stream[24:29]
        velocity = self.input_stream[30:]

        parsed_data.insert[0] = id
        parsed_data.insert[1] = lat
        parsed_data.insert[2] = long
        parsed_data.insert[3] = altitude
        parsed_data.insert[4] = velocity

#        plane_controller.input_data(parsed_data)

    else:
#        audio_alert('bad_raw_data_error')

    self.assertEqal(parsed_data, ["0001", "0174678922", "045375468", "035700", "0600"], "Wrong")
'''

if __name__ == '__main__':
    unittest.main()
