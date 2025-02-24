# -*- coding: utf-8 -*-
"""
Module for the creation of an object oriented class of vectors working in Cartesian coordinates
with adaptibility to polar coordinates

MIT License

Copyright (c) 2025 Adam John Rae

See LICENSE.txt for details
"""
import numpy as np

class Vector:
    """
       Vector class for three dimensional quantities using Cartesian coordinates
    """
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        """
        Assumes floating point when printing
        """
        return f"Vector: ({self.i:.2f}, {self.j:.2f}, {self.k:.2f})"

    def __add__(self,other):
        """
        Overloads addition for the elements of two instances

        """
        return Vector(self.i + other.i, self.j + other.j, self.k + other.k)

    def __sub__(self,other):
        """
        Overloads subtraction for the elements of two instances

        """
        return Vector(self.i - other.i, self.j - other.j, self.k - other.k)

    def magnitude(self):
        """
        Computes the magnitude of an instance as the square root of the sum of the squares of the
        vector components
        
        """
        return np.sqrt(self.i**2 + self.j**2 + self.k**2)

    def dot(self,other):
        """
        Computes the dot product of two vector instances
        
        """
        return self.i * other.i + self.j * other.j + self.k * other.k

    def cross(self,other):
        """
        Computes the cross product of two vector instances

        """
        return Vector(self.j * other.k - self.k * other.j,
                      -(self.i * other.k - self.k * other.i),
                      self.i * other.j - self.j * other.i)

    def area(self,other,other2):
        """
        Given 3 vertice instances, calculates the area of the triangle they create
        
        """
        line_ab = other - self
        line_ac = other2 - self
        return (Vector.cross(line_ab, line_ac)).magnitude()/2

    def angle(self,other):
        """
        Given two instances, calculates the angle between them

        """
        return np.rad2deg(np.arccos(Vector.dot(self,other)/ (self.magnitude() * other.magnitude())))

    def angle_vertices(self,other,other2):
        """
        Taking 3 vertice points, caclulates the internal angles of the triangle they create
        
        """
        line_ab, line_ac = other - self, other2 - self
        line_ba, line_bc = self - other, other2 - other
        line_ca, line_cb = self - other2, other - other2
        return (Vector.angle(line_ab, line_ac),
                Vector.angle(line_bc, line_ba),
                Vector.angle(line_cb, line_ca))

class PolarVector(Vector):
    """
       Vector class for three dimensional quantities using spherical/polar coordinates in degrees
       
    """
    def __init__(self, r, theta, phi):
        """
        Calculates the Cartesian equivalent of the polar coordinates and stores the PolarVector
        as a Vector

        """
        theta = np.deg2rad(theta)
        phi = np.deg2rad(phi)
        Vector.__init__(self,
                        r*np.sin(theta) * np.cos(phi),
                        r*np.sin(theta) * np.sin(phi),
                        r*np.cos(theta))

    def r(self):
        """
        Computes the radius component
        
        """
        return self.magnitude()

    def phi(self):
        """
        Computes the azimuthal angle in degrees
        
        """
        return np.rad2deg(np.arctan2(self.j,self.i))

    def theta(self):
        """
        Calculates the polar angle in degrees
        
        """
        return np.rad2deg(np.arcsin(self.k/self.magnitude()))

    def __str__(self):
        """
        Assumes floating point when printing and converts from Cartesian to polar
        
        """
        r = self.r()
        phi = self.phi()
        theta = self.theta()
        return f"PolarVector: ({r:.2f}, {theta:.2f}, {phi:.2f})"
