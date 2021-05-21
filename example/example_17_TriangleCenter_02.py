import king

p1, p2, p3 = king.point(p_list=[[5, 7], [-2, 3], [2, -8]])
l1 = king.line_segment(p1, p2)
l2 = king.line_segment(p2, p3)
l3 = king.line_segment(p1, p3)
c = king.median(p1, p2, p3)
