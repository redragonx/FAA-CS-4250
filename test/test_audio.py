import unittest
from io_package.audio import Audio


__author__ = 'redragonx/daemoniclegend'


class TestAudio(unittest.TestCase):

    def test_audio_alert(self):
        audio = Audio()

        test1_answer = False
        test2_answer = False
        response = None
        __goodString = 'testok'
        __badString = 'Bad Error Message'

    # tests using a valid error code
        response = audio.audio_alert(__goodString)
        if response == 'Valid':
            test1_answer = True

        print('Test with valid input: ', test1_answer)

    # tests using an invalid error code
        response = audio.audio_alert(__badString)
        if response == 'Invalid':
            test2_answer = True

        print('Test with valid input: ', test2_answer)


if __name__ == '__main__':
    unittest.main()