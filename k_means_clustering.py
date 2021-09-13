from nearest_neighbor import find_distance


def generate_random_centroids(num_of_centroids):
    print("okay")


def find_closest_cluster_center_list(dataset, centroids):
    cluster_center_dataset = []

    for point in dataset:
        smallest_distance = float("inf")
        closest_center = float("inf")
        for center in centroids:
            distance = find_distance(point, center)
            if distance < smallest_distance:
                smallest_distance = distance
                closest_center = center

        cluster_center_dataset.append([point, closest_center, smallest_distance])

    get_average_centroid(cluster_center_dataset)

    return cluster_center_dataset


def get_average_centroid(dataset):
    sum_list = [0, 0]
    average_list = []

    cluster_dictionary = generate_cluster_dictionary(dataset)
    for item in cluster_dictionary:
        print(cluster_dictionary[item])

    # data points are always stored in [i][0]
    for i in range(len(dataset[0][0])):
        for item in dataset:
            # print(item)
            sum_list[i] += float(item[0][i])
            # print("row", i, item[0][i])

    # print(sum_list)
    for i in range(len(sum_list)):
        average_list.append(sum_list[i]/len(dataset))

    # print(average_list)


def generate_cluster_dictionary(dataset_with_centers):
    centroid_dict = {}
    for item in dataset_with_centers:
        if item[-2] not in centroid_dict:
            centroid_dict[item[-2]] = item[:-2]
        else:
            centroid_dict[item[-2]].extend(item[:-2])

    return centroid_dict
