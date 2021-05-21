from king.core.king_animation import KingAnimation
import king

p1 = king.point(3, 0)
p2 = king.point_matrix(depends=[p1], essential_data=[[[1, 2], [2, -1]]])
l1 = king.line(k=1, b=2)

KingAnimation([p1, l1], [lambda frame: [3 * king.cos(frame), 3 * king.sin(frame)],
                         lambda frame: [king.cos(frame), king.sin(frame)]])
