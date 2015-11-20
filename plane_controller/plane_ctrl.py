__corrective_actions = ["ASCEND", "MAINTAIN ALTITUDE", "DESCEND"]
#https://docs.python.org/2/library/queue.html#Queue.Queue.join
from multiprocessing.pool import ThreadPool
from Queue import Queue
from computation_package.collision_detection import CollisionDetection
from threading import Thread
from plane_controller.data_verification import DataVerify

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
    Use Event to wait for the input to reliquinsh the lock so that we can update the nearby_planes_list


    dispatch_collision_alerts(get_corrective_action(find_highest_priority_s(collision_detection_generator())))

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
    #     Thread(target= CollisionDetection().build_collision_list, args=(dummy_pa, i ,queue)).start()
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

    # dummy_plane1 = PlaneObject("1", 400, 0, 0, 100, 0, 0) #shouldnt hit
    # # dummy_plane2 = PlaneObject("2", 500, 500, -500, -10, -10, 10) #should hit
    # # dummy_plane3 = PlaneObject("3", -401, 0, 0, 100, 0, 0) #should hit
    # dummy_plane2 = PlaneObject("2", 400, 0, 0, 100, 0, 0) #shouldnt hit
    # dummy_plane3 = PlaneObject("3", 400, 0, 0, 100, 0, 0) #shouldnt hit
    # dummy_plane4 = PlaneObject("4", 400, 0, 0, 100, 0, 0) #shouldnt hit
    # dummy_plane5 = PlaneObject("5", 400, 0, 0, 100, 0, 0) #shouldnt hit
    # dummy_plane6 = PlaneObject("6", 400, 0, 0, 100, 0, 0) #shouldnt hit
    # dummy_plane7 = PlaneObject("7", 400, 0, 0, 100, 0, 0) #shouldnt hit
    # dummy_plane8 = PlaneObject("8", 400, 0, 0, 100, 0, 0) #shouldnt hit
    # dummy_plane9 = PlaneObject("9", 400, 0, 0, 100, 0, 0) #shouldnt hit
    # # dummy_plane9 = PlaneObject("9", 500, 500, -500, -10, -10, 10) #should hit
    # dummy_plane10 = PlaneObject("10", 500, 500, -500, -10, -10, 10) #should hit
    #
    #
    #
    # # dummy_plane2 = PlaneObject("2", 1, 1, 1, 2, 2, 2)
    # # dummy_plane3 = PlaneObject("3", 1, 1, 1, 2, 2, 2)
    # # dummy_plane4 = PlaneObject("4", 1, 1, 1, 2, 2, 2)
    # # dummy_plane5 = PlaneObject("5", 1, 1, 1, 2, 2, 2)
    # # dummy_plane6 = PlaneObject("6", 1, 1, 1, 2, 2, 2)
    # # dummy_plane7 = PlaneObject("7", 1, 1, 1, 2, 2, 2)
    # # dummy_plane8 = PlaneObject("8", 1, 1, 1, 2, 2, 2)
    # # dummy_plane9 = PlaneObject("9", 1, 1, 1, 2, 2, 2)
    # # dummy_plane10 = PlaneObject("10", 1, 1, 1, 2, 2, 2)
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
    # print len(nearby_planes_list)
    print "This isnt correct: " + str(nearby_planes_list)

    queue = Queue()
    thread_list = []
    # print len(nearby_planes_list)
    for i in nearby_planes_list:
        t = Thread(target=CollisionDetection().build_collision_list, args=(dummy_pa, i ,queue))
        thread_list.append(t)
        t.start()

    for i in thread_list:
        i.join()
    # print "Here passed Join......."

    collision_course_planes = []
    # print "Que:",queue.qsize()
    if queue.qsize() > 0:
        for i in iter(queue.get, None):
            collision_course_planes.append(i)
            if queue._qsize() == 0:
                break

    for i in collision_course_planes:
        print i.id_code

    # print "RL:",len(collision_course_planes)
    # print "Done......."
    return collision_course_planes



def input_data(data_in):
    """
    Takes the data from the plane_controller_driver and sends that information to data_verification.

    :param data_in:
    :return:
    """
    verifier = DataVerify()
    result = verifier.verify_data(data_in)
    numerical_data = __convert_to_numbers(data_in)
    if result:
        cartesian_list = convert_to_cartesian_meters(numerical_data[1:4])
        plane_object = PlaneObject(data_in[0], cartesian_list[0], cartesian_list[1], cartesian_list[2], data_in[4],
                                   data_in[5], data_in[6], data_in[3])
        if verifier.within_distance(plane_object):
            update_plane_list(plane_object)

    # ["1067118752", "1103679115", "5815"]



def __convert_to_numbers(list_in):
    list_in[0] = int(list_in[0])
    list_in[1] = __convert_lat_long(list_in[1])
    list_in[2] = __convert_lat_long(list_in[2])
    list_in[3] = int(list_in[3])
    list_in[4] = __convert_vector(list_in[4])
    list_in[5] = __convert_vector(list_in[5])
    list_in[6] = __convert_vector(list_in[6])
    return list_in


def __convert_lat_long(string_lat_long):
    unsigned_lat_long = string_lat_long[1:10]
    if string_lat_long == 0:
        return float(unsigned_lat_long) / 1000000
    else:
        return -1 * float(unsigned_lat_long) / 1000000


