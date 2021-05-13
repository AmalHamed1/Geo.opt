import Rhino.Geometry as rg
import math

#create a sun vector

#1. create a Sphere at point (0,0,0) with radius 1 and output it to a
#output the sphere to a

sphere_center = rg.Point3d (0,0,0)
sphere_radius = 1.0
sphere = rg.Sphere(sphere_center, sphere_radius)

a = sphere 

#2. evaluate a point in the sphere using rg.Sphere.PointAt() at coordintes x and y
#the point should only be on the upper half of the sphere (upper hemisphere)
#the angles are in radians, so you might want to use math.pi for this
#output the point to b


b = rg.Sphere.PointAt(a, x, y)

#create a vector from the origin and reverse the vector
#keep in mind that Reverse affects the original vector
#output the vector to c


vec = rg.Vector3d(b)
vec = rg.Vector3d.Negate(vec)

c = vec