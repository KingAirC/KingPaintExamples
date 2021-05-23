import king

c = king.conic(p_list=king.point(p_list=[[12, -4], [-4.2, -2], [4, 9], [0, 2], [5, 4]]))

p = king.point(curve=c, color='red')

l1, l2, p1, p2 = king.tangent_line(p, c)

l1.set_color('green')
