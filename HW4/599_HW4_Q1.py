#!/usr/bin/env python

#Nicole Guymer and Niklas Delboi
#ME 599: Solid Modeling
#Homework 4
#2/27/2019

"""Question 1: Write a function that plots a rational quadratic Bezier curve.
It will recieve 4 vector (p0,p1,p2,w). Points p_i are 2D while w has 3 values
(one for each control point). t varies from 0 to 1, split this up into 20 line segments. """

#%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

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

	plt.plot(P[:,0], P[:,1])
	plt.title('Question 1')
	plt.xlabel('X')
	plt.ylabel('Y')
	plt.show()


if __name__ == '__main__':
	p0 = [2,0]
	p1 = [2,-2]
	p2 = [0,-2]
	w = [1,1,2]
	RationalBezier(p0,p1,p2,w)