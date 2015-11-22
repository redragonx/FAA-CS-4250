__corrective_actions = ["ASCEND", "MAINTAIN ALTITUDE", "DESCEND"]
#https://docs.python.org/2/library/queue.html#Queue.Queue.join
from Queue import Queue
from time import sleep,clock
from computation_package.collision_detection import CollisionDetection
from threading import Thread
from plane_controller.data_verification import DataVerify
from io_package.audio import Audio
__collision_alerts = {
    "HIGH": {"CLIMB": 'climbnow', "DESCEND": 'descendnow', "MAINTAIN": 'maintain'},
    "MEDIUM": {"CLIMB": 'climb2', "DESCEND": 'descend2', "MAINTAIN": 'maintain'},
    "LOW": {"CLIMB": 'climb', "DESCEND": 'descend', "MAINTAIN": 'maintain'}
}
"""
The set of planes that the ADS-B send in.
"""
from plane import PlaneObject
import math
nearby_planes_list = []
primary_aircraft = PlaneObject(-1, 0, 0, 0, 0, 0, 0)
# primary_aircraft = PlaneObject(00, 0, 0, 0, 0, 0, 0)
plane_management_queue=Queue(maxsize=10)

def remove_excess_planes():
    b=0
    for i in nearby_planes_list:
        if(clock()-i.update_time>10):
            nearby_planes_list.pop(b)
        b+=1



def plane_controller_driver():
    """
    This thread runs in all of the computations for detecting collisions and generates relevant alerts.

    :param list_in:
    :return:
    Use Event to wait for the input to reliquinsh the lock so that we can update the nearby_planes_list


    dispatch_collision_alerts(get_corrective_action(find_highest_priority_s(collision_detection_generator())))

    """
    while True:
        clock_time = clock()
        while clock() < clock_time+5:
            if plane_management_queue.qsize()!=0:
                inputed_plane = plane_management_queue.get()
                update_plane_list(inputed_plane)
        remove_excess_planes()
        lookup_list = find_highest_priority_s(collision_detection_generator())
        # print ">>>>>",lookup_list
        lookup_list.reverse()
        if not(lookup_list[0] == "DO NOTHING"):
            # print ">>>>>",lookup_list[0],lookup_list[1][0].to_string()
            lookup_list[1] = get_corrective_action(lookup_list[1])
            dispatch_collision_alerts(lookup_list)

def collision_detection_generator():
    """
    This will create threads for each plane and call the collision detection. The collision detection will return
    true or false. If true, the object will be placed into a list. Once all the threads have completed their calculations
    and returned the booleans, the list will contain all of the closest 10 planes that are on a collision course with the
    PA

    :return: list_closest: returns a list with the closest airplanes on a collision course with the PA
    """

    queue = Queue()
    thread_list = []
    # print "Begin Set","-"*100
    # for i in nearby_planes_list:
    #     print "*"*20
    #     print i.to_string()
    # print "End Set","-"*100
    for i in nearby_planes_list:
        t = Thread(target=CollisionDetection().build_collision_list, args=(primary_aircraft,i,queue))
        thread_list.append(t)
        t.start()

    for i in thread_list:
        i.join()

    collision_course_planes = []
    if queue.qsize() > 0:
        for i in iter(queue.get, None):
            collision_course_planes.append(i)
            if queue._qsize() == 0:
                break

    # for i in collision_course_planes:
        # print i.id_code
    return collision_course_planes

def put_in_plane(plane_object):
    plane_management_queue.put(plane_object)


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
            put_in_plane(plane_object)



def __convert_to_numbers(list_in):
    list_in[0] = int(list_in[0])
    # list_in[1] = __convert_lat_long(list_in[1])
    # list_in[2] = __convert_lat_long(list_in[2])
    # list_in[3] = int(list_in[3])
    list_in[4] = __convert_vector(list_in[4])
    list_in[5] = __convert_vector(list_in[5])
    list_in[6] = __convert_vector(list_in[6])
    return list_in


def __convert_lat_long(string_lat_long):
    unsigned_lat_long = string_lat_long[1:10]
    if int(string_lat_long[0]) == 0:
        return float(unsigned_lat_long) / 1000000
    else:
        return -1 * float(unsigned_lat_long) / 1000000


