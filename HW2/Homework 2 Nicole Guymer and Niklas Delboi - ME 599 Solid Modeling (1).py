#!/usr/bin/env python

#Nicole Guymer and Niklas Delboi
#ME 599: Solid Modeling
#Homework 2
#1/30/2019

"""Homework 2: Read in the bug file, display it graphically, and calculate the surface area and the volume of the bug.
Next, transform the bug by rotating it 45 degrees about the vector [1,1,1] and scale the end result by 2.
Finally, display this new bug and find its surface area and volume."""

%matplotlib inline
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot
from numpy.linalg import norm
import math as m
import numpy as np

# Create a new plot
figure = pyplot.figure()
axes = mplot3d.Axes3D(figure)

# Load the STL files and add the vectors to the plot
your_mesh = mesh.Mesh.from_file('bug.stl')
axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))
axes.set_xlabel('$X$')
axes.set_ylabel('$Y$')
axes.set_zlabel('$Z$')
axes.set_title('Initial Bug')

# Auto scale to the mesh size
scale = your_mesh.points.flatten(-1)
axes.auto_scale_xyz(scale, scale, scale)

# Get the vertices of the fugure
v0 = your_mesh.data['vectors'][:,0] 	# 1st vertex of each triangle
v1 = your_mesh.data['vectors'][:,1] 	# 2nd vertex of each triangle
v2 = your_mesh.data['vectors'][:,2] 	# 3rd vertex of each triangle

# Get the surface area and the volume for stl file
norms = np.cross(v1-v0, v2-v0)			# cross product of two triangle´s edges (normal vector)
surface_total = 0
volume_total = 0

for i in range(len(norms)):
	surface_triangle = norm(norms[i])/2
	surface_total = surface_total+surface_triangle

	partial_volume = np.dot(v0[i],norms[i])/6
	volume_total = volume_total+partial_volume

# Print the required parameters
print("Initial Surface Area = {0}".format(surface_total))
print("Initial Volume       = {0}".format(volume_total))

# Arbitrary rotation and scaling
# 1. Define the axis of rotation and the angle
a = [1,1,1]
theta = m.radians(45)						# define the angle for the rotation in radian (theta = 45 degrees)

# 2. Calculate the matrix for rotation R
mag = norm(a) 								# calculates the magnitude of a
a_norm = [a[0]/mag, a[1]/mag, a[2]/mag]		# calculate the unit vector of a
R = [[(1-m.cos(theta))*a_norm[0]**2+m.cos(theta), (1-m.cos(theta))*a_norm[0]*a_norm[1]-a_norm[2]*m.sin(theta), (1-m.cos(theta))*a_norm[0]*a_norm[2]+a_norm[1]*m.sin(theta)],
	[(1-m.cos(theta))*a_norm[0]*a_norm[1]+a_norm[2]*m.sin(theta), (1-m.cos(theta))*a_norm[1]**2+m.cos(theta), (1-m.cos(theta))*a_norm[1]*a_norm[2]-a_norm[0]*m.sin(theta)],
	[(1-m.cos(theta))*a_norm[0]*a_norm[2]-a_norm[1]*m.sin(theta), (1-m.cos(theta))*a_norm[1]*a_norm[2]+a_norm[0]*m.sin(theta), (1-m.cos(theta))*a_norm[2]**2+m.cos(theta)]]

# 3. Transpose the vertex vectors for multiplication with R
v0_transpose = np.transpose(v0)
v1_transpose = np.transpose(v1)
v2_transpose = np.transpose(v2)

# 4. Get the new points after rotation by multiplication of R and the vertices
v0_prime = np.matmul(R,v0_transpose)
v1_prime = np.matmul(R,v1_transpose)
v2_prime = np.matmul(R,v2_transpose)

# 5. Scale all vertices by 2
v0_prime = v0_prime*2
v1_prime = v1_prime*2
v2_prime = v2_prime*2

# 6. Transpose back for plotting
v0_prime = np.transpose(v0_prime)
v1_prime = np.transpose(v1_prime)
v2_prime = np.transpose(v2_prime)

mesh_new =[]
for i in range(len(v0_prime)):
	mesh_new.append([v0_prime[i], v1_prime[i], v2_prime[i]])

figure = pyplot.figure()
axes = mplot3d.Axes3D(figure)
axes.add_collection3d(mplot3d.art3d.Poly3DCollection(mesh_new))
axes.set_xlim([-0.006,0.006])
axes.set_ylim([-0.006,0.006])
axes.set_zlim([-0.006,0.006])
axes.set_xlabel('$X$')
axes.set_ylabel('$Y$')
axes.set_zlabel('$Z$')
axes.set_title('New Bug')
pyplot.show()

# Get the surface area and the volume for the new figure
norms = np.cross(v1_prime-v0_prime, v2_prime-v0_prime)		# cross product of two triangle´s edges (normal vector)
surface_total_new = 0
volume_total_new = 0

for i in range(len(norms)):
	surface_triangle = norm(norms[i])/2
	surface_total_new = surface_total_new+surface_triangle

	partial_volume = np.dot(v0_prime[i],norms[i])/6
	volume_total_new = volume_total_new+partial_volume

# Print the required parameters
print("New Surface Area = {0}".format(surface_total_new))
print("New Volume       = {0}".format(volume_total_new))