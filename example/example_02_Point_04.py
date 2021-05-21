import king

p1, p2, p3 = king.point(p_list=[[3, 4], [-4, 2], [5, 6]], label='p', from_number=1, color='yellow')

l1 = king.line(p1, p2)
p4 = king.vertical(p3, l1)
p4.set_markerfacecolor('green')
p4.set_markeredgecolor('darkgreen')
