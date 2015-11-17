__corrective_actions = ["ASCEND", "MAINTAIN ALTITUDE", "DESCEND"]
#https://docs.python.org/2/library/queue.html#Queue.Queue.join
from multiprocessing.pool import ThreadPool
from Queue import Queue
from computation_package.collision_detection import CollisionDetection
from threading import Thread

"""
The set of planes that the ADS-B send in.
"""
from plane import PlaneObject
# __nearby_planes_list = {}
nearby_planes_list = []
primary_aircraft = PlaneObject("00", 0, 0, 0, 0, 0, 0)


def plane_controller_driver():
    """
    This thread runs in all of the computations for detecting collisions and generates relevant alerts.

    :param list_in:
    :return:
    collision_detection_generator():


    """
    pass


def collision_detection_generator():
    """
    This will create threads for each plane and call the collision detection. The collision detection will return
    true or false. If true, the object will be placed into a list. Once all the threads have completed their calculations
    and returned the booleans, the list will contain all of the closest 10 planes that are on a collision course with the
    PA

    :return: list_closest: returns a list with the closest airplanes on a collision course with the PA
    """


    # pool = ThreadPool(processes=10)
    # c_d = CollisionDetection()
    # queue = Queue()
    # for i in nearby_planes_list:
    #     pool.apply_async(c_d.determine_collision(dummy_pa, i, queue)) #A variant of the apply() method which returns a result object.
    # queue.join()
    # collision_course_planes = []
    # for i in iter(queue.get, None):
    #     collision_course_planes.append(i)
    #     if queue._qsize() == 0:
    #         break
    #
    # print(collision_course_planes)
    # for i in collision_course_planes:
    #     print i.id_code

    # pool = ThreadPool(processes=10)
    # c_d = CollisionDetection()
    # queue = Queue()
    # for i in nearby_planes_list:
    #     pool.apply(c_d.determine_collision, (dummy_pa, i, queue))
    # queue.join()
    # collision_course_planes = []
    # for i in iter(queue.get, None):
    #     collision_course_planes.append(i)
    #     if queue._qsize() == 0:
    #         break
    #
    # print(collision_course_planes)
    # for i in collision_course_planes:
    #     print i.id_code

    # dummy_pa = PlaneObject("PA", 1 ,1 ,1 ,2, 2, 2)
    # dummy_plane1 = PlaneObject("1", 1, 1, 1, 2, 2, 2)
    # dummy_plane2 = PlaneObject("2", 1, 1, 1, 2, 2, 2)
    # dummy_plane3 = PlaneObject("3", 1, 1, 1, 2, 2, 2)
    # dummy_plane4 = PlaneObject("4", 1, 1, 1, 2, 2, 2)
    # dummy_plane5 = PlaneObject("5", 1, 1, 1, 2, 2, 2)
    # dummy_plane6 = PlaneObject("6", 1, 1, 1, 2, 2, 2)
    # dummy_plane7 = PlaneObject("7", 1, 1, 1, 2, 2, 2)
    # dummy_plane8 = PlaneObject("8", 1, 1, 1, 2, 2, 2)
    # dummy_plane9 = PlaneObject("9", 1, 1, 1, 2, 2, 2)
    # dummy_plane10 = PlaneObject("10", 1, 1, 1, 2, 2, 2)
    #
    #
    # nearby_planes_list.append(dummy_plane1)
    # nearby_planes_list.append(dummy_plane2)
    # nearby_planes_list.append(dummy_plane3)
    # nearby_planes_list.append(dummy_plane4)
    # nearby_planes_list.append(dummy_plane5)
    # nearby_planes_list.append(dummy_plane6)
    # nearby_planes_list.append(dummy_plane7)
    # nearby_planes_list.append(dummy_plane8)
    # nearby_planes_list.append(dummy_plane9)
    # nearby_planes_list.append(dummy_plane10)
    #
    #
    # queue = Queue()
    # for i in nearby_planes_list:
    #     Thread(target= CollisionDetection().build_collision_list(dummy_pa, i ,queue)).start()
    # queue.join() ## block until all tasks are done
    # collision_course_planes = []
    # for i in iter(queue.get, None):
    #     collision_course_planes.append(i)
    #     if queue._qsize() == 0:
    #         break
    #
    # print collision_course_planes
    # for i in collision_course_planes:
    #     print i.id_code
    # return collision_course_planes
    dummy_pa = PlaneObject("PA", 0 , 0 , 0 , 0, 0, 0)

    dummy_plane1 = PlaneObject("1", 400, 0, 0, 100, 0, 0) #shouldnt hit
    dummy_plane2 = PlaneObject("2", 500, 500, -500, -10, -10, 10) #should hit
    dummy_plane3 = PlaneObject("3", -401, 0, 0, 100, 0, 0) #should hit

    # dummy_plane2 = PlaneObject("2", 1, 1, 1, 2, 2, 2)
    # dummy_plane3 = PlaneObject("3", 1, 1, 1, 2, 2, 2)
    # dummy_plane4 = PlaneObject("4", 1, 1, 1, 2, 2, 2)
    # dummy_plane5 = PlaneObject("5", 1, 1, 1, 2, 2, 2)
    # dummy_plane6 = PlaneObject("6", 1, 1, 1, 2, 2, 2)
    # dummy_plane7 = PlaneObject("7", 1, 1, 1, 2, 2, 2)
    # dummy_plane8 = PlaneObject("8", 1, 1, 1, 2, 2, 2)
    # dummy_plane9 = PlaneObject("9", 1, 1, 1, 2, 2, 2)
    # dummy_plane10 = PlaneObject("10", 1, 1, 1, 2, 2, 2)


    nearby_planes_list.append(dummy_plane1)
    #nearby_planes_list.append(dummy_plane2)
    #nearby_planes_list.append(dummy_plane3)
    # nearby_planes_list.append(dummy_plane3)
    # nearby_planes_list.append(dummy_plane4)
    # nearby_planes_list.append(dummy_plane5)
    # nearby_planes_list.append(dummy_plane6)
    # nearby_planes_list.append(dummy_plane7)
    # nearby_planes_list.append(dummy_plane8)
    # nearby_planes_list.append(dummy_plane9)
    # nearby_planes_list.append(dummy_plane10)


    queue = Queue()
    for i in nearby_planes_list:
        Thread(target= CollisionDetection().build_collision_list(dummy_pa, i ,queue)).start()
    queue.join() ## block until all tasks are done

    collision_course_planes = []
    if queue.qsize() > 0:
        for i in iter(queue.get, None):
            collision_course_planes.append(i)
            if queue._qsize() == 0:
                break

    for i in collision_course_planes:
        print i.id_code
    return collision_course_planes



