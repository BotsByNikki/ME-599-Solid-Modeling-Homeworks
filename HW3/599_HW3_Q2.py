#!/usr/bin/env python

#Nicole Guymer and Niklas Delboi
#ME 599: Solid Modeling
#Homework 3
#2/10/2019

"""Homework Problem 2: Given a convex polygon and a single scalar delta, offset the polygon. 
Delta can be positive or negative.
Corners should be extended (no miter or rounding)."""

"""Subquestion 1: Is the resulting shape the same as if you scaled it with
a homogeneous transform?

Answer: No, it is not. The scaling refers to the origin. So, the polygon's center moves. For the offset, the center remains at its previous
position (see the plot at the end of that program)."""

"""Subquestion 2: What happens to the resulting shape if a large negative
delta is provided? What does the polygon become?

Answer: Large negative deltas lead to another shape of the offsetted polygon. Each edge of the given polygon is offsetted on the other
side of the polygon. That happens with each edge."""

#%matplotlib inline
from io import StringIO
import matplotlib.pyplot as plt
import numpy as np
import shapely.geometry as shp


def PolyOffset(points, offset, scaling):

	# Create a Polygon from the given points
	OGpoly = shp.Polygon(points)


	# Get all the vertices of the offset polygon
	# Define the sizes of some variables that are used in the for loop
	edges = np.zeros((len(points),2))				# Edges of the given polygon
	normals = np.zeros((len(points),2))				# normal vectors to each edge
	unit_normals = np.zeros((len(points),2))		# unit normal vectors
	midpoints = np.zeros((len(points),2))			# midpoint of each edge
	midpoints_offset = np.zeros((len(points),2))	# midpoint of the offset polygon´s edges
	vert_offset = np.zeros((len(points),2))			# vertices of the offset polygon

	for i in range(len(points)-1):
		edges[i] = np.subtract(points[i+1],points[i])
		normals[i] = (edges[i,1],-edges[i,0])
		mag2 = np.sqrt(normals[i,0]**2+normals[i,1]**2)
		unit_normals[i] = normals[i]/mag2
		midpoints[i] = points[i]+0.5*edges[i]						# find the midpoint by the half length of each edge
		midpoints_offset[i] = midpoints[i]+offset*unit_normals[i] 	# get the offset midpoints with the offset as a scalar (delta) and the unit normal vectors

	# Do all the same steps for the last edge from the "last point" to the "first point" of the given polygon
	edges[len(points)-1] = np.subtract(points[0],points[len(points)-1])
	normals[len(points)-1] = (edges[len(points)-1,1],-edges[len(points)-1,0])
	mag2 = np.sqrt(normals[len(points)-1,0]**2+normals[len(points)-1,1]**2)
	unit_normals[len(points)-1] = normals[len(points)-1]/mag2
	midpoints[len(points)-1] = points[len(points)-1]+0.5*edges[len(points)-1]
	midpoints_offset[len(points)-1] = midpoints[len(points)-1]+offset*unit_normals[len(points)-1] 

	# Get the value for "t1" which discribes the scalar for the intersection between two neighbored edges of the offset polygon
	# Use Cramer´s rule to find those
	for i in range(len(points)-1):
		A1 = np.array([np.subtract(midpoints_offset[i+1],midpoints_offset[i]),-edges[i+1]])
		A = np.array([edges[i],-edges[i+1]])
		t1 = np.linalg.det(A1)/np.linalg.det(A)
		
		vert_offset[i] = midpoints_offset[i]+t1*edges[i]	# Get the vertices of the offset polygon with t1 
	
	# Do the same steps in the previous loop for the last edge from the "last point" to the "first point" of the offset polygon
	A1 = np.array([np.subtract(midpoints_offset[0],midpoints_offset[len(points)-1]),-edges[0]])
	A = np.array([edges[len(points)-1],-edges[0]])
	t1 = np.linalg.det(A1)/np.linalg.det(A)

	vert_offset[len(points)-1] = midpoints_offset[len(points)-1]+t1*edges[len(points)-1] # Get the last vertex of the offsetted polygon with t1 

	# For comparison with a scaled polygon define a transformation matrix T
	T = ([scaling,0],[0,scaling])
	vert_trans = np.zeros((len(points),2))		# define a matrix for the vertices that are calculated in the following loop

	# Get the transformed vertices by multiplication between the transformation matrix and the vertices of the given polygon
	for i in range(len(points)):
		vert_trans[i] = np.matmul(T,points[i])

	# Define the new polygons
	OffsetPoly = shp.Polygon(vert_offset)
	TransformPoly = shp.Polygon(vert_trans)

	# Turn polygon points into numpy arrays for plotting
	OGpolypts = np.array(OGpoly.exterior)
	OffsetPolypts = np.array(OffsetPoly.exterior)
	TransformPolypts = np.array(TransformPoly.exterior)

	# Plot points
	plt.plot(*OGpolypts.T,'--', color='g', label='Original Polygon')
	plt.plot(*OffsetPolypts.T, color='red', label='Offset Polygon')
	#plt.plot(*TransformPolypts.T, color='blue', label='Scaled Polygon')
	plt.axis('equal')
	plt.legend()
	plt.title('Question 2: Offset Convex Polygon')
	plt.xlabel('X')
	plt.ylabel('Y')
	plt.show()

if __name__ == '__main__':
	a = ([5,1],[5,3],[3,3],[3,5],[1,3])
	offset = 1.25
	scaling = 1.25
	PolyOffset(a,offset,scaling)