import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameters for the 5D manifold
n_points = 20  # Reduced number of points for demonstration
x = np.linspace(-5, 5, n_points)  # Spatial x
y = np.linspace(-5, 5, n_points)  # Spatial y
z = np.linspace(-5, 5, n_points)  # Spatial z
t = np.linspace(0, 10, n_points)  # Physical time (4th dimension)
tau = np.linspace(0, 5, n_points)  # Conscious observer time (5th dimension)

# Create a grid for the 4D spacetime (x, y, z, t)
X, Y, Z, T = np.meshgrid(x, y, z, t, indexing='ij')

# Define the 5th dimension (tau) as a function of the 4D spacetime
def compute_tau(x_val, y_val, z_val, t_val):
    distance = np.sqrt(x_val**2 + y_val**2 + z_val**2)
    base_tau = t_val * 0.5  # Scales with physical time
    perturbation = np.sin(distance) * 0.1  # Variation based on position
    return base_tau + perturbation

# Compute tau for the entire grid (using vectorized operations if possible)
tau_values = np.zeros_like(X)
for i in range(n_points):
    for j in range(n_points):
        for k in range(n_points):
            for l in range(n_points):
                tau_values[i, j, k, l] = compute_tau(X[i, j, k, l], Y[i, j, k, l], Z[i, j, k, l], T[i, j, k, l])

# For visualization, project the 5D manifold into 3D:
# We'll fix z=0 and t=5 (choose the index closest to these values)
z_index = n_points // 2  # roughly 0
t_index = n_points // 2  # roughly t=5

# Extract the slice
X_slice = X[:, :, z_index, t_index]
Y_slice = Y[:, :, z_index, t_index]
tau_slice = tau_values[:, :, z_index, t_index]

# Create a 3D scatter plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(X_slice.flatten(), Y_slice.flatten(), tau_slice.flatten(),
                     c=tau_slice.flatten(), cmap='viridis', s=50)
plt.colorbar(scatter, label='Conscious Observer Time (τ)')
ax.set_xlabel('X (Spatial)')
ax.set_ylabel('Y (Spatial)')
ax.set_zlabel('Conscious Observer Time (τ)')
ax.set_title('Projection of 5D Manifold (N-Frame Framework) into 3D')
plt.show()-- run this code 