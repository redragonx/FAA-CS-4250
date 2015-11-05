__author__ = 'redragonx/daemoniclegend'

# Sound files Copyright (C) 2004, Danny Ho, danniho@canada.com

# import pyglet

class Audio():

    def audio_alert(self, stringIn):

        error_type = stringIn

        if error_type == 'error1':
            # sound = pyglet.resource.media('testok.wav')
            # sound.play()
            # pyglet.app.run()
            return 'Valid'
        elif error_type == 'bad_raw_data_error':
            # sound = pyglet.resource.media('testfail.wav')
            # sound.play()
            # pyglet.app.run()
            return 'Valid'
        else:
            return 'Invalid'
