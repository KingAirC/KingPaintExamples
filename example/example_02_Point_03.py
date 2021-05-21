import king

# p3 is p2 rotate with p1 anti-clockwise pi/4.
# Drag p1, p2.
# You can't drag p3.

p1, p2 = king.point(p_list=[[0, 5], [0, 0]], label='p', from_number=1)
p3 = king.rotate(p1, p2, king.pi_quarter)
p3.text.set_text('p3')
