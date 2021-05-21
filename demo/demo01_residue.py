import king


def func_generator(point_list, power_list):
    def f(z):
        count = len(point_list)
        result = 1
        for i in range(count):
            x, y = point_list[i].basic_data
            result *= (z - (x + y * 1j)) ** power_list[i]
        return result

    return f


@king.geometry_generate(cls=king.KingPoint)
def point_image(depends=(), essential_data=None):
    x, y = depends[0].basic_data
    z = x + y * 1j
    f = essential_data[0]
    result = f(z)
    return result.real, result.imag


@king.geometry_generate(cls=king.KingPoint)
def point_on_circle(depends=(), essential_data=None):
    x, y = depends[0].basic_data
    r = depends[1].basic_data[1]
    dis = king.get_distance_by_tow_point(0, 0, x, y)

    return [x / dis * r, y / dis * r]


p_free = king.point(5, 5, color='red')
p_on_circle = king.point(0, 3)
o = king.point(0, 0)
o.set_visible(False)

p_list = king.point(p_list=[[3, 5], [-3, 2], [0, 4], [-3, -2]])

my_pow_list = [1, 2, -3, -2]

for index in range(len(p_list)):
    p_list[index].set_markerfacecolor('black')
    p_list[index].text.set_text(my_pow_list[index])

p_image = point_image(depends=[p_free], essential_data=[func_generator(p_list, my_pow_list)])
point_on_circle(depends=[p_image, king.circle_center_edge_point(depends=[o, p_on_circle])])
