
def load_example_data(filename):
    with open(filename, "r") as file:
        sequences = file.readlines()

    return sequences


def load_data(filename):
    with open(filename, "r") as file:
        sequence = file.read()

    return sequence.strip()


def detect_packet(sequence, window_size=4):
    begin = 0
    end = window_size - 1
    while True:
        seq_window = sequence[begin:end]
        character = sequence[end]
        incr = 1
        if character in seq_window:
            incr += seq_window.index(character)
        else:
            if len(set(seq_window)) == (window_size - 1):
                return end + 1

        begin += incr
        end += incr
