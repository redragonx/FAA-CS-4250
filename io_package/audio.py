__author__ = 'redragonx/daemoniclegend'

# Sound files Copyright (C) 2004, Danny Ho, danniho@canada.com

# import pyglet

class Audio():

    def audio_alert(self, stringIn):

        error_type = stringIn

        if error_type == 'adjustvert':
            # sound = pyglet.resource.media('adjustvert.wav')
            # sound.play()
            # pyglet.app.run()
            return 'Valid'
        elif error_type == 'adjustvert2':
            # sound = pyglet.resource.media('adjustvert2.wav')
            # sound.play()
            # pyglet.app.run()
            return 'Valid'
        elif error_type == 'clear':
            # sound = pyglet.resource.media('clear.wav')
            # sound.play()
            # pyglet.app.run()
            return 'Valid'
        elif error_type == 'climb':
            # sound = pyglet.resource.media('climb.wav')
            # sound.play()
            # pyglet.app.run()
            return 'Valid'
        elif error_type == 'climb2':
            # sound = pyglet.resource.media('climb2.wav')
            # sound.play()
            # pyglet.app.run()
            return 'Valid'
        elif error_type == 'climbcross':
            # sound = pyglet.resource.media('climbcross.wav')
            # sound.play()
            # pyglet.app.run()
            return 'Valid'
        elif error_type == 'climbnow':
            # sound = pyglet.resource.media('climbnow.wav')
            # sound.play()
            # pyglet.app.run()
            return 'crossclimb'
        elif error_type == 'testok':
            # sound = pyglet.resource.media('crossclimb.wav')
            # sound.play()
            # pyglet.app.run()
            return 'Valid'
        elif error_type == 'crossdescend':
            # sound = pyglet.resource.media('crossdescend.wav')
            # sound.play()
            # pyglet.app.run()
            return 'Valid'
        elif error_type == 'descend':
            # sound = pyglet.resource.media('descend.wav')
            # sound.play()
            # pyglet.app.run()
            return 'Valid'
        elif error_type == 'descend2':
            # sound = pyglet.resource.media('descend2.wav')
            # sound.play()
            # pyglet.app.run()
            return 'Valid'
        elif error_type == 'descendcross':
            # sound = pyglet.resource.media('descendcross.wav')
            # sound.play()
            # pyglet.app.run()
            return 'Valid'
        elif error_type == 'descendnow':
            # sound = pyglet.resource.media('descendnow.wav')
            # sound.play()
            # pyglet.app.run()
            return 'Valid'
        elif error_type == 'incrclimb':
            # sound = pyglet.resource.media('incrclimb.wav')
            # sound.play()
            # pyglet.app.run()
            return 'Valid'
        elif error_type == 'incrdescend':
            # sound = pyglet.resource.media('incrdescend.wav')
            # sound.play()
            # pyglet.app.run()
            return 'Valid'
        elif error_type == 'incrdescent':
            # sound = pyglet.resource.media('incrdescent.wav')
            # sound.play()
            # pyglet.app.run()
            return 'Valid'
        elif error_type == 'maintain':
            # sound = pyglet.resource.media('maintain.wav')
            # sound.play()
            # pyglet.app.run()
            return 'Valid'
        elif error_type == 'maintaincross':
            # sound = pyglet.resource.media('maintaincross.wav')
            # sound.play()
            # pyglet.app.run()
            return 'Valid'
        elif error_type == 'monitor':
            # sound = pyglet.resource.media('monitor.wav')
            # sound.play()
            # pyglet.app.run()
            return 'Valid'
        elif error_type == 'noclimb':
            # sound = pyglet.resource.media('noclimb.wav')
            # sound.play()
            # pyglet.app.run()
            return 'Valid'
        elif error_type == 'nodescend':
            # sound = pyglet.resource.media('nodescend.wav')
            # sound.play()
            # pyglet.app.run()
            return 'Valid'
        elif error_type == 'testfail':
            # sound = pyglet.resource.media('testfail.wav')
            # sound.play()
            # pyglet.app.run()
            return 'Valid'
        elif error_type == 'traffic':
            # sound = pyglet.resource.media('traffic.wav')
            # sound.play()
            # pyglet.app.run()
            return 'Valid'
        elif error_type == 'traffic2':
            # sound = pyglet.resource.media('traffic2.wav')
            # sound.play()
            # pyglet.app.run()
            return 'Valid'
        elif error_type == 'bad_raw_data_error':
            # sound = pyglet.resource.media('testfail.wav')
            # sound.play()
            # pyglet.app.run()
            return 'Valid'
        elif error_type == 'bad_data_integrity_error':
            # sound = pyglet.resource.media('testfail.wav')
            # sound.play()
            # pyglet.app.run()
            return 'Valid'
        else:
            return 'Invalid'
