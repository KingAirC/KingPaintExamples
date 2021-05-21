import king


# Create a point in the middle of p1 and p2.
# s is a KingPoint too.
# You can't drag and move s.

p1, p2 = king.point(p_list=[[2, 0.5], [4, 9]], color='red')
s = king.middle(p1, p2)
