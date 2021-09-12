result = []


def find_nearest_neighbor(dataset_unknown, dataset_red, dataset_blue):
    for item in dataset_unknown:
        result.append(find_nearest_neighbor_for_point(item, dataset_red, dataset_blue))
    return result


def find_nearest_neighbor_for_point(unknown_tuple, dataset_red, dataset_blue):
    dataset_color = "white"
    nearest_tuple = (float("inf"), float("inf"))
    smallest_distance = float("inf")

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
    difference_squared_sum = 0
    for i in range(len(point_a)):
        difference_squared_sum += ((float(point_b[i]) - float(point_a[i])) ** 2)

    distance = (difference_squared_sum ** 0.5)
    return distance


def generate_neighborhood_dataset(dataset_unknown, nearest_dataset):
    result_dataset = []
    for i in range(len(dataset_unknown)):
        result_dataset.append([dataset_unknown[i], nearest_dataset[i][1]])

    return result_dataset
