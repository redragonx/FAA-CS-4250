__author__ = 'Dean'
from threading import Thread
from io_package.ADS_io import *
from plane_controller import *
from plane_controller.plane_ctrl import *

def main():
    global primary_aircraft
    primary_aircraft.id_code = "0001"
    primary_aircraft.update_plane([0, 0, 6391000])
    Thread(target=plane_ctrl.plane_controller_driver).start()#initilizes plane_ctrl_diver and continues till program exits
    ADSIO.input_listener() #input the long number system

# def test_1():
#     ADSIO.input_listener(000100900000000000000000020000000000000000000000000000)#input the long number system
#     time.sleep(0)

if __name__ == '__main__':
    main()
