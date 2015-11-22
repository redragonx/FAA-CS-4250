__author__ = 'redragonx/daemoniclegend'

import os
import io
# Sound files Copyright (C) 2004, Danny Ho, danniho@canada.com
import pyglet

pyglet.options['audio'] = ('openal', 'pulse', 'directsound', 'silent',)


class Audio():
    __audio_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Soundfiles'))

    def __init__(self):
        pass

    def audio_alert(self, stringIn):

        def exit_callback(dt):
            pyglet.app.exit()

        error_type = stringIn

        if error_type == 'adjustvert':
            errorSound = os.path.join(self.__audio_dir, "adjustvert.wav")

            sound = pyglet.media.load(errorSound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'adjustvert2':
            errorSound = os.path.join(self.__audio_dir, "adjustvert2.wav")

            sound = pyglet.media.load(errorSound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'clear':
            errorSound = os.path.join(self.__audio_dir, "clear.wav")

            sound = pyglet.media.load(errorSound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'climb':
            errorSound = os.path.join(self.__audio_dir, "climb.wav")

            sound = pyglet.media.load(errorSound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'climb2':
            errorSound = os.path.join(self.__audio_dir, "climb2.wav")

            sound = pyglet.media.load(errorSound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'climbcross':
            errorSound = os.path.join(self.__audio_dir, "climbcross.wav")

            sound = pyglet.media.load(errorSound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'climbnow':
            errorSound = os.path.join(self.__audio_dir, "climbnow.wav")

            sound = pyglet.media.load(errorSound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'crossdescend':
            errorSound = os.path.join(self.__audio_dir, "crossdescend.wav")

            sound = pyglet.media.load(errorSound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'descend':
            errorSound = os.path.join(self.__audio_dir, "descend.wav")

            sound = pyglet.media.load(errorSound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'descend2':
            errorSound = os.path.join(self.__audio_dir, "descend2.wav")

            sound = pyglet.media.load(errorSound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'descendcross':
            errorSound = os.path.join(self.__audio_dir, "descendcross.wav")

            sound = pyglet.media.load(errorSound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'descendnow':
            errorSound = os.path.join(self.__audio_dir, "descendnow.wav")

            sound = pyglet.media.load(errorSound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'incrclimb':
            errorSound = os.path.join(self.__audio_dir, "incrclimb.wav")

            sound = pyglet.media.load(errorSound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'incrdescend':
            errorSound = os.path.join(self.__audio_dir, "incrdescend.wav")

            sound = pyglet.media.load(errorSound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'incrdescent':
            errorSound = os.path.join(self.__audio_dir, "incrdescent.wav")

            sound = pyglet.media.load(errorSound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'maintain':
            errorSound = os.path.join(self.__audio_dir, "maintain.wav")

            sound = pyglet.media.load(errorSound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'maintaincross':
            errorSound = os.path.join(self.__audio_dir, "maintaincross.wav")

            sound = pyglet.media.load(errorSound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'monitor':
            errorSound = os.path.join(self.__audio_dir, "monitor.wav")

            sound = pyglet.media.load(errorSound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'noclimb':
            errorSound = os.path.join(self.__audio_dir, "noclimb.wav")

            sound = pyglet.media.load(errorSound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'nodescend':
            errorSound = os.path.join(self.__audio_dir, "nodescend.wav")

            sound = pyglet.media.load(errorSound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'testok':
            errorSound = os.path.join(self.__audio_dir, "testok.wav")

            sound = pyglet.media.load(errorSound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'testfail':
            errorSound = os.path.join(self.__audio_dir, "testfail.wav")

            sound = pyglet.media.load(errorSound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'traffic':
            errorSound = os.path.join(self.__audio_dir, "traffic.wav")

            sound = pyglet.media.load(errorSound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'traffic2':
            errorSound = os.path.join(self.__audio_dir, "traffic2.wav")

            sound = pyglet.media.load(errorSound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'bad_raw_data_error':
            errorSound = os.path.join(self.__audio_dir, "bad_raw_data_error.wav")

            sound = pyglet.media.load(errorSound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'bad_data_integrity_error':
            errorSound = os.path.join(self.__audio_dir, "bad_data_integrity_error.wav")

            sound = pyglet.media.load(errorSound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'you_entered':
            errorSound = os.path.join(self.__audio_dir, "you_entered.wav")

            sound = pyglet.media.load(errorSound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == '0':
            errorSound = os.path.join(self.__audio_dir, "0.wav")

            sound = pyglet.media.load(errorSound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == '1':
            errorSound = os.path.join(self.__audio_dir, "1.wav")

            sound = pyglet.media.load(errorSound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == '2':
            errorSound = os.path.join(self.__audio_dir, "2.wav")

            sound = pyglet.media.load(errorSound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == '3':
            errorSound = os.path.join(self.__audio_dir, "3.wav")

            sound = pyglet.media.load(errorSound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == '4':
            errorSound = os.path.join(self.__audio_dir, "4.wav")

            sound = pyglet.media.load(errorSound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == '5':
            errorSound = os.path.join(self.__audio_dir, "5.wav")

            sound = pyglet.media.load(errorSound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == '6':
            errorSound = os.path.join(self.__audio_dir, "6.wav")

            sound = pyglet.media.load(errorSound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == '7':
            errorSound = os.path.join(self.__audio_dir, "7.wav")

            sound = pyglet.media.load(errorSound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == '8':
            errorSound = os.path.join(self.__audio_dir, "8.wav")

            sound = pyglet.media.load(errorSound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == '9':
            errorSound = os.path.join(self.__audio_dir, "9.wav")

            sound = pyglet.media.load(errorSound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()

            return True
        else:
            return False