def __convert_vector(string_vector):
    unsigned_vector = string_vector[1:8]
    if int(string_vector[0]) == 0:
        return float(unsigned_vector) / 1000
    else:
        return -1 * float(unsigned_vector) / 1000


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
    list_in[0] = __convert_lat_long(list_in[0]) #Converting string value to float value
    list_in[1] = __convert_lat_long(list_in[1]) #Converting string value to float value
    list_in[2] = int(list_in[2]) #Converting string value to integer value
    radius = 6371000 + list_in[2]
    x = radius * math.cos(math.degrees(list_in[0])) * math.cos(math.degrees(list_in[1]))
    y = radius * math.cos(math.degrees(list_in[0])) * math.sin(math.degrees(list_in[1]))
    z = radius * math.sin(math.degrees(list_in[1]))
    return [x, y, z]


def find_highest_priority_s(collision_list):
    """
    Finds the plane or planes, when applicable, with the highest priority and returns them as list to the caller.

    :param
    :return: list of length two:
                attribute 1 will be:
                    Plane or planes (up to two), with the highest priority
                attribute 2 will be:
                    HIGH - if high priority
                    MEDIUM - if medium priority
                    LOW - if low priority
                    LOWEST - if farther than 10 minutes away
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
    return __find_priority(priority_list)


def __find_priority(priority_list):
    if len(priority_list) == 0:
        return [priority_list, "DO NOTHING"]
    elif len(priority_list) == 1:
        if not (priority_list[0] == "LOWEST"):
            return [priority_list, __get_priority(priority_list[0])]
        else:
            return [priority_list, "DO NOTHING"]
    elif __get_priority(priority_list[0]) == __get_priority(priority_list[1]):
        if not (priority_list[0] == "LOWEST"):
            return [priority_list, __get_priority(priority_list[0])]
        else:
            return [priority_list, "DO NOTHING"]
    else:
        if __get_priority(priority_list[0]) == "HIGH" or __get_priority(priority_list[1]) == "HIGH":
            if __get_priority(priority_list[0]) == "HIGH":
                return [[priority_list[0]], __get_priority(priority_list[0])]
            else:
                return [[priority_list[1]], __get_priority(priority_list[1])]
        elif __get_priority(priority_list[0]) == "MEDIUM" or __get_priority(priority_list[1]) == "MEDIUM":
            if __get_priority(priority_list[0]) == "MEDIUM":
                return [[priority_list[0]], __get_priority(priority_list[0])]
            else:
                return [[priority_list[1]], __get_priority(priority_list[1])]
        elif __get_priority(priority_list[0]) == "LOW" or __get_priority(priority_list[1]) == "LOW":
            if __get_priority(priority_list[0]) == "LOW":
                return [[priority_list[0]], __get_priority(priority_list[0])]
            else:
                return [[priority_list[1]], __get_priority(priority_list[1])]
    return [priority_list, "DO NOTHING"]



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


def update_plane_list(plane):
    """
    Adds or updates the plane to the nearby_plane_list

    :param plane:
    :return:
    """
    if plane.id_code == primary_aircraft.id_code:
        primary_aircraft.update_plane(plane.location_vector,plane.velocity_vector,plane.elevation)

    else:
        updated_or_not = False
        for i in nearby_planes_list:
            if plane.id_code == i.id_code:
                updated_or_not = True
                i.update_plane(plane.location_vector,plane.velocity_vector,plane.elevation)
                i.update_time = clock()
        if not(updated_or_not):
            nearby_planes_list.append(plane)




    # pass


def dispatch_collision_alerts(lookup_list):
    """

    :return:
    """
    audio = Audio()
    audio.audio_alert(__collision_alerts[lookup_list[0]][lookup_list[1]])



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


    # print "Elv: " + str(primary_aircraft.elevation)
    # print "lox y: " + str(primary_aircraft.location_vector[1])
    # print "vect z:: " + str(primary_aircraft.velocity_vector[2])


    if len(priority_list) == 0:
        return "DO NOTHING"
    elif len(priority_list) == 1:
        if (__compare_planes(primary_aircraft, priority_list[0])) == 1:
            return "CLIMB"
        else:
            return "DESCEND"
    elif len(priority_list) == 2:
        result_intruder1 = __compare_planes(primary_aircraft, priority_list[0])
        result_intruder2 = __compare_planes(primary_aircraft, priority_list[1])
        result = result_intruder1 + result_intruder2
        #if = 2 then the PA needs to go above both the planes
        if result == 2:
            return "CLIMB"
        #else if result is equal to 0 then the PA should maintain its elevation and not move
        elif result == 0:
            return "MAINTAIN"
        #else if the result is = -2 then the PA should descend
        elif result == -2:
            return "DESCEND"
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
    primary_aircraft.id_code = int(new_code)



