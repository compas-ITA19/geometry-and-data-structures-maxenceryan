from compas.geometry import Vector, Polygon

# As an exercise, instead of using centroid, tried to draw vectors from the starting vertex to all other vertices
# Then computed areas for all triangle subdivions of convex polygon and summed them up
# inspired by https://bell0bytes.eu/centroid-convex/

def get_convex_polygon_area(P):
    p = Polygon(P)
    pt_base = p.points[0]
    pts = p.points
    pts.pop(0)
    
    vectors = [pt_base - pt for pt in pts]
    #print(vectors)
    partial_areas = [vectors[i].cross(vectors[i+1]).length * 0.5 for i in range(0, len(vectors)-1)]
    #print(partial_areas)
    return sum(partial_areas)

# Example
polygon = Polygon([[0,0,0], [1,0,0],  [1,1,0], [0,1,0]])
print(get_convex_polygon_area(polygon) == polygon.area)