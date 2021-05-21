import king
import threading
import time

n = 8

f = king.KingFunction(essential_data={'function': lambda x: 1, 'x_min': None, 'x_max': None, 'count': None})


def gen_heart(a, x):
    return abs(x) ** (2 / 3) + 0.9 * (3.3 - x ** 2) ** 0.5 * king.sin(a * king.pi * x)


def update_f(a):
    f.update_affected(new_essential_data={'function': lambda x: n * gen_heart(a, x / n),
                                          'x_min': -1.81 * n,
                                          'x_max': 1.81 * n,
                                          'count': 100 + 50 * abs(int(a))})


def update(n):
    for frame in king.linspace(-10, 10, 100):
        update_f(frame)
        time.sleep(0.02)


t = threading.Thread(target=update, args=('1',))
t.start()
# t.setDaemon(True)
t.join()
