from plane_controller.plane_controller import PlaneController
from audio import Audio

__author__ = 'redragonx/daemoniclegend'


# 4 digit id
# 10 digit lat/longs  can have leading zeros format (+/-)XXX.XXXXXX first digit is 0 or 1 sign bit
# 6 digit altitude
# 4 digit velocity


class ADSIO():
    input_stream = None
    parsed_data = None
    id = None
    lat = None
    long = None
    altitude = None
    velocity = None

    def __init__(self):
        pass

    def input_listener(self):
        pass

    def parse_string(self, userInput):
        self.input_stream = userInput  # raw_input()  removed currently for testing purposes
        parsed_data = []

        if len(self.input_stream) == 34:
            id = self.input_stream[0:-30]
            lat = self.input_stream[4:-20]
            long = self.input_stream[14:-10]
            altitude = self.input_stream[24:-4]
            velocity = self.input_stream[30:]

            parsed_data.insert(0, id)
            parsed_data.insert(1, lat)
            parsed_data.insert(2, long)
            parsed_data.insert(3, altitude)
            parsed_data.insert(4, velocity)

            # PlaneController.input_data(parsed_data)

        else:
            parsed_data = "INCOMPLETE"
            # errors to be added later
            # Audio.audio_alert('bad_raw_data_error')

        return parsed_data
