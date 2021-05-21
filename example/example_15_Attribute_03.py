import king

c = king.circle(o=king.point(1, 3), p=king.point(-3, 2)).append_call_back(lambda circle: print(circle.basic_data[1]))
