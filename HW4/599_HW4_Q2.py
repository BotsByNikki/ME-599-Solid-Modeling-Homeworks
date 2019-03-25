#!/usr/bin/env python

#Nicole Guymer and Niklas Delboi
#ME 599: Solid Modeling
#Homework 4
#2/27/2019

"""Question 2: Draw an egg shape comprised of four function calls to your function from question 1."""

"""Question 2.1: The polygonal area of the egg is lower than the actual area. The polygonal area of the egg
cuts the corners instead of following the curve, resulting in a lower area. A higher number of t values would make the difference
between the actual area of the egg and the polygonal area smaller."""

"""Question 2.2: The continuity of the connections between the curves is C0  and C1. """

#%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import shapely.geometry as shp
import math as m

def RationalBezier(p0,p1,p2,w): #quadratic k=2, i=3
	p0 = np.array(p0)
	p1 = np.array(p1)
	p2 = np.array(p2)
	P = np.zeros((21,2))

	#t from 0 to 1, divided into 20 segments
	t = np.arange(start = 0, stop = 1.05, step = 0.05)


	#Solve for the blending curve and alpha values at each t value
	for i in range(21):
		B02 = (1-t[i])**2
		B12 = 2*t[i]*(1-t[i])
		B22 = t[i]**2

		#denominate value for calculating alpha
		denom = (w[0]*B02) + (w[1]*B12) + (w[2]*B22) 


		alpha02 = w[0]*B02/denom
		alpha12 = w[1]*B12/denom
		alpha22 = w[2]*B22/denom

		#Array of points to plot the curve
		P[i,:] = alpha02*p0 + alpha12*p1 + alpha22*p2
		
	return P

if __name__ == '__main__':

	#For the bottom right segment of the egg
	p0 = [20,0]
	p1 = [20,-20]
	p2 = [0,-20]
	w = [1,1,2]
	a = RationalBezier(p0,p1,p2,w)

	#For the bottom left segment of the egg
	p0 = [0,-20]
	p1 = [-20,-20]
	p2 = [-20,0]
	b = RationalBezier(p0,p1,p2,w)


	#For the top left segment of the egg
	p0 = [-20,0]
	p1 = [-20,40]
	p2 = [0,40]
	c = RationalBezier(p0,p1,p2,w)

	#For the top right segment of the egg
	p0 = [0,40]
	p1 = [20,40]
	p2 = [20,0]
	d = RationalBezier(p0,p1,p2,w)

	#Plot each segment seperately so the colors vary
	plt.plot(a[:,0], a[:,1])
	plt.plot(b[:,0], b[:,1])
	plt.plot(c[:,0], c[:,1])
	plt.plot(d[:,0], d[:,1])
	plt.axis([-40, 40, -20, 50])
	plt.grid()
	plt.title('Question 2: Egg')
	plt.xlabel('X')
	plt.ylabel('Y')
	plt.show()

	#Combine all the segments into 1 array
	total = np.concatenate((a,b), axis=0)
	total = np.concatenate((total,c), axis=0)
	total = np.concatenate((total,d), axis=0)

	#Create a polygonal version of the egg
	egg_poly = shp.Polygon((total))

	#Print the polygonal area of the egg
	print("The polygonal Area of the egg = %s" % egg_poly.area)

	#Calculate the actual area of the egg
	A_circ = 0.5*m.pi*20**2
	A_ellipse = 0.5*m.pi*40*20
	egg_actual = A_circ+A_ellipse

	print("The actual area of the egg = %s" % egg_actual)