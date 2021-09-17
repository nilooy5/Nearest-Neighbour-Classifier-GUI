from nearest_neighbor import find_distance


def generate_random_centroids(num_of_centroids):
    print("okay")


def find_cluster_for_random_center(dataset, centroids):
    cluster_center_with_distance = []

    for point in dataset:
        smallest_distance = float("inf")
        closest_center = float("inf")
        for center in centroids:
            distance = find_distance(point, center)
            if distance < smallest_distance:
                smallest_distance = distance
                closest_center = center

        cluster_center_with_distance.append([point, closest_center, smallest_distance])

    get_average_centroid(cluster_center_with_distance)

    return cluster_center_with_distance


def get_average_centroid(cluster_center_with_distance):
    sum_list = [0, 0]
    average_list = []
    prev_to_new_centroids_list = []

    cluster_dictionary = generate_cluster_dictionary(cluster_center_with_distance)
    for item in cluster_dictionary:
        prev_to_new_centroids_list.append(generate_average_center_for_class(cluster_dictionary[item], item))

    decide_to_change_cluster(prev_to_new_centroids_list, cluster_center_with_distance)

    # data points are always stored in [i][0]
    for i in range(len(cluster_center_with_distance[0][0])):
        for item in cluster_center_with_distance:
            # print(item)
            sum_list[i] += float(item[0][i])
            # print("row", i, item[0][i])

    # print(sum_list)
    for i in range(len(sum_list)):
        average_list.append(sum_list[i] / len(cluster_center_with_distance))

    # print(average_list)


def generate_cluster_dictionary(dataset_with_centers):
    centroid_dict = {}
    for item in dataset_with_centers:
        if item[-2] not in centroid_dict:
            centroid_dict[item[-2]] = item[:-2]
        else:
            centroid_dict[item[-2]].extend(item[:-2])

    return centroid_dict


def generate_average_center_for_class(cluster_points, cluster_name):
    average_centers = []
    print("length:", len(cluster_points), cluster_points)
    for i in range(len(cluster_points[0])):
        sum_for_x_coordinate = 0
        for item in cluster_points:
            print("coord", i, ":", item[i])
            sum_for_x_coordinate += float(item[i])

        average_centers.append(sum_for_x_coordinate/len(cluster_points))

    print("average for", cluster_name, "cluster's data-points:", average_centers, "length:", len(cluster_points))
    return [cluster_name, tuple(average_centers)]

#     now calculate distance between cluster_name and tuple(average_centers)


def decide_to_change_cluster(points_pair_list, dataset):
    distance = 0
    for points_pair in points_pair_list:
        distance += find_distance(points_pair[0], points_pair[1])

    print("total:", distance)
    print(dataset[0])
