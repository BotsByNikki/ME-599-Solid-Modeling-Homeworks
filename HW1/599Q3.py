#!/usr/bin/env python

#Nicole Guymer and Niklas Delboi
#ME 599: Solid Modeling
#Homework 1
#1/21/2019

"""Question 3: Given three non-collinear points as input, plot and print out 
the two new points that are each 10 units away from these three points. 

Hint: there will be a line - similar to the perpendicular bisector that is 
equidistant from these three points. This line passes perpendicularly through 
the plane defined by the three lines (therefore, you must first find this plane). """
%matplotlib inline
from scipy.optimize import fsolve
import math as m
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection

def vert (p1, p2):
	"""This function finds the edges between the given points. 
	I initial called it "verticies" originally, but I'm too lazy to change it """
	vx = p2[0]-p1[0]
	vy = p2[1]-p1[1]
	vz = p2[2]-p1[2]
	return [vx, vy, vz]


def Question3 (x1, x2, x3):
	"""This function does takes the given three points of a trianglar plane
	and finds two points that are 10 units away from all points. Then plots the
	resulting points and the plane."""

	#solve systems of equations
	def equations(p):
		dx, dy, dz = p
		return (m.sqrt((x1[0]-dx)**2 + (x1[1]-dy)**2 + (x1[2]-dz)**2)-10, m.sqrt((x2[0]-dx)**2 + (x2[1]-dy)**2 + (x2[2]-dz)**2)-10, m.sqrt((x3[0]-dx)**2 + (x3[1]-dy)**2 + (x3[2]-dz)**2)-10)

	dx, dy, dz = fsolve(equations, (1,1,1))
	

	#cross product to find a perpendicular vector
	x21 = vert(x1, x2)
	x31 = vert(x1, x3)
	c = np.cross(x21, x31) #normal vector
	mag = m.sqrt(c[0]**2 + c[1]**2 + c[2]**2)

	#make into a unit vector
	c_norm = [] 
	for i in range(len(c)):
		c_norm.append(c[i]/mag)


	#point 10 units away- from plane to point
	w = [(dx-x1[0]), (dy-x1[1]), (dz-x1[2])]
	top = np.dot(c,w)
	

	#distance from point to plane
	g = np.abs(top)/mag

	#mirror that point across the plane to get a second point
	d2x, d2y, d2z = (dx + 2*g*c_norm[0]), (dy + 2*g*c_norm[1]), (dz + 2*g*c_norm[2])
	w2 = [(d2x-x1[0]), (d2y-x1[1]), (d2z-x1[2])]
	top2 = np.dot(c, w2)
	g2 = np.abs(top2)/mag	


	#Plotting
	fig = plt.figure()
	ax = fig.add_subplot(111, projection = '3d')

	#Plot the two points
	d1 = [dx,dy,dz]
	d2 = [d2x, d2y, d2z]
	points = np.array([d1,d2])
	ax.scatter3D(points[:,0], points[:,1], points[:,2], color = 'k')
	#plt.hold(True)

	#Plot the plane
	plane_pt = np.array([x1,x2,x3])
	ax.scatter3D(plane_pt[:,0], plane_pt[:,1], plane_pt[:,2], color = 'g')
	verts = [[plane_pt[0], plane_pt[1], plane_pt[2]]]
	ax.add_collection3d(Poly3DCollection(verts, facecolors='g', linewidths=1, edgecolors='k', alpha = .1))


	#Label your plot
	plt.title('Plane with 2 points 10 units away')
	ax.set_xlabel('X')
	ax.set_ylabel('Y')
	ax.set_zlabel('Z')
	plt.show()




if __name__ == '__main__':
	#Replace the values for x1, x2, and x3 below with the desired test cases
	x1 = [11,8,9]
	x2 = [10,10,10]
	x3 = [2,3,4]
	print (Question3(x1,x2,x3))





