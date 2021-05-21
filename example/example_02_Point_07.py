import king

p1, p2, p3, p4 = king.point(p_list=[[4, 5], [-3, 2], [1, 9], [8, 2]], label='p', from_number=1)
l1 = king.line(p1, p2)
l2 = king.line(p3, p4)
p = king.intersect(l1, l2)
