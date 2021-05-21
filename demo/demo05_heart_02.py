import time
import king

# king.KingFigure().init_delay_update = True

o = king.point(0, 0)
o.set_visible(False)
r = 18

c = king.circle(o, r)
c.set_color('red')

n = 101

p_list = []

for i in range(n):
    p = king.point(r * king.cos(i * 2 * king.pi / n), r * king.sin(i * 2 * king.pi / n))
    p_list.append(p)
    p.set_visible(False)

l_lst = []

tow_pow = 1
for i in range(n):
    nxt = 2 * tow_pow
    time.sleep(0.02)
    line = king.line_segment(p_list[tow_pow % n], p_list[nxt % n])
    line.set_color('#EE6AA7')
    l_lst.append(line)
    tow_pow = nxt

king.KingFigure().init_delay_update = False
