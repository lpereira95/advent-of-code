

def parse_packet(line):
    line = line.replace(' ', '')

    stack = [[]]
    current_object = stack[-1]
    value = ''
    for char_ in line[1:-1]:
        if char_ == "[":
            current_object = []
            stack.append(current_object)

        elif char_ == "]":
            if value:
                current_object.append(int(value))
                value = ''

            last_object = stack.pop()
            stack[-1].append(last_object)
            current_object = stack[-1]

        elif char_ == ",":
            if value:
                current_object.append(int(value))
                value = ''

        else:
            value += char_

    if len(stack) > 1:
        raise Exception("Unable to parse packet")

    packet = stack.pop()
    if value:
        packet.append(int(value))

    return packet


def is_empty_list(ls):
    try:
        ls[0]
        return False
    except IndexError:
        return True


def compare_pair(packet_left, packet_right):
    if type(packet_left) is int and type(packet_right) is int:
        if packet_left < packet_right:
            return 1
        elif packet_left == packet_right:
            return 0

        return -1

    if len(set([type(packet_left), type(packet_right)])) == 2:
        if type(packet_left) is int:
            return compare_pair([packet_left], packet_right)

        return compare_pair(packet_left, [packet_right])

    for packet_left_, packet_right_ in zip(packet_left, packet_right):
        res = compare_pair(packet_left_, packet_right_)
        if res != 0:
            return res

    if len(packet_left) == len(packet_right):
        return 0

    if is_empty_list(packet_left) or len(packet_left) < len(packet_right):
        return 1

    return -1
