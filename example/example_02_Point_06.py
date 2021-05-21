from king.geometry.king_plane_geometry_graph import KingPoint
from king.geometry.king_plane_geometry_graph_generator import point_matrix


p1 = KingPoint(essential_data=[3, 4])
p1.text.set_text('p1')
mat = [
    [1, 2],
    [2, -3]
]
p2 = point_matrix(depends=[p1], essential_data=[mat])
p2.text.set_text('p2')
