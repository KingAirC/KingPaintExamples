import king

p1, p2, p3 = king.point(p_list=[[6, 0.34], [2.34, -9], [3.54, 2]], label='p', from_number=1)
p3.set_markerfacecolor('red')
l1 = king.line(p1, p2)
l1.text.set_text('mirror')
p4 = king.symmetric(p3, l1)
p4.set_markerfacecolor('grey')
