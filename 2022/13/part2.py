from _utils import (
    parse_packet,
    compare_pair,
)


def load_data(filename):
    with open(filename, "r") as file:
        packets = []
        for line in file:
            if line.strip() == "":
                continue

            packets.append(parse_packet(line.strip()))

    return packets


def sort_packets(packets):
    sorted_packets = packets.copy()
    i = 0
    while i < len(packets) - 1:
        packet = sorted_packets[i]
        for cmp_packet in sorted_packets[i + 1:]:
            if compare_pair(packet, cmp_packet) == -1:
                sorted_packets.append(sorted_packets.pop(i))
                break

        else:
            i += 1

    return sorted_packets


def get_divider_packet_index(packets, number):
    for index, packet in enumerate(packets):

        if (not type(packet) is int and len(packet) == 1
                and not type(packet[0]) is int
                and len(packet[0]) == 1
                and packet[0][0] == number):
            return index + 1

    raise Exception("Cannot find divider packet")


def get_distress_signal(packets):
    packets = packets.copy()

    packets.append(parse_packet("[[2]]"))
    packets.append(parse_packet("[[6]]"))

    sorted_packets = sort_packets(packets)

    index_init = get_divider_packet_index(sorted_packets, 2)
    index_end = get_divider_packet_index(sorted_packets, 6)

    return index_init * index_end


if __name__ == "__main__":

    filename = "input.dat"
    packets = load_data(filename)

    answer = get_distress_signal(packets)
    question = "What is the decoder key for the distress signal?"

    print(f"{question} {answer}")
