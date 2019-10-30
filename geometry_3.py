from compas.geometry import Vector
import numpy as np

def get_array_cross(A,B):
    if len(A) != len(B): return []
    return [a.cross(b) for a, b in zip(A,B)]

def get_array_cross_numpy(A,B):
    if len(A) != len(B): return []
    return np.cross(A,B)

# Example
A = [Vector(0,0,1),
    Vector(0,1,0),
    Vector(1,0,0)]

B = [Vector(1,0,0),
    Vector(0,0,1),
    Vector(0,1,0)]

print(get_array_cross(A,B))
print(get_array_cross_numpy(A,B))

