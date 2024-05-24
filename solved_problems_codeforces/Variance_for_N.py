import numpy as np


def pi_estimation(points):
    rand = np.random.uniform(-1, 1, 2 * points)
    rand_points = rand.reshape(points, 2)
    norm_points = rand_points[:, 0] ** 2 + rand_points[:, 1] ** 2
    points_inside = rand_points[norm_points < 1]
    pi_approx = 4 * len(points_inside) / points


    return pi_approx



repeats = 10
def repeat_estimation(points, repeats):
    pi_estimates = []
    for i in range(repeats):
        pi_estimates.append(pi_estimation(points))
    return pi_estimates

def calculate_variance(pi_estimates):
    return np.var(pi_estimates)

# Define the range of points (N) and repetitions
points_range = [10, 100, 1000, 10000]  # Different values of N
repeats = 100

results = []
for points in points_range:
    pi_estimates = repeat_estimation(points, repeats)
    variance = calculate_variance(pi_estimates)
    results.append((points, variance))
print(results)



