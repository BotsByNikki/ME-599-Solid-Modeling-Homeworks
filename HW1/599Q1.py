#!/usr/bin/env python

#Nicole Guymer and Niklas Delboi
#ME 599: Solid Modeling
#Homework 1
#1/21/2019

"""Question 1: Your function should accept two arguments,
each an array of four numbers representing the normal 
and the offset for the plane. The output from your function 
should print to the screen and return the line as a two arguments:
an anchor point and a direction vector. Then plot the result!

Here is where it gets tricky. You only need to plot the line segment(s) 
that connect the points where the line passes through each of the x, y, 
and z planes. Like the problem from class, it could be that your segment 
only passes through two of the planes. """

#Solving simultaneous equations with Numpy:
#	http://dwightreid.com/blog/2015/09/21/python-how-to-solve-simultaneous-equations/

%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def Question1 (n1, b1, n2, b2):
	"""This function takes the normal and offset points of two planes
	and prints the resulting intersection line """
	#Find the direction vector
	d = np.cross(n1, n2)
	div = np.sqrt(d[0]**2 + d[1]**2 + d[2]**2)

	#Normalize the direction vector
	d_norm = []
	for i in range(len(d)):
		d_norm.append(d[i]/div)


	#Find the line
	A = np.array([ [n1[1], n1[2]] , [n2[1], n2[2]] ])
	B = np.array([b1, b2])

	C = np.linalg.solve(A,B)
	Xx = 0.0
	Xy = C[0]
	Xz = C[1]

	#Plot the intersection line
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	ax.quiver(d_norm[0], d_norm[1], d_norm[2], Xx, Xy, Xz)
	plt.title('Line of intersetion between two plane')
	ax.set_xlabel('X')
	ax.set_ylabel('Y')
	ax.set_zlabel('Z')
	plt.show()

	return ("Anchor Point = %s" % [Xx, Xy, Xz], "Direction = %s" % d_norm)


if __name__ == '__main__':
	#Replace values below with test cases for n1, b1, n2, b2 (respectively)
	n1 = [0.65, 0.575, 0.503]
	b1 = 10.3
	n2 = [-0.2, 0.0, 0.98]
	b2 = 5.0
	print (Question1 (n1, b1, n2 , b2))