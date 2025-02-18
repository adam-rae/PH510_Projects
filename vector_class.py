# -*- coding: utf-8 -*-
import numpy as np

"""
Object oriented class of vectors working in Cartesian coordinates with adaptibility to polar coordinates

"""

class vector:
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
        return vector(self.i + other.i, self.j + other.j, self.k + other.k)

    def __sub__(self,other):
        """
        Overloads subtraction for the elements of two instances

        """
        return vector(self.i - other.i, self.j - other.j, self.k - other.k)

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
        return vector(self.j * other.k - self.k * other.j,
                      -(self.i * other.k - self.k * other.i),
                      self.i * other.j - self.j * other.i)

    def area(self,other,other2):
        """
        Given 3 vertice instances, calculates the area of the triangle they create
        
        """
        line_ab = other - self
        line_ac = other2 - self
        return (vector.cross(line_ab, line_ac)).magnitude()/2

    def angle(self,other):
        """
        Given two instances, calculates the angle between them

        """
        return np.rad2deg(np.arccos(vector.dot(self,other)/ (self.magnitude() * other.magnitude())))

    def angle_vertices(self,other,other2):
        """
        Taking 3 vertice points, caclulates the internal angles of the triangle they create
        
        """
        line_ab, line_ac = other - self, other2 - self
        line_ba, line_bc = self - other, other2 - other
        line_ca, line_cb = self - other2, other - other2
        return vector.angle(line_ab, line_ac),
        vector.angle(line_bc, line_ba),
        vector.angle(line_cb, line_ca)

class polar_vector(vector):
    """
    Vector class for three dimensional quantities using spherical/polar coordinates in degrees
    
    """
    def __init__(self, r, theta, phi):
        theta = np.deg2rad(theta)
        phi = np.deg2rad(phi)
        vector.__init__(self,
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
        return f"polar_vector: ({r:.2f}, {theta:.2f}, {phi:.2f})"
