from compas.geometry import Vector, Polygon

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