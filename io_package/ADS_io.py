from plane_controller import plane_ctrl
from audio import Audio
from io_package import ADS_ANTENNA
import io

__author__ = 'redragonx/daemoniclegend'


# 4 digit id
# 10 digit lat/longs  can have leading zeros format (+/-)XXX.XXXXXX first digit is 0 or 1 sign bit
# 6 digit altitude
# 8 digit x velocity (1 digit sign) (4 digit kilometers/hour speed; ranges from 0kph - 9,999 kph) (3 digit decimal ranging from (.000-.999))
# 8 digit y velocity (1 digit sign) (4 digit kilometers/hour speed; ranges from 0kph - 9,999 kph) (3 digit decimal ranging from (.000-.999))
# 8 digit z velocity (1 digit sign) (4 digit kilometers/hour speed; ranges from 0kph - 9,999 kph) (3 digit decimal ranging from (.000-.999))


class ADSIO():
    audio = Audio()
    input_stream = io.BufferedReader(ADS_ANTENNA, 54)
    string_out = None
    parsed_data = None
    plane_id = None
    plane_lat = None
    plane_long = None
    plane_altitude = None
    x = None
    y = None
    z = None

    def __init__(self):
        pass

    def input_listener(self):
        while self.input_stream.peek() != None:
            self.string_out = self.input_stream.read()
            self.parse_string(self, self.string_out)

    def parse_string(self, user_input):
        self.input_stream = user_input  # raw_input()  removed currently for testing purposes
        parsed_data = []

        if len(self.input_stream) == 54:
            self.plane_id = self.input_stream[0:-50]
            self.plane_lat = self.input_stream[4:-40]
            self.plane_long = self.input_stream[14:-30]
            self.plane_altitude = self.input_stream[24:-24]
            self.x = self.input_stream[30:-16]
            self.y = self.input_stream[38:-8]
            self.z = self.input_stream[46:]

            parsed_data.insert(0, self.plane_id)
            parsed_data.insert(1, self.plane_lat)
            parsed_data.insert(2, self.plane_long)
            parsed_data.insert(3, self.plane_altitude)
            parsed_data.insert(4, self.x)
            parsed_data.insert(5, self.y)
            parsed_data.insert(6, self.z)

            plane_ctrl.input_data(parsed_data)

        else:
            parsed_data = False

            self.audio.audio_alert('bad_raw_data_error')

        return parsed_data
