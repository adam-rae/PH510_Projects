# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 20:21:50 2025

@author: adamr
"""

"""
   Object oriented class of vectors
"""

class Vector:
    """
       Vector class for three dimensional quantities
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
        Parameters
        
        """
        return (self.i**2 + self.j**2 + self.k**2)**(1/2)
    
    def dot(self,other):
        """
        Computes the dot product of two instances
        
        """
        return self.i * other.i + self.j * other.j + self.k * other.k
    
    def cross(self,other):
        """
        Computes the cross product of two instances

        """
        return Vector(self.j * other.k - self.k * other.j,
                      -(self.i * other.k - self.k * other.i),
                      self.i * other.j - self.j * other.i)
    
X = Vector(1,0,0)
Y = Vector(0,1,0)
Z = Vector(0,0,1)

print(X-Y)
print(Vector.cross(X, Z))