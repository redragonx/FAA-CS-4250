__author__ = 'Dean'

import math


def from_c_t_c1_back(**c_t_c_set):
    z = c_t_c_set.get("z")
    y = c_t_c_set.get("y")
    x = c_t_c_set.get("x")
    R = calculate_r(x, y, z)
    lat = math.degrees(math.asin(z / R))
    long = math.degrees(math.atan2(y, x))
    lat = int(round(lat,6) * 1000000)
    long = int(round(long,6) * 1000000)

    if lat < 0:
        str_lat = "1" + prepend_zero(str(abs(lat)), 9-len(str(abs(lat))))
    elif lat >= 0:
        str_lat = "0" + prepend_zero(str(abs(lat)), 9-len(str(abs(lat))))


    if long < 0:
        str_long = "1" + prepend_zero(str(abs(long)), 9-len(str(abs(long))))
    elif long >= 0:
        str_long= "0" + prepend_zero(str(abs(long)), 9-len(str(abs(long))))

    # print("*"*20)
    # print "R:", (R-6371000)
    # print "lat: " + str_lat
    # print "lon: " + str_long
    # print [str_lat, str_long, prepend_zero((int(R-6371000)), (6-len(str(abs(int(R-6371000))))))]
    return [str_lat, str_long, prepend_zero((int(R-6371000)), (6-len(str(abs(int(R-6371000))))))]


def build_number_system(id_code, list_in, x, y, z):
    return id_code + list_in[0] + list_in[1] + list_in[2] + convert_vector(x) + convert_vector(y) + convert_vector(z)


def convert_vector(vec_int):
    vec_int = int(round(vec_int, 3)*1000)
    str_int = str(prepend_zero(abs(vec_int), (7-len(str(abs(vec_int))))))
    if vec_int < 0:
        str_int = "1" + str_int
    elif vec_int >= 0:
        str_int = "0" + str_int
    return str_int


def prepend_zero(str_lat, num_zero):
    for i in range(0, num_zero):
        str_lat = str(0) + str(str_lat)
    return str_lat


def calculate_r(x,y,z):
    return math.sqrt(x**2 + y**2 + z**2)

# print convert_vector(100)
# print convert_vector(-100.2377)
print "PA"
# print len(build_number_system("0001", from_c_t_c1_back(x=0, y=0, z=6391000), 0, 0, 0))
print(build_number_system("0001", from_c_t_c1_back(x=0, y=0, z=6391000), 0, 0, 0))
# print "*"*20
# print len(build_number_system("0002", from_c_t_c1_back(x=5000, y=0, z=6391000), 100, 0, 0))
print(build_number_system("0002", from_c_t_c1_back(x=5000, y=0, z=6391000), 100, 0, 0))
# print "*"*20
# print len(build_number_system("0003", from_c_t_c1_back(x=6000, y=0, z=6391000), 100, 0, 0))
print(build_number_system("0003", from_c_t_c1_back(x=6000, y=0, z=6391000), 100, 0, 0))
# print "*"*20
# print len(build_number_system("0004", from_c_t_c1_back(x=7000, y=0, z=6391000), 100, 0, 0))
print(build_number_system("0004", from_c_t_c1_back(x=7000, y=0, z=6391000), 100, 0, 0))
# print "*"*20
# print len(build_number_system("0005", from_c_t_c1_back(x=8000, y=0, z=6391000), 100, 0, 0))
print(build_number_system("0005", from_c_t_c1_back(x=8000, y=0, z=6391000), 100, 0, 0))
# print "*"*20
# print len(build_number_system("0006", from_c_t_c1_back(x=9000, y=0, z=6391000), 100, 0, 0))
print(build_number_system("0006", from_c_t_c1_back(x=9000, y=0, z=6391000), 100, 0, 0))
# print "*"*20
# print len(build_number_system("0007", from_c_t_c1_back(x=-6000, y=0, z=6391000), -100, 0, 0))
print(build_number_system("0007", from_c_t_c1_back(x=-6000, y=0, z=6391000), -100, 0, 0))
# print "*"*20
# print len(build_number_system("0008", from_c_t_c1_back(x=-7000, y=0, z=6391000), -100, 0, 0))
print(build_number_system("0008", from_c_t_c1_back(x=-7000, y=0, z=6391000), -100, 0, 0))
# print "*"*20
# print len(build_number_system("0009", from_c_t_c1_back(x=-8000, y=0, z=6391000), -100, 0, 0))
print(build_number_system("0009", from_c_t_c1_back(x=-8000, y=0, z=6391000), -100, 0, 0))
# print "*"*20
# print len(build_number_system("0010", from_c_t_c1_back(x=500, y=500, z=(6391000-500)), -10, -10, 10))
print(build_number_system("0010", from_c_t_c1_back(x=500, y=500, z=(6391000-500)), -10, -10, 10))


# from_c_t_c1_back(x=, y=,z=)
# from_c_t_c1_back(x=, y=,z=)
# from_c_t_c1_back(x=, y=,z=)
