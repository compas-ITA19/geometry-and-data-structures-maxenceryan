import os, compas, random
from compas.datastructures import Mesh
from compas_plotters import MeshPlotter

HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, 'data')
FILE = os.path.join(DATA,'faces.obj')

mesh = Mesh.from_obj(FILE)
plotter = MeshPlotter(mesh)

l = mesh.vertices_on_boundaries()
# get only boundary vertices without corners and flattening list of lists to list
boundary_vertices = [item for sublist in l for item in sublist if mesh.vertex_degree(item) == 3]

start_vertex_index = random.randint(0,len(boundary_vertices)-1)
start_vertex_key = boundary_vertices[start_vertex_index]

def get_traverse(start_key):

    if start_key not in boundary_vertices:
        raise ValueError('Vertex not on boundary')
    if mesh.vertex_degree(start_key) == 2:
        raise ValueError('Vertex cannot be corner')
    
    start_neighbors = mesh.vertex_neighbors(start_key)
    # find the index that corresponds to the next vertex for traversing the mesh
    # this helps ensure we go the proper direction despite the algorithm for ordering neighboring vertices
    index_traverse = [mesh.vertex_degree(key) for key in start_neighbors] #if mesh.vertex_degree(start_key)==4]
    #print(index_traverse)
    index_traverse = index_traverse[0]

    vertices = [start_key]
    current = start_neighbors[index_traverse]

    while True:
        vertices.append(current)
        if mesh.vertex_degree(current) < 4:
            break
        current = mesh.vertex_neighbors(current)[index_traverse]

    edges = []

    return vertices, edges

traverse_vertices, traverse_edges = get_traverse(start_vertex_key)
#print(traverse_vertices)

plotter.draw_vertices(
    facecolor={key: (255,0,0) for key in traverse_vertices},
    text= {key: str(key) for key in mesh.vertices()},
    radius=0.2
)

plotter.draw_edges(
    color={key: (255,0,0) for key in traverse_edges},
)

plotter.show()