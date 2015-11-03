__author__ = 'redragonx/daemoniclegend'

# 4 digit id
# 10 digit lat/longs  can have leading zeros format +/-XXX.XXXXXX first digit is 0 or 1 sign bit
# 6 digit altitude
# 4 digit velocity


class ADSIO():

    input_stream =  None
    parsed_data = None
    id = None
    lat, long = None
    altitude = None
    velocity = None

    def __init__(self):
        pass

    def input_listener(self):
        pass

    def parse_string(self):
        self.input_stream = raw_input()
        parsed_data = None

        if len(self.input_stream) == 34:
            id = self.input_stream[0:-30]
            lat = self.input_stream[5:-24]
            long = self.input_stream[15:-14]
            altitude = self.input_stream[25:-30]
            velocity = self.input_stream[31:]

            parsed_data.insert[0] = id
            parsed_data.insert[1] = lat
            parsed_data.insert[2] = long
            parsed_data.insert[3] = altitude
            parsed_data.insert[4] = velocity

            plane_controller.input_data(parsed_data)

        else:
            audio_alert('bad_raw_data_error')

        return parsed_data
