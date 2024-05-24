import numpy as np
import matplotlib.pyplot as plt

def estimate_pi(points):
    rand = np.random.uniform(-1, 1, 2 * points)
    rand_points = rand.reshape(points, 2)
    norm_points = rand_points[:, 0] ** 2 + rand_points[:, 1] ** 2
    points_inside = rand_points[norm_points < 1]
    pi_approx = 4 * len(points_inside) / points
    return pi_approx

def repeat_estimation(points, repeats):
    pi_estimates = []
    for _ in range(repeats):
        pi_estimates.append(estimate_pi(points))
    return pi_estimates

def calculate_variance(pi_estimates):
    return np.var(pi_estimates)

# Define the range of points (N) and repetitions
points_range = np.logspace(2, 6, num=30, dtype=int)  # generating 30 logarithmically spaced array of points
repeats = 10

variances = []
for points in points_range:
    pi_estimates = repeat_estimation(points, repeats)
    variance = calculate_variance(pi_estimates)
    variances.append(variance)

# Plotting the variance of the error versus N on a log-log scale
plt.figure()
plt.loglog(points_range, variances, marker='o', linestyle='-')
plt.xlabel('Number of Points (N)')
plt.ylabel('Variance of Error')
plt.title('Variance of Error versus Number of Points (N)')
plt.grid(True)
plt.show()