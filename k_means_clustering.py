from nearest_neighbor import find_distance


def generate_random_centroids(num_of_centroids):
    print("okay")


def find_closest_cluster_center(dataset, centroids):
    for point in dataset:
        distance = float("inf")
        closest_center = float("inf")
        for center in centroids:
            local_distance = find_distance(point, center)
            if local_distance < distance:
                distance = local_distance
                closest_center = center
        print("point:", point, "center:", closest_center, "distance:", distance)
