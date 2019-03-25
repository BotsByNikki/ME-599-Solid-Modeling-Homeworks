# ME 599 Solid Modeling HW 1

This repository holds the final version of the code submitted for ME 599 Solid Modeling homework #1.

Questions 1) Write a function that finds the line between two planes. 
Your function should accept two arguments - each an array of four numbers representing the normal (x_n, y_n, z_n) and the offset (b) for the plane. 
The output from your function should print to the screen and return the line as a two arguments: an anchor point (X) and a direction vector (d). 
Then plot the result! Here is where it gets tricky. You only need to plot the line segment(s) that connect the points where the line passes through each of the x, y, and z planes. 
Like the problem from class, it could be that your segment only passes through two of the planes.

Question 2) Write a function to calculate the surface area and volume of a tetrahedron. 
Write a function that takes four points of a tetrahedron as input (4 3-element arrays), and shows the resulting solid. 
Also, print out the surface area and volume of the tetrahedron.

Question 3) Find and plot the two points that are 10 units away from any three arbitrary points. 
Given three non-collinear points as input (x_1, x_2, x_3), plot and print out the two new points (y_1, y_2) that are each 10 units away from these three points. 
Hint: there will be a line - similar to the perpendicular bisector that is equidistant from these three points. 
This line passes perpendicularly through the plane defined by the three lines (therefore, you must first find this plane).
