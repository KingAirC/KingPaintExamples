import king

king.KingFigure().init_delay_update = True

n = 8

f = king.KingFunction(essential_data={'function': lambda x: 1, 'x_min': None, 'x_max': None, 'count': None})


def gen_heart(a, x):
    return abs(x) ** (2 / 3) + 0.9 * (3.3 - x ** 2) ** 0.5 * king.sin(a * king.pi * x)


def update(a):
    f.update_affected(new_essential_data={'function': lambda x: n * gen_heart(a, x / n),
                                          'x_min': -1.81 * n,
                                          'x_max': 1.81 * n,
                                          'count': 100 + 50 * abs(int(a))})


king.KingAnimation([f], [update], frames=king.linspace(-10, 10, 400), interval=50)
