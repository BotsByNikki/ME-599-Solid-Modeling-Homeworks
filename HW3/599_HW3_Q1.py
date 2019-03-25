#!/usr/bin/env python

#Nicole Guymer and Niklas Delboi
#ME 599: Solid Modeling
#Homework 3
#2/10/2019

"""Homework Problem 1: Wright a function that returns 'inside' or 'outside' 
for whether a point is inside or outside a polygon. This polygon can be simple
or complex. 2D problem. """
"""The algorithm is from Janke´s example on page 432ff of the textbook."""

%matplotlib inline
from io import StringIO
import matplotlib.pyplot as plt
import numpy as np
import shapely.geometry as shp

def InOrOut(points, point):

	# Create a Polygon from the given points
	OGpoly = shp.Polygon(points)

	# Turn polygon points into numpy arrays for plotting
	OGpolypts = np.array(OGpoly.exterior)

	# Check if point is inside or outside
	# Define any direction vector for the ray 
	d = ([0,-1]) 				# use an easy one like Janke did

	# Get the unit normal vector which is rotated about d by 90 degrees (clockwise)
	n = ([-1,0])
	
	# Reshape the matrix with vertices in their x and y values to calculate the differences to point P. Those are needed to calculate
	# the dot product with the normal vector to check for intersections
	vert_reshape = np.reshape(vert,(len(vert),2))
	vertx = vert_reshape[:,0]					# x-values of all vertices
	verty = vert_reshape[:,1]					# y-values of all vertices

	Pvert_x = np.subtract(vertx,P[0])			# x-values of the vector from P to the vertices 
	Pvert_y = np.subtract(verty,P[1])			# y-values of the vector from P to the vertices

	# Define the sizes of some variables for the loop. After that, calculate all the dot products between the vectors from P to the
	# vertices and the normal vector
	Pvert = np.zeros((len(vert),2))
	dot_Pn = np.zeros(len(vert))
	edges = np.zeros((len(vert),2))		# edges of the polygon

	for i in range(len(vert)):
		Pvert[i] = [Pvert_x[i],Pvert_y[i]]
		dot_Pn[i] = np.dot(Pvert[i],n)

	for i in range(len(vert)-1):
		edges[i] = np.subtract(vert[i+1],vert[i])		

	edges[len(vert)-1] = np.subtract(vert[0],vert[len(vert)-1])		# Edge between the "last" and the "first point" of the polygon

	# In the following for-loop, there are 3 different if-statements. The first one shows if two neighbored vertices of the polygon, 
	# defined by i and i+1, are on opposite sides of the ray. That would confirm an intersection! The second if statement filters out
	# all those edges of the polygon that are behind the point P (not in the direction of the ray). That can be checked with either
	# both dot-products are negative or the scalar "t1" becomes negative (Get "t1" with Cramer´s rule).The last statement asks for the
	# sign that indicates an intection from right-to-left (-1) or from left-to-right (+1). 
	# "sum" stores all the values (+1 or -1) for the intersections. Start with sum = 0
	sum = 0

	for i in range(len(vert)-1):
		if dot_Pn[i]*dot_Pn[i+1]<=0:
			if np.dot(np.subtract(vert[i],P),d)>=0 and np.dot(np.subtract(vert[i+1],P),d)>=0:
				if np.dot(edges[i],n)<0:
					sum = sum-1
				else:
					sum = sum+1
			elif (np.dot(np.subtract(vert[i],P),d)<0 and np.dot(np.subtract(vert[i+1],P),d)<0):
				continue
			elif (np.dot(np.subtract(vert[i],P),d)>=0 and np.dot(np.subtract(vert[i+1],P),d)<=0) or (np.dot(np.subtract(vert[i],P),d)<=0 and np.dot(np.subtract(vert[i+1],P),d)>=0):
				A1 = np.array([Pvert[i],-edges[i]])
				A = np.array([d,-edges[i]])
				t1 = np.linalg.det(A1)/np.linalg.det(A)

				if t1>=0:
					if np.dot(edges[i],n)<0:
						sum = sum-1
					else:
						sum = sum+1
				
	# The for-loop does not consider the edge from the "last point" of the polygon to it´s "first one". This is done with the following
	# algorithm, where the procedure is the same one like in the previous for-loop
	if dot_Pn[0]*dot_Pn[len(vert)-1]<=0: 
		if np.dot(np.subtract(vert[len(vert)-1],P),d)>=0 and np.dot(np.subtract(vert[0],P),d)>=0:
			if np.dot(edges[len(vert)-1],n)<0:
				sum = sum-1
			else:
				sum = sum+1
		elif (np.dot(np.subtract(vert[len(vert)-1],P),d)>=0 and np.dot(np.subtract(vert[0],P),d)<=0) or (np.dot(np.subtract(vert[len(vert)-1],P),d)<=0 and np.dot(np.subtract(vert[0],P),d)>=0):
			A1 = np.array([Pvert[len(vert)-1],-edges[len(vert)-1]])
			A = np.array([d,-edges[len(vert)-1]])
			t1 = np.linalg.det(A1)/np.linalg.det(A)

			if t1>=0:
				if np.dot(edges[len(vert)-1],n)<0:
					sum = sum-1
				else:
					sum = sum+1
	
	# Now it can be inferred of the sum if the point P is inside (sum != 0) or outside (sum = 0)
	if sum == 0:
		print('The point is outside!')
	else:
		print('The point is inside!')

	# Plot points to visually check that the function is producing the correct answer
	plt.plot(*OGpolypts.T,'--', color='g', label='Polygon')
	plt.plot(point[0], point[1], 'o', color='red', label='Point')
	plt.axis('equal')
	plt.legend()
	plt.title('Question 1: Polygon and Point Check')
	plt.xlabel('X')
	plt.ylabel('Y')
	plt.show()

if __name__ == '__main__':
	vert = ([1,-1], [3,3], [-2,6], [6,7], [-4,5], [7,-1])
	P = ([0, 0.5])
	InOrOut(vert,P)
