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

            print( errorSound )
            sound = pyglet.media.load(errorSound)
            sound.play()

            pyglet.clock.schedule_once(exit_callback, 5)
            pyglet.app.run()
            return True
        elif error_type == 'adjustvert2':
            # sound = pyglet.media.load('adjustvert2.wav')
            # sound.play()
            # pyglet.app.run()
            return True
        elif error_type == 'clear':
            # sound = pyglet.media.load('clear.wav')
            # sound.play()
            # pyglet.app.run()
            return True
        elif error_type == 'climb':
            # sound = pyglet.media.load('climb.wav')
            # sound.play()
            # pyglet.app.run()
            return True
        elif error_type == 'climb2':
            # sound = pyglet.media.load('climb2.wav')
            # sound.play()
            # pyglet.app.run()
            return True
        elif error_type == 'climbcross':
            # sound = pyglet.media.load('climbcross.wav')
            # sound.play()
            # pyglet.app.run()
            return True
        elif error_type == 'climbnow':
            # sound = pyglet.media.load('climbnow.wav')
            # sound.play()
            # pyglet.app.run()
            return True
        elif error_type == 'crossdescend':
            # sound = pyglet.media.load('crossdescend.wav')
            # sound.play()
            # pyglet.app.run()
            return True
        elif error_type == 'descend':
            # sound = pyglet.media.load('descend.wav')
            # sound.play()
            # pyglet.app.run()
            return True
        elif error_type == 'descend2':
            # sound = pyglet.media.load('descend2.wav')
            # sound.play()
            # pyglet.app.run()
            return True
        elif error_type == 'descendcross':
            # sound = pyglet.media.load('descendcross.wav')
            # sound.play()
            # pyglet.app.run()
            return True
        elif error_type == 'descendnow':
            # sound = pyglet.media.load('descendnow.wav')
            # sound.play()
            # pyglet.app.run()
            return True
        elif error_type == 'incrclimb':
            # sound = pyglet.media.load('incrclimb.wav')
            # sound.play()
            # pyglet.app.run()
            return True
        elif error_type == 'incrdescend':
            # sound = pyglet.media.load('incrdescend.wav')
            # sound.play()
            # pyglet.app.run()
            return True
        elif error_type == 'incrdescent':
            # sound = pyglet.media.load('incrdescent.wav')
            # sound.play()
            # pyglet.app.run()
            return True
        elif error_type == 'maintain':
            # sound = pyglet.media.load('maintain.wav')
            # sound.play()
            # pyglet.app.run()
            return True
        elif error_type == 'maintaincross':
            # sound = pyglet.media.load('maintaincross.wav')
            # sound.play()
            # pyglet.app.run()
            return True
        elif error_type == 'monitor':
            # sound = pyglet.media.load('monitor.wav')
            # sound.play()
            # pyglet.app.run()
            return True
        elif error_type == 'noclimb':
            # sound = pyglet.media.load('noclimb.wav')
            # sound.play()
            # pyglet.app.run()
            return True
        elif error_type == 'nodescend':
            # sound = pyglet.media.load('nodescend.wav')
            # sound.play()
            # pyglet.app.run()
            return True
        elif error_type == 'testok':
            # sound = pyglet.media.load('crossclimb.wav')
            # sound.play()
            # pyglet.app.run()
            return True
        elif error_type == 'testfail':
            # sound = pyglet.media.load('testfail.wav')
            # sound.play()
            # pyglet.app.run()
            return True
        elif error_type == 'traffic':
            # sound = pyglet.media.load('traffic.wav')
            # sound.play()
            # pyglet.app.run()
            return True
        elif error_type == 'traffic2':
            # sound = pyglet.media.load('traffic2.wav')
            # sound.play()
            # pyglet.app.run()
            return True
        elif error_type == 'bad_raw_data_error':
            # sound = pyglet.media.load('testfail.wav')
            # sound.play()
            # pyglet.app.run()
            return True
        elif error_type == 'bad_data_integrity_error':
            # sound = pyglet.media.load('testfail.wav')
            # sound.play()
            # pyglet.app.run()
            return True
        elif error_type == 'you_entered':
            # sound = pyglet.media.load('youentered.wav')
            # sound.play()
            # pyglet.app.run()
            return True
        elif error_type == '0':
            # sound = pyglet.media.load('zero.wav')
            # sound.play()
            # pyglet.app.run()
            return True
        elif error_type == '1':
            # sound = pyglet.media.load('one.wav')
            # sound.play()
            # pyglet.app.run()
            return True
        elif error_type == '2':
            # sound = pyglet.media.load('two.wav')
            # sound.play()
            # pyglet.app.run()
            return True
        elif error_type == '3':
            # sound = pyglet.media.load('three.wav')
            # sound.play()
            # pyglet.app.run()
            return True
        elif error_type == '4':
            # sound = pyglet.media.load('four.wav')
            # sound.play()
            # pyglet.app.run()
            return True
        elif error_type == '5':
            # sound = pyglet.media.load('five.wav')
            # sound.play()
            # pyglet.app.run()
            return True
        elif error_type == '6':
            # sound = pyglet.media.load('six.wav')
            # sound.play()
            # pyglet.app.run()
            return True
        elif error_type == '7':
            # sound = pyglet.media.load('seven.wav')
            # sound.play()
            # pyglet.app.run()
            return True
        elif error_type == '8':
            # sound = pyglet.media.load('eight.wav')
            # sound.play()
            # pyglet.app.run()
            return True
        elif error_type == '9':
            # sound = pyglet.media.load('nine.wav')
            # sound.play()
            # pyglet.app.run()
            return True
        else:
            return False
