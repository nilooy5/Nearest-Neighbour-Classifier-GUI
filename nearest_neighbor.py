import math


def find_nearest_neighbor(unknown_tuple, given_dataset):
    nearest_tuple = (math.inf, math.inf)
    smallest_distance = math.inf
    for item in given_dataset:
        distance = find_distance(unknown_tuple, item)
        if distance < smallest_distance:
            nearest_tuple = item
            smallest_distance = distance
    # print(smallest_distance)
    # print(nearest_tuple)
    return nearest_tuple


def find_distance(point_a, point_b):
    distance = math.sqrt(
        (float(point_b[0])-float(point_a[0]))**2 +
        (float(point_b[1])-float(point_a[1]))**2)
    return distance
