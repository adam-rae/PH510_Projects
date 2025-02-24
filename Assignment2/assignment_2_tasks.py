# -*- coding: utf-8 -*-
"""
Module for testing the Vector class. Each vertice is loaded to a vector and then the Vector.area
and Vector.angle_vertices functions are used to calculate the desired information which is printed
in the command line

MIT License

Copyright (c) 2025 Adam John Rae

See LICENSE.txt for details
"""
from vector_class import Vector, PolarVector

# ~~~~~~~~~~~~~~~~~~~~~~
# Triangle 1 - Cartesian

Vertice_1_a = Vector(0,0,0)
Vertice_1_b = Vector(1,0,0)
Vertice_1_c = Vector(0,0,1)

Area = Vector.area(Vertice_1_a, Vertice_1_b, Vertice_1_c)
print(f"Triangle 1 has area = {Area:.3f}")

angle_A, angle_B, angle_C = Vector.angle_vertices(Vertice_1_a, Vertice_1_b, Vertice_1_c)
print(f"Triangle 1 has internal angles {angle_A:.2f}, {angle_B:.2f}, and {angle_C:.2f}")

# ~~~~~~~~~~~~~~~~~~~~~~
# Triangle 2 - Cartesian

Vertice_2_a = Vector(-1,-1,-1)
Vertice_2_b = Vector(0,-1,-1)
Vertice_2_c = Vector(-1,0,-1)

Area = Vector.area(Vertice_2_a, Vertice_2_b, Vertice_2_c)
print(f"Triangle 2 has area = {Area:.3f}")

angle_A, angle_B, angle_C = Vector.angle_vertices(Vertice_2_a, Vertice_2_b, Vertice_2_c)
print(f"Triangle 2 has internal angles {angle_A:.2f}, {angle_B:.2f}, and {angle_C:.2f}")

# ~~~~~~~~~~~~~~~~~~~~~~
# Triangle 3 - Cartesian

Vertice_3_a = Vector(1,0,0)
Vertice_3_b = Vector(0,0,1)
Vertice_3_c = Vector(0,0,0)

Area = Vector.area(Vertice_3_a, Vertice_3_b, Vertice_3_c)
print(f"Triangle 3 has area = {Area:.3f}")

angle_A, angle_B, angle_C = Vector.angle_vertices(Vertice_3_a, Vertice_3_b, Vertice_3_c)
print(f"Triangle 3 has internal angles {angle_A:.2f}, {angle_B:.2f}, and {angle_C:.2f}")

# ~~~~~~~~~~~~~~~~~~~~~~
# Triangle 4 - Cartesian

Vertice_4_a = Vector(0,0,0)
Vertice_4_b = Vector(1,-1,0)
Vertice_4_c = Vector(0,0,1)

Area = Vector.area(Vertice_4_a, Vertice_4_b, Vertice_4_c)
print(f"Triangle 4 has area = {Area:.3f}")

angle_A, angle_B, angle_C = Vector.angle_vertices(Vertice_4_a, Vertice_4_b, Vertice_4_c)
print(f"Triangle 4 has internal angles {angle_A:.2f}, {angle_B:.2f}, and {angle_C:.2f}")

print("")

# ~~~~~~~~~~~~~~~~~~~~~~
# Triangle 5 - Spherical

Vertice_5_a = PolarVector(0,0,0)
Vertice_5_b = PolarVector(1,0,0)
Vertice_5_c = PolarVector(1,90,0)

Area = Vector.area(Vertice_5_a, Vertice_5_b, Vertice_5_c)
print(f"Triangle 5 has area = {Area:.3f}")

angle_A, angle_B, angle_C = Vector.angle_vertices(Vertice_5_a, Vertice_5_b, Vertice_5_c)
print(f"Triangle 5 has internal angles {angle_A:.2f}, {angle_B:.2f}, and {angle_C:.2f}")

# ~~~~~~~~~~~~~~~~~~~~~~
# Triangle 6 - Spherical

Vertice_6_a = PolarVector(1,0,0)
Vertice_6_b = PolarVector(1,90,0)
Vertice_6_c = PolarVector(1,90,180)

Area = PolarVector.area(Vertice_6_a, Vertice_6_b, Vertice_6_c)
print(f"Triangle 6 has area = {Area:.3f}")

angle_A, angle_B, angle_C = PolarVector.angle_vertices(Vertice_6_a, Vertice_6_b, Vertice_6_c)
print(f"Triangle 6 has internal angles {angle_A:.2f}, {angle_B:.2f}, and {angle_C:.2f}")

# ~~~~~~~~~~~~~~~~~~~~~~
# Triangle 7 - Spherical

Vertice_7_a = PolarVector(0,0,0)
Vertice_7_b = PolarVector(2,0,0)
Vertice_7_c = PolarVector(2,90,0)

Area = Vector.area(Vertice_7_a, Vertice_7_b, Vertice_7_c)
print(f"Triangle 7 has area = {Area:.3f}")

angle_A, angle_B, angle_C = Vector.angle_vertices(Vertice_7_a, Vertice_7_b, Vertice_7_c)
print(f"Triangle 7 has internal angles {angle_A:.2f}, {angle_B:.2f}, and {angle_C:.2f}")

# ~~~~~~~~~~~~~~~~~~~~~~
# Triangle 8 - Spherical

Vertice_8_a = PolarVector(1,90,0)
Vertice_8_b = PolarVector(1,90,180)
Vertice_8_c = PolarVector(1,90,270)

Area = Vector.area(Vertice_8_a, Vertice_8_b, Vertice_8_c)
print(f"Triangle 8 has area = {Area:.3f}")

angle_A, angle_B, angle_C = Vector.angle_vertices(Vertice_8_a, Vertice_8_b, Vertice_8_c)
print(f"Triangle 8 has internal angles {angle_A:.2f}, {angle_B:.2f}, and {angle_C:.2f}")
