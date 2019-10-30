from compas.geometry import Vector

def get_orthonomal_vectors(A,B):
    u = A
    v = A.cross(B)
    w = v.cross(A)
    return u.unitized(), v.unitized(), w.unitized()

# Example
A = Vector(1.0, 0.0, 0.0)
B = Vector(0.0, 1.0, 0.0)

print(get_orthonomal_vectors(A,B))

