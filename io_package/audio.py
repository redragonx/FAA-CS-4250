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
            error_sound = os.path.join(self.__audio_dir, "adjustvert.wav")

            sound = pyglet.media.load(error_sound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'adjustvert2':
            error_sound = os.path.join(self.__audio_dir, "adjustvert2.wav")

            sound = pyglet.media.load(error_sound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'clear':
            error_sound = os.path.join(self.__audio_dir, "clear.wav")

            sound = pyglet.media.load(error_sound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'climb':
            error_sound = os.path.join(self.__audio_dir, "climb.wav")

            sound = pyglet.media.load(error_sound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'climb2':
            error_sound = os.path.join(self.__audio_dir, "climb2.wav")

            sound = pyglet.media.load(error_sound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'climbcross':
            error_sound = os.path.join(self.__audio_dir, "climbcross.wav")

            sound = pyglet.media.load(error_sound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'climbnow':
            error_sound = os.path.join(self.__audio_dir, "climbnow.wav")

            sound = pyglet.media.load(error_sound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'crossdescend':
            error_sound = os.path.join(self.__audio_dir, "crossdescend.wav")

            sound = pyglet.media.load(error_sound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'descend':
            error_sound = os.path.join(self.__audio_dir, "descend.wav")

            sound = pyglet.media.load(error_sound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'descend2':
            error_sound = os.path.join(self.__audio_dir, "descend2.wav")

            sound = pyglet.media.load(error_sound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'descendcross':
            error_sound = os.path.join(self.__audio_dir, "descendcross.wav")

            sound = pyglet.media.load(error_sound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'descendnow':
            error_sound = os.path.join(self.__audio_dir, "descendnow.wav")

            sound = pyglet.media.load(error_sound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'incrclimb':
            error_sound = os.path.join(self.__audio_dir, "incrclimb.wav")

            sound = pyglet.media.load(error_sound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'incrdescend':
            error_sound = os.path.join(self.__audio_dir, "incrdescend.wav")

            sound = pyglet.media.load(error_sound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'incrdescent':
            error_sound = os.path.join(self.__audio_dir, "incrdescent.wav")

            sound = pyglet.media.load(error_sound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'maintain':
            error_sound = os.path.join(self.__audio_dir, "maintain.wav")

            sound = pyglet.media.load(error_sound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'maintaincross':
            error_sound = os.path.join(self.__audio_dir, "maintaincross.wav")

            sound = pyglet.media.load(error_sound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'monitor':
            error_sound = os.path.join(self.__audio_dir, "monitor.wav")

            sound = pyglet.media.load(error_sound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'noclimb':
            error_sound = os.path.join(self.__audio_dir, "noclimb.wav")

            sound = pyglet.media.load(error_sound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'nodescend':
            error_sound = os.path.join(self.__audio_dir, "nodescend.wav")

            sound = pyglet.media.load(error_sound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'testok':
            error_sound = os.path.join(self.__audio_dir, "testok.wav")

            sound = pyglet.media.load(error_sound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'testfail':
            error_sound = os.path.join(self.__audio_dir, "testfail.wav")

            sound = pyglet.media.load(error_sound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'traffic':
            error_sound = os.path.join(self.__audio_dir, "traffic.wav")

            sound = pyglet.media.load(error_sound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'traffic2':
            error_sound = os.path.join(self.__audio_dir, "traffic2.wav")

            sound = pyglet.media.load(error_sound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'bad_raw_data_error':
            error_sound = os.path.join(self.__audio_dir, "bad_raw_data_error.wav")

            sound = pyglet.media.load(error_sound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'bad_data_integrity_error':
            error_sound = os.path.join(self.__audio_dir, "bad_data_integrity_error.wav")

            sound = pyglet.media.load(error_sound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'you_entered':
            error_sound = os.path.join(self.__audio_dir, "you_entered.wav")

            sound = pyglet.media.load(error_sound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == '0':
            error_sound = os.path.join(self.__audio_dir, "0.wav")

            sound = pyglet.media.load(error_sound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == '1':
            error_sound = os.path.join(self.__audio_dir, "1.wav")

            sound = pyglet.media.load(error_sound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == '2':
            error_sound = os.path.join(self.__audio_dir, "2.wav")

            sound = pyglet.media.load(error_sound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == '3':
            error_sound = os.path.join(self.__audio_dir, "3.wav")

            sound = pyglet.media.load(error_sound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == '4':
            error_sound = os.path.join(self.__audio_dir, "4.wav")

            sound = pyglet.media.load(error_sound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == '5':
            error_sound = os.path.join(self.__audio_dir, "5.wav")

            sound = pyglet.media.load(error_sound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == '6':
            error_sound = os.path.join(self.__audio_dir, "6.wav")

            sound = pyglet.media.load(error_sound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == '7':
            error_sound = os.path.join(self.__audio_dir, "7.wav")

            sound = pyglet.media.load(error_sound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == '8':
            error_sound = os.path.join(self.__audio_dir, "8.wav")

            sound = pyglet.media.load(error_sound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == '9':
            error_sound = os.path.join(self.__audio_dir, "9.wav")

            sound = pyglet.media.load(error_sound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()

            return True
        else:
            return False
