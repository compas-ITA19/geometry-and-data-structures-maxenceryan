import compas
from compas.geometry import Vector, Polygon

## MODULE 0: ASSIGNMENT 02

## Task 1

# Gets the three orthonormal unit vectors based on the first vector given
def get_orthonomal_vectors(A,B):
    u = A
    v = A.cross(B)
    w = v.cross(A)
    return u.unitized(), v.unitized(), w.unitized()

A = Vector(1.0, 0.0, 0.0)
B = Vector(0.0, 1.0, 0.0)

#print(get_orthonomal_vectors(A,B))

## Task 2

# Given an input as a Polygon, calculates the area
def get_convex_polygon_area(P):
    #P.area()....
    p = Polygon(P)
    pt_base = p.points[0]
    pts = p.points.pop(0)
    vectors = [pt_base - pt for pt in pts]
    print(vectors)

    return sum() * 0.5

polygon = Polygon([[0,0,0], [1,0,0], [1,1,0], [0,1,0]])
print(get_convex_polygon_area(polygon))