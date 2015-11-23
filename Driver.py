__author__ = 'Dean/Alton09'
from threading import Thread
from io_package.ADS_io import *
from plane_controller import *
from plane_controller.plane_ctrl import *
import time

def main():
    global primary_aircraft
    global adsb_obj
    adsb_obj = ADSIO()
    primary_aircraft.id_code = "0001"
    primary_aircraft.update_plane([0, 0, 0], [0, 0, 0], 6391000)
    Thread(target=plane_ctrl.plane_controller_driver).start()

    #These are different cases to test. Recommended to run them differrently becausse they are bsed
    #off the location of the primary aircraift and it being set to different locations in each case
    test_1()
    time.sleep(15)
    test_1()
    time.sleep(15)
    #test_1()
    #test_2()
    # test_3()
    #test_4()

def test_1():
    """ Test 1 Plane 9 and 10 hit """
    adsb_obj.parse_string("000100900000000000000000020000000000000000000000000000")
    adsb_obj.parse_string("001000899936610045000000020000100100001001000000000000")
    # adsb_obj.parse_string("000100900000000000000000020000000000000000000000000000")
    # adsb_obj.parse_string("001000899936610045000000020000100100001001000000000000")
    # adsb_obj.parse_string("000100900000000000000000020000000000000000000000000000")
    # adsb_obj.parse_string("001000899936610045000000020000100100001001000000000000")


def test_2():
    """ Test 2 Plane 10 hit """
    adsb_obj.parse_string("000100900000000000000000020000000000000000000000000000")
    time.sleep(1)
    adsb_obj.parse_string("001000899936610045000000020000100100001001000000000000")
    time.sleep(1)
    adsb_obj.parse_string("000300899462100000000000020002001000000000000000000000")
    time.sleep(1)
    adsb_obj.parse_string("000400899372450000000000020003001000000000000000000000")
    time.sleep(1)
    adsb_obj.parse_string("000500899282790000000000020005001000000000000000000000")
    time.sleep(1)
    adsb_obj.parse_string("000600899193140000000000020006001000000000000000000000")
    time.sleep(1)
    adsb_obj.parse_string("000700899462100180000000020002101000000000000000000000")
    time.sleep(1)
    adsb_obj.parse_string("000800899372450180000000020003101000000000000000000000")
    time.sleep(1)
    adsb_obj.parse_string("000900899282790180000000020005101000000000000000000000")
    time.sleep(1)
    adsb_obj.parse_string("001000899936600045000000019500100100001001000000010000")

def test_3():
    """ Test 1 Plane 9 and 10 hit """
    adsb_obj.parse_string("000100900000000000000000020000000000000000000000000000")
    # time.sleep(1)
    adsb_obj.parse_string("000200899551750000000000020001001000000000000000000000")
    # time.sleep(1)
    adsb_obj.parse_string("000300899462100000000000020002001000000000000000000000")
    # time.sleep(1)
    adsb_obj.parse_string("000400899372450000000000020003001000000000000000000000")
    # time.sleep(1)
    adsb_obj.parse_string("000500899282790000000000020005001000000000000000000000")
    # time.sleep(1)
    adsb_obj.parse_string("000600899193140000000000020006001000000000000000000000")
    # time.sleep(1)
    adsb_obj.parse_string("000700899462100180000000020002101000000000000000000000")
    # time.sleep(1)
    adsb_obj.parse_string("000800899372450180000000020003101000000000000000000000")
    # time.sleep(1)
    adsb_obj.parse_string("000900899282790180000000020005101000000000000000000000")
    # time.sleep(1)
    adsb_obj.parse_string("001000899936600045000000019500000100000001000000010000")

def test_4():
    """ Test 2 Plane 10 hit """
    adsb_obj.parse_string("000100900000000000000000020000000000000000000000000000")
    adsb_obj.parse_string("000400899372450000000000020003001000000000000000000000")
    adsb_obj.parse_string("000800899372450180000000020003101000000000000000000000")
    adsb_obj.parse_string("001000899936600045000000019500100100001001000000010000")

if __name__ == '__main__':
    main()
