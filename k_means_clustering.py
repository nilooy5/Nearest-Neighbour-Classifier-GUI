from nearest_neighbor import find_distance

threshold = 0.1
final_cluster = []


# acts as an entry point for dataset and given centroids
def find_cluster_for_random_center(dataset, centroids):
    cluster_center_with_distance = generate_cluster_center_with_distance(dataset, centroids)

    get_average_centroid(cluster_center_with_distance, dataset)

    return final_cluster


# takes:    a list with the dataset and centroids
# returns:  dataset with all points, it's closest centroid and distance between them
def generate_cluster_center_with_distance(dataset, centroids):
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

    return cluster_center_with_distance


# takes:        the list generated in generate_cluster_center_with_distance
# generates:    a dictionary where keys are the tuple of the centroids by calling generate_cluster_dictionary
#               a list with previous centroids and new centroids
# calls:        the generate_cluster_dictionary and then sends the whole dataset, previous to
#               new centroid list and cluster dictionary to generate_cluster_dictionary
def get_average_centroid(cluster_center_with_distance, dataset):
    prev_to_new_centroids_list = []

    cluster_dictionary = generate_cluster_dictionary(cluster_center_with_distance)
    for item in cluster_dictionary:
        prev_to_new_centroids_list.append(generate_average_center_for_class(cluster_dictionary[item], item))

    decide_to_change_cluster(prev_to_new_centroids_list, dataset, cluster_dictionary)


# takes:    the list with centroids with distances between all points of the dataset
# returns:  the dictionary where centroids are the keys and their list of cluster points are the values
def generate_cluster_dictionary(dataset_with_centers):
    centroid_dict = {}
    for item in dataset_with_centers:
        if item[-2] not in centroid_dict:
            centroid_dict[item[-2]] = item[:-2]
        else:
            centroid_dict[item[-2]].extend(item[:-2])

    return centroid_dict


# takes:        a cluster's member (cluster_points) list and its value (cluster_name)
# generates:    average center of a cluster
# returns:      the cluster center tuple & new average of the cluster as a list
def generate_average_center_for_class(cluster_points, cluster_name):
    average_centers = []
    # print("length:", len(cluster_points), cluster_points)
    for i in range(len(cluster_points[0])):
        sum_for_x_coordinate = 0
        for item in cluster_points:
            # print("coord", i, ":", item[i])
            sum_for_x_coordinate += float(item[i])

        average_centers.append(sum_for_x_coordinate / len(cluster_points))

    # print("average for", cluster_name, "cluster's data-points:", average_centers, "length:", len(cluster_points))

    return [cluster_name, tuple(average_centers)]


# takes:    the whole dataset, pair of previous & new average centroids and the dictionary with clusters
# checks:   the sum of distances between previous & new centroids (distance). If sum of distance > threshold
#           it again starts from the beginning with new centroids we found after averaging
#           else it stores the new cluster dictionary to the final_cluster
#           finally, the looping function call that started from get_average_centroid in find_cluster_for_random_center
#           stops and returns final_cluster with resultant data in the main function where it was first called
def decide_to_change_cluster(points_pair_list, dataset, cluster_dictionary):
    distance = 0
    old_points = []
    new_points = []
    for points_pair in points_pair_list:
        old_points.append(points_pair[0])
        new_points.append(points_pair[1])
        distance += find_distance(points_pair[0], points_pair[1])

    # print("old:", old_points)
    # print("new:", new_points)
    # print("total:", distance)
    if distance > threshold:
        find_cluster_for_random_center(dataset, new_points)
    else:
        final_cluster.append(cluster_dictionary)
