
INF = 1e6


def get_v_x(t, v_x_0):
    if t > abs(v_x_0):
        return 0

    if v_x_0 > 0:
        return v_x_0 - (t - 1)

    else:
        return v_x_0 + (t - 1)


def get_v_y(t, v_y_0):
    return v_y_0 - (t - 1)


def get_x_positions(v_x_0, target_area):
    _, b = target_area
    x = 0
    t = 0
    positions = [x]
    while True:
        t += 1
        v_x = get_v_x(t, v_x_0)
        x += v_x

        positions.append(x)

        if x < 0 or x > b or v_x == 0:
            break

    return positions


def get_y_positions(v_y_0, target_area):
    a, _ = target_area
    y = 0
    t = 0
    positions = [y]
    while True:
        t += 1
        v_y = get_v_y(t, v_y_0)
        y += v_y

        positions.append(y)

        if y < a:
            break

    return positions


def get_max_y_pos(v_y_0):
    y = 0
    max_pos = -1e6
    t = 0
    while True:
        t += 1
        v_y = get_v_y(t, v_y_0)
        y += v_y
        if y > max_pos:
            max_pos = y
        else:
            break

    return max_pos


def hits_target(positions, target_area):
    a, b = target_area
    for pos in reversed(positions):
        if a <= pos <= b:
            return True

    return False


def get_within_target_times(positions, target_area):
    a, b = target_area
    times = []
    for t, pos in enumerate(positions):
        if a <= pos <= b:
            times.append(t)

    return times


def get_time_lims(positions, target_area):
    times = get_within_target_times(positions, target_area)

    time_min = times[0]
    time_max = times[-1]

    time_max = INF if positions[-2] == positions[-1] else times[-1]

    return time_min, time_max
