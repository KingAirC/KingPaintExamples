import king

e1 = king.parametric_equation(lambda t: 5 * (t - king.sin(t)), lambda t: 5 * (1 - king.cos(t)), 0, king.pi_2)
