# ME 599 Project

Term project, done in teams of two, that uses the concepts from lecture.

Project Proposal: For our project, we propose taking homework 3 question 2 and expanding on that to include a variable offset. 
The original question asked us to create a function that can take in vertex points of a convex polygon and create a new polygon that is offset from those vertices by a given amount. 
Our project will apply a variable offset to the original polygon vertices (either convex or concave) which means that for each vertex we will apply a different offset (within a close margin ~0.0 to ~3.0) and connect these points to create a new offset polygon. 
If time allows, we will work on applying a spline between these points to create a smooth transition between vertices either using an available python module or creating our own method. 
The function created above will be applied to various test racetracks in order to assist the students working on the Formula Student Driverless Team. 
Their task is to create a path planning algorithm for their autonomous race car. 
They need to be able to take in information about the track and generate an appropriate spline/path for the race car. 
Our work will help build the configuration space in which the race car will operate. 
The offset for each vertex of the racetrack will be formulated given the race car's estimate of where the edges of the track are; this value will be given to us by the Formula Team. 
The goal of the configuration space is to keep the race car a safe distance away from the edges of the track even with measurement uncertainty.
