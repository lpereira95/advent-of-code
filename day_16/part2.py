
from _utils import get_packet
from _utils import get_lims
from _utils import get_type


def _evaluate_0(packet, hierarchy, lims):
    subpacket_lims = hierarchy[lims]
    sum_ = 0
    for subpacket_lim in subpacket_lims:
        sum_ += evaluate(packet, hierarchy, subpacket_lim)

    return sum_


def _evaluate_1(packet, hierarchy, lims):
    subpacket_lims = hierarchy[lims]
    prod = 1
    for subpacket_lim in subpacket_lims:
        prod *= evaluate(packet, hierarchy, subpacket_lim)

    return prod


def _evaluate_2(packet, hierarchy, lims):
    subpacket_lims = hierarchy[lims]
    min_ = 1e6
    for subpacket_lim in subpacket_lims:
        val = evaluate(packet, hierarchy, subpacket_lim)
        if val < min_:
            min_ = val

    return min_


def _evaluate_3(packet, hierarchy, lims):
    subpacket_lims = hierarchy[lims]
    max_ = 0
    for subpacket_lim in subpacket_lims:
        val = evaluate(packet, hierarchy, subpacket_lim)
        if val > max_:
            max_ = val

    return max_


def _evaluate_4(packet, hierarchy, lims):
    # args for consistency
    # assumes it has no children
    start, end = lims
    pointer = start + 6
    bin_str = ''
    while True:

        val = packet[pointer]
        pointer += 1
        bin_str += packet[pointer:pointer + 4]
        pointer += 4

        if val == '0':
            break

    return int(bin_str, 2)


def _evaluate_logical(packet, hierarchy, lims, fnc):
    subpacket_lims = hierarchy[lims]

    value_0 = evaluate(packet, hierarchy, subpacket_lims[0])
    value_1 = evaluate(packet, hierarchy, subpacket_lims[1])

    if fnc(value_0, value_1):
        return 1

    return 0


def _evaluate_5(packet, hierarchy, lims):
    return _evaluate_logical(packet, hierarchy, lims,
                             lambda x, y: x > y)


def _evaluate_6(packet, hierarchy, lims):
    return _evaluate_logical(packet, hierarchy, lims,
                             lambda x, y: x < y)


def _evaluate_7(packet, hierarchy, lims):
    return _evaluate_logical(packet, hierarchy, lims,
                             lambda x, y: x == y)


def evaluate(packet, hierarchy, lims):
    type_ = get_type(packet, lims[0])
    fnc = eval(f'_evaluate_{type_}')

    val = fnc(packet, hierarchy, lims)

    return val


def hierarchize(lims):

    hierarchy = {}
    children_pool = lims.copy()
    for lim in reversed(lims):
        start, end = lim
        hierarchy[lim] = []
        for cmp_lim in children_pool.copy():
            if start <= cmp_lim[0] <= end and start <= cmp_lim[1] <= end:
                if lim == cmp_lim:
                    continue

                hierarchy[lim].append(cmp_lim)
                children_pool.remove(cmp_lim)

    return hierarchy


def get_root_key(lims):
    for lim in lims:
        if lim[0] == 0:
            return lim


if __name__ == '__main__':

    from input import MAIN as HEXA_STR

    packet = get_packet(HEXA_STR)

    n = len(packet)
    lims = get_lims(packet, 0, n)

    hierarchy = hierarchize(lims)
    root_lims = get_root_key(hierarchy)

    value = evaluate(packet, hierarchy, root_lims)

    print(f'What do you get if you evaluate the expression represented by your hexadecimal-encoded BITS transmission? {value}')