def input_data(data_in):
    """
    Takes the data from the plane_controller_driver and sends that information to data_verification

    :param data_in:
    :return:
    """
    pass


def convert_to_cartesian_meters(list_in):
    """
    Converts the list of data from latitude, longitude, and elevation to cartesian coordinates.

    :param list_in: the initial list of data in elevation, latitude, and longitude.
    :return: the same list converted
    """
    pass


def find_highest_priority_s(list_in):
    """
    Finds the plane or planes, when applicable, with the highest priority and returns them as list to the caller.

    :param
    :return: high_priority_list: the the collisions with the highest priority
    """
    pass
    # we should reset the tuc interval here of all of them back to -1. So we dont
    # resuse the same tuc interval


def data_verify(list):
    pass


def update_plane_list(plane):
    """
    Adds or updates the plane to the nearby_plane_list

    :param plane:
    :return:
    """
    pass


def dispatch_collision_alerts(alert_type):
    """

    :return:
    """
    # rel_x = PA[loc_x] - new_plane[loc_x]
    # rel_y = PA[loc_y] - new_plane[loc_y]
    # rel_z = PA[loc_z] - new_plane[loc_z]


def get_corrective_action(planes):
    """
    Calculates the corrective action of the primary aircraft, will ascend or descend or maintain elevation based
    upon the GPS location of the PA relative to other Aircraft.

    :param planes: planes
    :return: ASCEND, MAINTAIN ALTITUDE, DESCEND
    """
    pass


#    constructor can go here. each piece can be accessed using   data_in[x]
#    plane.__init__(data_in[0], data_in[1], data_in[2], data_in[3], data_in[4], data_in[5], data_in[6],)

# function to take in a new transponder code for itself from the user keypad
def update_transponder_code(new_code):
    """
    Updates the transponder code with the new code entered by the user.

    :param new_code:
    :return:
    """
    pass
    # new_trans_code = new_code


print collision_detection_generator()
