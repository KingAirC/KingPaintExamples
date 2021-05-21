import king

p1 = king.point(4, 2)


@king.geometry_generate(cls=king.KingFunction)
def sin_point(depends=(), essential_data=None):
    a = depends[0].basic_data[0]
    b = depends[0].basic_data[1]

    return {'function': lambda x: a * king.sin(b * x),
            'x_min': None,
            'x_max': None,
            'count': 100 + 100 * abs(int(b))}


f1 = sin_point(depends=[p1])
