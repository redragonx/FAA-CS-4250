import unittest
from io_package.audio import Audio

__author__ = 'redragonx/daemoniclegend'


class TestAudio(unittest.TestCase):
    def test_audio_alert(self):
        audio = Audio()

        __goodString = 'adjustvert'
        __badString = 'Bad error message is bad'

        # tests using a valid error code
        self.assertEqual(True, audio.audio_alert(__goodString), "audio test 1 FAILED")

        # tests using an invalid error code
        self.assertEqual(False, audio.audio_alert(__badString), "audio test 2 FAILED")


if __name__ == '__main__':
    unittest.main()
