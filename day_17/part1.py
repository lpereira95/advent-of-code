

from _utils import get_v_y
from _utils import get_max_y_pos


def get_highest_y(target_area_y):
    c, d = target_area_y

    v_y_0 = - 1
    previous_overshoot = 1e6
    while True:
        v_y_0 += 1
        h = get_max_y_pos(v_y_0)

        k = -1
        sum_ = 0
        while True:
            k += 1
            sum_ += k
            if h - d - sum_ <= 0:
                overshoot = h - c - sum_
                if overshoot == 0 and previous_overshoot == overshoot + 1:
                    return v_y_0, h

                previous_overshoot = overshoot
                break


if __name__ == '__main__':
    # x does not really matter (because the conditions allows to stop)

    # target_area = (20, 30), (-10, -5)
    target_area = (34, 67), (-215, -186)

    target_area_x, target_area_y = target_area

    v_y_0, highest_y = get_highest_y(target_area_y)
    print(v_y_0)

    print(f'What is the highest y position it reaches on this trajectory? {highest_y}')
