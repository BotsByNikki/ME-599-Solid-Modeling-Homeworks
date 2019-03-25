# ME 599 Solid Modeling HW4

Question 1) Rational Bezier Curves Write a function that plots a rational quadratic Bezier curve (see Janke 7.2.4 for details). 
It will need to recieve four vectors: 𝑝0 , 𝑝1 , 𝑝2 , & 𝑤 . Note 𝑝𝑖 are 2D points (x and y pairs), but 𝑤 is three values (one for each control point). 
Since, 𝑡 will only vary from 0 to 1, plot 20 line segments by dividing the t into a linear space (e.g. t = 0.0, 0.05, 0.1, 0.15, ..., 1.0).

Question 2) Egg Draw an egg shape comprised of four function calls to your above function following the picture attached.

Note that the orange and yellow curves are comprised of ellipses and the blue and green are circles. 
You should be exact in making the circle sections, but you can try different locations for the intermediate control point of the ellipese.

2.1 Using your previous polygonal functions come up with a value for the area of the egg. Is this lower or greater than the actual area?

2.2 What is the continuity at the connections between the curves?
