import king

edge_number = 37
jump_number = 17
radius = 10

t = king.pi_2 / edge_number

v = []

# KingFigure not update immediately.
king.figure.init_delay_update = True

for i in range(edge_number):
    v.append(king.point(radius * king.cos(i * t), radius * king.sin(i * t)))

for i in range(edge_number):
    king.line_segment(v[i], v[(i + jump_number) % edge_number])

# KingFigure update immediately.
king.figure.init_delay_update = False
