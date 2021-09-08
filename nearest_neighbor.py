import math


def find_nearest_neighbor(unknown_tuple, dataset_red, dataset_blue):
    dataset_color = "white"
    nearest_tuple = (math.inf, math.inf)
    smallest_distance = math.inf

    for item in dataset_red:
        distance = find_distance(unknown_tuple, item)
        if distance < smallest_distance:
            nearest_tuple = item
            smallest_distance = distance
            dataset_color = "red"

    for item in dataset_blue:
        distance = find_distance(unknown_tuple, item)
        if distance < smallest_distance:
            nearest_tuple = item
            smallest_distance = distance
            dataset_color = "blue"

    return [nearest_tuple, dataset_color]


def find_distance(point_a, point_b):
    distance = math.sqrt(
        (float(point_b[0]) - float(point_a[0])) ** 2 +
        (float(point_b[1]) - float(point_a[1])) ** 2)
    return distance
