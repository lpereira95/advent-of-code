
from _utils import get_max_y_pos
from _utils import get_x_positions
from _utils import hits_target
from _utils import get_y_positions
from _utils import get_time_lims


def load_solution(filename):
    with open(filename, 'r') as file:
        sol = []
        for line in file:
            for string in line.strip().split():
                string_ls = string.strip().split(',')

                sol.append((int(string_ls[0]), int(string_ls[1])))

    return sol


def get_valid_v_y_0(target_area_y):
    # assumes target area below 0
    c, d = target_area_y

    # negative
    v_y_0 = c - 1
    valid_pos = []
    while v_y_0 < -1:
        v_y_0 += 1
        pos = 0
        k = -1
        while True:
            k += 1
            pos += v_y_0 - k
            if pos <= d:
                if pos >= c:
                    valid_pos.append(v_y_0)

                break

    # positive
    v_y_0 = -1
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
                if overshoot >= 0:
                    valid_pos.append(v_y_0)

                if overshoot == 0 and previous_overshoot == overshoot + 1:
                    return valid_pos

                previous_overshoot = overshoot
                break


def get_valid_v_x_0(target_area):
    a, b = target_area

    valid_pos = []
    v_x_0 = -1
    while True:
        v_x_0 += 1
        pos_x = get_x_positions(v_x_0, target_area)

        hitted_target = hits_target(pos_x, target_area)
        if hitted_target:
            valid_pos.append(v_x_0)

        if v_x_0 > b:
            break

    return valid_pos


if __name__ == '__main__':
    # target_area = (20, 30), (-10, -5)
    target_area = (34, 67), (-215, -186)

    target_area_x, target_area_y = target_area

    initial_vels_y = get_valid_v_y_0(target_area_y)
    initial_vels_x = get_valid_v_x_0(target_area_x)

    lims_x = []
    for v_x_0 in initial_vels_x:
        positions = get_x_positions(v_x_0, target_area_x)
        lims_x.append(get_time_lims(positions, target_area_x))

    valid_init = []
    for v_y_0 in initial_vels_y:
        positions = get_y_positions(v_y_0, target_area_y)

        t_lims_y = get_time_lims(positions, target_area_y)
        for v_x_0, t_lims_x in zip(initial_vels_x, lims_x):
            if t_lims_x[0] >= t_lims_y[0] and t_lims_x[1] <= t_lims_y[1] \
                    or t_lims_x[0] <= t_lims_y[0] and t_lims_x[1] >= t_lims_y[1] \
                    or t_lims_x[0] == t_lims_y[1] or t_lims_x[1] == t_lims_y[0]:
                valid_init.append((v_x_0, v_y_0))

    print(f'How many distinct initial velocity values cause the probe to be within the target area after any step? {len(valid_init)}')
