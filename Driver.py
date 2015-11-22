__author__ = 'Dean'
from threading import Thread
from io_package.ADS_io import *
from plane_controller import *


def main():
    Thread(target=plane_ctrl.plane_controller_driver).start()#initilizes plane_ctrl_diver and continues till program exits
    ADSIO.input_listener()#input the long number system


if __name__ == '__main__':
    main()
