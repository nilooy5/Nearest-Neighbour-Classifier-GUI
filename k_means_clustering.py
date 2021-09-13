from nearest_neighbor import find_distance


def generate_random_centroids(num_of_centroids):
    print("okay")


def find_closest_cluster_center(dataset, centroids):
    cluster_center_dataset = []

    for point in dataset:
        smallest_distance = float("inf")
        closest_center = float("inf")
        for center in centroids:
            distance = find_distance(point, center)
            if distance < smallest_distance:
                smallest_distance = distance
                closest_center = center
                print(closest_center)

        cluster_center_dataset.append([point, closest_center, smallest_distance])
    return cluster_center_dataset
