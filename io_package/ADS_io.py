from plane_controller.plane_controller import PlaneController
from audio import Audio

__author__ = 'redragonx/daemoniclegend'


# 4 digit id
# 10 digit lat/longs  can have leading zeros format (+/-)XXX.XXXXXX first digit is 0 or 1 sign bit
# 6 digit altitude
# 4 digit velocity


class ADSIO():
    audio = Audio()
    input_stream = None
    parsed_data = None
    id = None
    lat = None
    long = None
    altitude = None
    x = None
    y = None
    z = None

    def __init__(self):
        pass

    def input_listener(self):
        pass

    def parse_string(self, userInput):
        self.input_stream = userInput  # raw_input()  removed currently for testing purposes
        parsed_data = []

        if len(self.input_stream) == 54:
            id = self.input_stream[0:-50]
            lat = self.input_stream[4:-40]
            long = self.input_stream[14:-30]
            altitude = self.input_stream[24:-24]
            x = self.input_stream[30:-16]
            y = self.input_stream[38:-8]
            z = self.input_stream[46:]

            parsed_data.insert(0, id)
            parsed_data.insert(1, lat)
            parsed_data.insert(2, long)
            parsed_data.insert(3, altitude)
            parsed_data.insert(4, x)
            parsed_data.insert(5, y)
            parsed_data.insert(6, z)

            # PlaneController.input_data(parsed_data)

        else:
            parsed_data = "INCOMPLETE"

            self.audio.audio_alert('bad_raw_data_error')

        return parsed_data
