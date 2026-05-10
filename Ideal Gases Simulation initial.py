import math
import random
import numpy as np
import matplotlib.pyplot as plt

import matplotlib
matplotlib.use('TkAgg')
#Constants
num_particles = int(input("Enter the no. of gas molecules: ")
container_size = 0.1
time_steps = 10000
particles_speed = 0.001

# Initial positions and velocities of each particles
positions = np.random.rand(num_particles, 2)*container_size
velocities = np.random.rand(num_particles, 2)*particles_speed

#Creating a plot
fig, ax = plt.subplots()
scatter = ax.scatter(positions[:, 0], positions[:, 1], marker='o')
ax.set_xlim(0, container_size)
ax.set_ylim(0, container_size)
plt.gca().set_aspect('equal', adjustable = 'box')


#Simulation Loop
"""
at t = t, p(t,0) = p(t-1,0) + v(1,0)
"""
collision_array = []
for step in range(time_steps):
    positions += velocities
    no_of_collisions = 0
    
    for i in range(num_particles):
        for j in range(2):
            if positions[i,j] < 0 or positions[i,j] > container_size:
                #collision with wall, velocity bevomes orthogonal
                velocities[i,j] *= -1
                no_of_collisions += 1
    collision_array = np.append(collision_array, no_of_collisions)           
    
    print(f"No. of collisions = {no_of_collisions}   Average no. of collisions = {np.average(collision_array)}", end = "\r")

    scatter.set_offsets(positions)
    plt.pause(0.001)

    if not plt.fignum_exists(fig.number):
        break

plt.show()      

