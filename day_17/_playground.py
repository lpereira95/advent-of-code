

from _utils import get_y_positions
from _utils import get_x_positions
from _utils import get_time_lims
from _utils import hits_target


def get_valid_v_0(target_area, axis):
    # does not work properly
    a, b = target_area

    valid_pos = []
    for sign in [-1, 1]:
        v_x_0 = -1 if sign else 0
        valid_pos_sign = []
        while True:
            v_x_0 += sign
            if axis == 0:
                pos_x = get_x_positions(v_x_0, target_area)
            else:
                pos_x = get_y_positions(v_x_0, target_area)

            hitted_target = hits_target(pos_x, target_area)
            if hitted_target:
                valid_pos_sign.append(v_x_0)

            if valid_pos_sign and not hitted_target or axis == 0 and pos_x[-1] < 0:
                break
        valid_pos.extend(valid_pos_sign)

    return valid_pos


def get_highest_y_vels(target_area):
    target_area_x, target_area_y = target_area
    initial_vels_y = get_valid_v_0(target_area_y, 1)
    initial_vels_x = get_valid_v_0(target_area_x, 0)

    for v_y_0 in reversed(initial_vels_y):
        pos_y = get_y_positions(v_y_0, target_area_y)
        t_lims_y = get_time_lims(pos_y, target_area_y)
        for v_x_0 in initial_vels_x:
            pos_x = get_x_positions(v_x_0, target_area_x)
            t_lims_x = get_time_lims(pos_x, target_area_x)

            if t_lims_x[0] >= t_lims_y[0] and t_lims_x[1] <= t_lims_y[1] or t_lims_x[0] <= t_lims_y[0] and t_lims_x[1] >= t_lims_y[1]:
                return v_x_0, v_y_0


def sum_natural_nums(n):
    sum_ = 0
    for k in range(1, n + 1):
        sum_ += k

    return sum_


if __name__ == '__main__':
    # x does not really matter (because the conditions allows to stop)

    target_area = (20, 30), (-10, -5)
    # # target_area = (34, 67), (-215, -186)

    target_area_x, target_area_y = target_area

    v_0 = get_highest_y_vels(target_area)

    v_y_0 = v_0[1]
    pos_y = get_y_positions(v_y_0, target_area_y)

    print(f'v_0: {v_0}')

    print('x...')
    v_x_0 = v_0[0]
    pos_x = get_x_positions(v_x_0, target_area_x)
    print(pos_x)
    time_lims = get_time_lims(pos_x, target_area_x)
    print(time_lims)

    print('y...')
    print(pos_y)
    print(hits_target(pos_y, target_area_y))
    time_lims = get_time_lims(pos_y, target_area_y)
    print(time_lims)

    print(f'What is the highest y position it reaches on this trajectory? {max(pos_y)}')
