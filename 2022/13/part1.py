from _utils import (
    parse_packet,
    compare_pair,
)


def load_data(filename):
    with open(filename, "r") as file:
        packets = []
        pair = []
        for line in file:
            if line.strip() == "":
                packets.append(pair)
                pair = []
                continue

            pair.append(parse_packet(line.strip()))

        packets.append(pair)

    return packets


def get_packets_in_right_order(packets):
    indices = []
    for i, (packet_left, packet_right) in enumerate(packets):
        if compare_pair(packet_left, packet_right) > -1:
            indices.append(i + 1)

    return indices


if __name__ == "__main__":

    filename = "input.dat"
    packets = load_data(filename)

    indices = get_packets_in_right_order(packets)

    answer = sum(indices)
    question = "What is the sum of the indices of those pairs?"

    print(f"{question} {answer}")
