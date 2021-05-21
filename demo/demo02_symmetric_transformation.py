import king

mat = [
    [2, -1],
    [-1, 0.3]
]

e = king.eig_n(mat)

v1 = e[0]
v2 = e[1]

o = king.point(0, 0)
o.set_visible(False)
p1 = king.point(v1[0], v1[1])
p1.set_visible(False)
p2 = king.point(v2[0], v2[1])
p2.set_visible(False)

l1 = king.line(o, p1)
l2 = king.line(o, p2)

p_free = king.point(5, 5, color='red')
p_val = king.point_matrix(depends=[p_free], essential_data=[mat])
vp = king.line_segment(p_free, p_val)

pf1 = king.symmetric(p_free, l1)
pv1 = king.point_matrix(depends=[pf1], essential_data=[mat])
king.line_segment(pf1, pv1)

pf2 = king.symmetric(p_free, l2)
pv2 = king.point_matrix(depends=[pf2], essential_data=[mat])
king.line_segment(pf2, pv2)

pf3 = king.symmetric(p_free, o)
pv3 = king.point_matrix(depends=[pf3], essential_data=[mat])
king.line_segment(pf3, pv3)
