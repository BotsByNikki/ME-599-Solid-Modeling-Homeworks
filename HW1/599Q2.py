#!/usr/bin/env python

#Nicole Guymer and Niklas Delboi
#ME 599: Solid Modeling
#Homework 1
#1/21/2019

"""Question 2: Write a function that takes four points of a tetrahedron as input 
(4 3-element arrays), and shows the resulting solid. 
Also, print out the surface area and volume of the tetrahedron."""

#Online calculator for volume, vert, and edge functions: 
#	http://tamivox.org/redbear/tetra_calc/index.html

#Area of triangles:
#	https://www.mathsisfun.com/geometry/herons-formula.html

	
%matplotlib inline
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
import matplotlib.pyplot as plt

def vert (p1, p2):
	"""This function finds the edges between the given points. 
	I initial called it "verticies" originally, but I'm too lazy to change it """
	vx = p2[0]-p1[0]
	vy = p2[1]-p1[1]
	vz = p2[2]-p1[2]
	return [vx, vy, vz]

def Tetra(p1, p2, p3, p4):
	"""This function takes four 3D points of a tetrahedron to calculate the volume
	and surface area, and plots the shape in 3D. """

    #Solve for the surface area.
    #This is done by finding the area of each triangular face of the tetrahedron,
    # and adding them together.

    #Area of triangle 1
	d = vert(p2,p4)
	mag = np.sqrt(d[0]**2+d[1]**2+d[2]**2)
	d_norm = [d[0]/mag, d[1]/mag, d[2]/mag]

	sub = np.subtract(p1,p2)
	q = np.add(p2,np.multiply(np.dot(sub,d_norm),d_norm))

	h = np.linalg.norm(q-p1)
	g = np.linalg.norm(d)
	tri1 = g*h/2

	#Area of triangle 2
	d = vert(p1,p2)
	mag = np.sqrt(d[0]**2+d[1]**2+d[2]**2)
	d_norm = [d[0]/mag, d[1]/mag, d[2]/mag]

	sub = np.subtract(p3,p1)
	q = np.add(p1,np.multiply(np.dot(sub,d_norm),d_norm))

	h = np.linalg.norm(q-p3)
	g = np.linalg.norm(d)
	tri2 = g*h/2

	#Area of triangle 3
	d = vert(p2,p4)
	mag = np.sqrt(d[0]**2+d[1]**2+d[2]**2)
	d_norm = [d[0]/mag, d[1]/mag, d[2]/mag]

	sub = np.subtract(p3,p2)
	q = np.add(p2,np.multiply(np.dot(sub,d_norm),d_norm))

	h = np.linalg.norm(q-p3)
	g = np.linalg.norm(d)
	tri3 = g*h/2

	#Area of triangle 4
	d = vert(p3,p4)
	mag = np.sqrt(d[0]**2+d[1]**2+d[2]**2)
	d_norm = [d[0]/mag, d[1]/mag, d[2]/mag]

	sub = np.subtract(p1,p3)
	q = np.add(p3,np.multiply(np.dot(sub,d_norm),d_norm))

	h = np.linalg.norm(q-p1)
	g = np.linalg.norm(d)
	tri4 = g*h/2


	#Find surface area by summing all the 4 above triangle areas
	SA = tri1+tri2+tri3+tri4

	#Volume
	V = np.abs(np.dot(vert(p1,p2),np.cross(vert(p1,p3),vert(p1,p4))))/6

	#Plot the tetrahedon : https://stackoverflow.com/questions/44881885/python-draw-3d-cube
	fig = plt.figure()
	ax = fig.add_subplot(111, projection = '3d')

	#plot points
	points = np.array([p1,p2,p3,p4])

	#plot vertices
	ax.scatter3D(points[:,0], points[:,1], points[:,2], color = 'k')
	verts = [[points[0], points[1], points[3]], [points[0], points[1], points[2]], [points[0], points[2], points[3]], [points[1], points[2], points[3]]]
	ax.add_collection3d(Poly3DCollection(verts, facecolors='w', linewidths=1, edgecolors='k', alpha = .1))

	#Label the plot
	plt.title('Tetrahedron Plot')
	ax.set_xlabel('X')
	ax.set_ylabel('Y')
	ax.set_zlabel('Z')
	plt.show()


	return ("Volume of Tetrahedron = %s" % V, "Surface Area of Tetrahedron = %s" % SA)

if __name__ == '__main__':
	#Replace the values for x1, x2, x3, x4 below with the desired test cases
	x1 = [0.0 ,0.0 ,-2.0]
	x2 = [5.0 ,0. ,0. ]
	x3 = [0. ,5. ,0. ]
	x4 = [2. ,2. ,4. ]
	print (Tetra(x1,x2,x3,x4))

