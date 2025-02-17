# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 20:21:50 2025

@author: adamr
"""

"""
   Object oriented class of vectors
"""
import numpy as np

class Vector:
    """
       Vector class for three dimensional quantities using Cartesian coordiantes
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
        Computes the magnitude of an instance as the square root of the sum of the squares of the vector components
        
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
    
class PolarVector(Vector):
    """
       Vector class for three dimensional quantities using spherical/polar coordinates in degrees
    """
    def __init__(self, r, theta, phi):
        theta = np.deg2rad(theta)
        phi = np.deg2rad(phi)
        Vector.__init__(self,
                        r*np.cos(theta) * np.cos(phi),
                        r*np.cos(theta) * np.sin(phi),
                        r*np.sin(theta))
        
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
        Assumes floating point when printing
        """
        r = self.r()
        phi = self.phi()
        theta = self.theta()
        return f"PolarVector: ({r:.2f}, {theta:.2f}, {phi:.2f})"