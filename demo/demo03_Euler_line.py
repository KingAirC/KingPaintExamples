import king

p1, p2, p3 = king.point(p_list=[[5, 7], [-2, 3], [2, -8]])

l1 = king.line_segment(p1, p2)
l2 = king.line_segment(p2, p3)
l3 = king.line_segment(p1, p3)

c1 = king.orthocenter(p1, p2, p3)
c1.text.set_text('ort')

c2 = king.median(p1, p2, p3)
c2.text.set_text('median')

c3 = king.outer(p1, p2, p3)
c3.text.set_text('outer')

euler_line = king.line(c1, c2)
euler_line.set_color('#893')
