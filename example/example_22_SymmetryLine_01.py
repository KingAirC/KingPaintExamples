import king

king.figure.init_delay_update = True

l1, l2 = king.symmetry_lines(king.conic(p_list=king.point(p_list=[[2, 4], [-9, 1], [3.5, 8], [11, 4], [-14, 4.3]])))

king.figure.init_delay_update = False