def __convert_vector(string_vector):
    unsigned_vector = string_vector[1:8]
    if string_vector == 0:
        return float(unsigned_vector) / 1000
    else:
        return -1 * float(unsigned_vector) / 1000



#180000000 -> 180.000000 = a degree value


def convert_to_cartesian_meters(list_in):
    """
    Converts the list of data from latitude, longitude, and elevation to cartesian coordinates.

    :param list_in: the initial list of data in elevation, latitude, and longitude.
    :return: list_out: the list with cartesian coordinates in place of location information. list should be
    in the following format:
        loc_x
        loc_y
        loc_z
    """
    pass


def find_highest_priority_s(collision_list):
    """
    Finds the plane or planes, when applicable, with the highest priority and returns them as list to the caller.

    :param
    :return: high_priority_list: the the collisions with the highest priority
    """
    priority_list =[]

    if len(collision_list) != 0:
        for p in collision_list:
            if len(priority_list) < 2:
                priority_list.append(p)
            else:
                if p.tuc_interval < priority_list[0].tuc_interval:
                    if priority_list[0].tuc_interval < priority_list[1].tuc_interval:
                        priority_list[1] = p
                    else:
                        priority_list[0] = p
                elif p.tuc_interval < priority_list[1].tuc_interval:
                    priority_list[1] = p
                else:
                    pass
    if len(priority_list) == 0 or len(priority_list) == 1:
        return priority_list
    elif __get_priority(priority_list[0]) == __get_priority(priority_list[1]):
        return priority_list
    else:
        if __get_priority(priority_list[0]) == "HIGH" or __get_priority(priority_list[1]) == "HIGH":
            if __get_priority(priority_list[0]) == "HIGH":
                return [priority_list[0]]
            else:
                return [priority_list[1]]
        elif __get_priority(priority_list[0]) == "MEDIUM" or __get_priority(priority_list[1]) == "MEDIUM":
            if __get_priority(priority_list[0]) == "MEDIUM":
                return [priority_list[0]]
            else:
                return [priority_list[1]]
        elif __get_priority(priority_list[0]) == "LOW" or __get_priority(priority_list[1]) == "LOW":
            if __get_priority(priority_list[0]) == "LOW":
                return [priority_list[0]]
            else:
                return [priority_list[1]]
    return "Unreachable Error"


def __get_priority(plane):
    if plane.tuc_interval < 1*60:
        return "HIGH"
    elif plane.tuc_interval < 3 * 60:
        return "MEDIUM"
    elif plane.tuc_interval < 10 * 60:
        return "LOW"
    else:
        return "LOWEST"

'''
    """
    These conditional statements check to see if the TUC of one plane is 2x greater than the other,
    if it is greater then we take closest plane which, under these conditions,
    we have designated to be a higher priority.
    """
    if len(priority_list) == 0 or len(priority_list) == 1:
        return priority_list
    elif len(priority_list) == 2:
        if priority_list[0].tuc_interval / priority_list[1].tuc_interval > 2.0:
            return [priority_list[1]]
        elif priority_list[1].tuc_interval / priority_list[0].tuc_interval > 2.0:
            return [priority_list[0]]
        else:
            return priority_list
'''
    # pass
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


def get_corrective_action(priority_list):
    """
    Calculates the corrective action of the primary aircraft, will ascend or descend or maintain elevation based
    upon the GPS location of the PA relative to other Aircraft.

    :param planes: planes
    :return: climb, maintain, descend
    """
    #global primary_aircraft
    #primary_aircraft = primary_aicrt


    print "Elv: " + str(primary_aircraft.elevation)
    print "lox y: " + str(primary_aircraft.location_vector[1])
    print "vect z:: " + str(primary_aircraft.velocity_vector[2])


    if len(priority_list) == 0:
        return "Do Nothing"
    elif len(priority_list) == 1:
        if (__compare_planes(primary_aircraft, priority_list[0])) == 1:
            return "climb"
        else:
            return "descend"
    elif len(priority_list) == 2:
        result_intruder1 = __compare_planes(primary_aircraft, priority_list[0])
        result_intruder2 = __compare_planes(primary_aircraft, priority_list[1])
        result = result_intruder1 + result_intruder2
        #if = 2 then the PA needs to go above both the planes
        if result == 2:
            return "climb"
        #else if result is equal to 0 then the PA should maintain its elevation and not move
        elif result == 0:
            return "maintain"
        #else if the result is = -2 then the PA should descend
        elif result == -2:
            return "descend"
        else:
            return "Error"




def __compare_planes(plane1, plane2):
    '''

    :param plane1:
    :param plane2:
    :return:
    '''

    result_elevation = __compare_numbers(plane1.elevation, plane2.elevation)
    if result_elevation != 0:
        return result_elevation

    result_x = __compare_numbers(plane1.location_vector[0], plane2.location_vector[0])
    if result_x != 0:
        return result_x

    result_y = __compare_numbers(plane1.location_vector[1], plane2.location_vector[1])
    if result_y != 0:
        return result_y

    result_z = __compare_numbers(plane1.location_vector[2], plane2.location_vector[2])
    if result_z != 0:
        return result_z

    return -5

def __compare_numbers(float1, float2):
    if float1 > float2:
        return 1
    elif float1 < float2:
        return -1
    else:
        return 0


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
