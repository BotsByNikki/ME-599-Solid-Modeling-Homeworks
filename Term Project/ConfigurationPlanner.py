#!/usr/bin/env python

#Nicole Guymer and Niklas Delboi
#HW 5 - Final Project

#%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import shapely.geometry as shp
from scipy.interpolate import splprep, splev, splrep


def PolyOffset(points, offset):

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
		midpoints_offset[i] = midpoints[i]+offset[i]*unit_normals[i] 	# get the offset midpoints with the offset as a scalar (delta) and the unit normal vectors

	# Do all the same steps for the last edge from the "last point" to the "first point" of the given polygon
	edges[len(points)-1] = np.subtract(points[0],points[len(points)-1])
	normals[len(points)-1] = (edges[len(points)-1,1],-edges[len(points)-1,0])
	mag2 = np.sqrt(normals[len(points)-1,0]**2+normals[len(points)-1,1]**2)
	unit_normals[len(points)-1] = normals[len(points)-1]/mag2
	midpoints[len(points)-1] = points[len(points)-1]+0.5*edges[len(points)-1]
	midpoints_offset[len(points)-1] = midpoints[len(points)-1]+offset[len(points)-1]*unit_normals[len(points)-1] 

	# # Define the new polygons
	OffsetPoly = shp.Polygon(midpoints_offset)

	# Turn polygon points into numpy arrays for plotting
	OGpolypts = np.array(OGpoly.exterior)
	OffsetPolypts = np.array(OffsetPoly.exterior)
	

	return OGpolypts, OffsetPolypts 


if __name__ == '__main__':	

	#read in the example track information
	wb = np.load('track2.npy')

	#seperate the inside and outside edges of the track
	wb0 = wb[0]
	wb1 = wb[1]

	#Close the loop by connecting the last point to the first point
	inside = wb0
	outside = wb1

	#make random set of test offsets
	offsets_inside = np.ones(len(wb0)) #don't include the repeated start point
	for i in range(len(offsets_inside)):
		offsets_inside[i] = np.random.uniform(low = 0.5, high = 1.25)

	offsets_outside = np.ones(len(wb1))
	for i in range(len(offsets_outside)):
		offsets_outside[i] = np.random.uniform(low = -2.25, high = -0.5)

	inside_track, in_offset = PolyOffset(inside, offsets_inside)
	outside_track, out_offset = PolyOffset(outside, offsets_outside)


#Spline the points
	x = (inside_track[:,0])
	y = (inside_track[:,1])
	tck, u = splprep([x,y], s = 5)
	new_points = splev(u,tck)
 
	i = in_offset[:,0]
	j = in_offset[:,1]
	tck1, u1 = splprep([i,j], s = 5)
	new_points1 = splev(u1,tck1)
	plt.plot(new_points[0], new_points[1], '--' ,color = 'blue', label = 'Left edge of track' )
	plt.plot(new_points1[0], new_points1[1], label = 'Left offset')

	x = (outside_track[:,0])
	y = (outside_track[:,1])
	tck, u = splprep([x,y], s = 5)
	new_points = splev(u,tck)

	i = out_offset[:,0]
	j = out_offset[:,1]
	tck1, u1 = splprep([i,j], s = 5)
	new_points1 = splev(u1,tck1)
	plt.plot(new_points[0], new_points[1], '--' ,color = 'orange', label = 'Right edge of track')
	plt.plot(new_points1[0], new_points1[1], label = 'Right offset')

	# #Plot points
	plt.axis('equal')
	plt.title('Test Track 1')
	plt.xlabel('X')
	plt.ylabel('Y')
	plt.legend()
	plt.show()
