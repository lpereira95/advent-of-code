
from _utils import get_packet
from _utils import get_lims
from _utils import get_type


def get_version(packet, pointer=0):
    return int(packet[pointer:pointer + 3], 2)


if __name__ == '__main__':

    from input import EXAMPLE_1 as HEXA_STR

    verbose = True

    packet = get_packet(HEXA_STR)

    n = len(packet)
    lims = get_lims(packet, 0, n)

    versions = [get_version(packet, lim[0]) for lim in lims]

    if verbose:
        print(f'Packet size: {n}')
        print(lims)

        print(versions)

        types = [get_type(packet, lim[0]) for lim in lims]
        print(types)

    print()
    sum_ = sum(versions)
    print(f'What do you get if you add up the version numbers in all packets? {sum_}')
