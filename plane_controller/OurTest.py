__author__ = 'abelamadou'
from plane_ctrl import *
import plane
from threading import Thread
from time import sleep




def main():
    # print "Befor", primary_aircraft.id_code
    update_transponder_code(1001)
    # print primary_aircraft.id_code
    Thread(target=plane_controller_driver).start()



    print "Going to start the threads....."

    # for i in testing_now1():
    #     Thread(target=put_in_plane_test,args=(i,)).start()
    put_in_p(testing_now1())
    sleep(2)
    put_in_p(testing_now2())

def put_in_p(list):
      for i in list:
        # Thread(target=put_in_plane,args=(i,)).start()
       put_in_plane(i)



def testing_now1():
    pr_ar = PlaneObject("1001", 0, 0, 0, 0, 0, 0) #shouldnt hit
    dummy_plane1 = PlaneObject("1", 400, 0, 0, 100, 0, 0) #shouldnt hit
    # dummy_plane2 = PlaneObject("2", 500, 500, -500, -10, -10, 10) #should hit
    # dummy_plane3 = PlaneObject("3", -401, 0, 0, 100, 0, 0) #should hit
    dummy_plane2 = PlaneObject("2", 400, 0, 0, 100, 0, 0) #shouldnt hit
    dummy_plane3 = PlaneObject("3", 400, 0, 0, 100, 0, 0) #shouldnt hit
    dummy_plane4 = PlaneObject("4", 400, 0, 0, 100, 0, 0) #shouldnt hit
    dummy_plane5 = PlaneObject("5", 400, 0, 0, 100, 0, 0) #shouldnt hit
    dummy_plane6 = PlaneObject("6", 400, 0, 0, 100, 0, 0) #shouldnt hit
    dummy_plane7 = PlaneObject("7", 400, 0, 0, 100, 0, 0) #shouldnt hit
    dummy_plane8 = PlaneObject("8", 400, 0, 0, 100, 0, 0) #shouldnt hit
    dummy_plane9 = PlaneObject("9", 400, 0, 0, 100, 0, 0) #shouldnt hit
    # dummy_plane9 = PlaneObject("9", 500, 500, -500, -10, -10, 10) #should hit
    dummy_plane10 = PlaneObject("10", 500, 500, -500, -10, -10, 10) #should hit
    list_of_planes=[]
    list_of_planes.append(dummy_plane1)
    list_of_planes.append(dummy_plane2)
    list_of_planes.append(dummy_plane3)
    list_of_planes.append(dummy_plane4)
    list_of_planes.append(dummy_plane5)
    list_of_planes.append(dummy_plane6)
    list_of_planes.append(dummy_plane7)
    list_of_planes.append(dummy_plane8)
    list_of_planes.append(dummy_plane9)
    list_of_planes.append(dummy_plane10)

    return list_of_planes

def testing_now2():
    pr_ar = PlaneObject("1001", 0, 0, 0, 0, 0, 0) #shouldnt hit
    dummy_plane1 = PlaneObject("1", 400, 0, 0, 100, 0, 0) #shouldnt hit
    # dummy_plane2 = PlaneObject("2", 500, 500, -500, -10, -10, 10) #should hit
    # dummy_plane3 = PlaneObject("3", -401, 0, 0, 100, 0, 0) #should hit
    dummy_plane2 = PlaneObject("2", 400, 0, 0, 100, 0, 0) #shouldnt hit
    dummy_plane3 = PlaneObject("3", 400, 0, 0, 100, 0, 0) #shouldnt hit
    dummy_plane4 = PlaneObject("4", 400, 0, 0, 100, 0, 0) #shouldnt hit
    dummy_plane5 = PlaneObject("5", 400, 0, 0, 100, 0, 0) #shouldnt hit
    dummy_plane7 = PlaneObject("7", 400, 0, 0, 100, 0, 0) #shouldnt hit
    dummy_plane8 = PlaneObject("8", 400, 0, 0, 100, 0, 0) #shouldnt hit
    dummy_plane9 = PlaneObject("9", 400, 0, 0, 100, 0, 0) #shouldnt hit
    # dummy_plane9 = PlaneObject("9", 500, 500, -500, -10, -10, 10) #should hit
    dummy_plane10 = PlaneObject("10", 500, 500, -500, -10, -10, 10) #should hit
    list_of_planes=[]
    list_of_planes.append(dummy_plane1)
    list_of_planes.append(dummy_plane2)
    list_of_planes.append(dummy_plane3)
    list_of_planes.append(dummy_plane4)
    list_of_planes.append(dummy_plane5)
    list_of_planes.append(dummy_plane7)
    list_of_planes.append(dummy_plane8)
    list_of_planes.append(dummy_plane9)
    list_of_planes.append(dummy_plane10)

    return list_of_planes


if __name__ == '__main__':
    main()
