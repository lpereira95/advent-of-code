

MAP_UNIQUE_NUM_SEG = {
    '1': 2,
    '4': 4,
    '7': 3,
    '8': 7,
}

MAP_UNIQUE_SEG_NUM = {value: key for key, value in MAP_UNIQUE_NUM_SEG.items()}


def load_data(filename, delimiter='|'):

    with open(filename, 'r') as file:
        lines = file.readlines()

    unique_signal_patterns = []
    output_values = []
    for line in lines:
        patterns, output = line.split(delimiter)
        unique_signal_patterns.append(patterns.strip().split())
        output_values.append(output.strip().split())

    return unique_signal_patterns, output_values


def count_uniques(output_values):
    count = 0
    for output_values_ in output_values:
        for output_value in output_values_:
            if len(output_value) in MAP_UNIQUE_SEG_NUM:
                count += 1

    return count


def _get_if_all_in(patterns, signal):

    for pattern in patterns:
        this = True
        for val in signal:
            if val not in pattern:
                this = False

        if this:
            return pattern


def _decode_5(patterns, known_keys):
    key = {}
    pool = patterns.copy()

    # get 3
    key['3'] = _get_if_all_in(patterns, known_keys['7'])
    pool.remove(key['3'])

    # get 5
    c = 0
    for val in pool[0]:
        if val in known_keys['4']:
            c += 1
    if c == 2:
        key['2'] = pool[0]
        key['5'] = pool[1]
    else:
        key['2'] = pool[1]
        key['5'] = pool[0]

    return key


def _decode_6(patterns, known_keys):

    key = {}

    pool = patterns.copy()

    # get 9
    key['9'] = _get_if_all_in(pool, known_keys['4'])
    pool.remove(key['9'])

    # get 0
    key['0'] = _get_if_all_in(pool, known_keys['7'])
    pool.remove(key['0'])

    # get 6
    key['6'] = pool[0]

    return key


def sort_string(string):
    return ''.join(sorted(string))


def get_key(patterns):
    num_pattern = {}

    # decode known lenghts
    for pattern in patterns:
        n = len(pattern)
        if n in MAP_UNIQUE_SEG_NUM:
            num_pattern[MAP_UNIQUE_SEG_NUM[n]] = pattern

    # decode len 5
    patterns_5 = [pattern for pattern in patterns if len(pattern) == 5]
    num_pattern.update(_decode_5(patterns_5, num_pattern))

    # decode len 6
    patterns_6 = [pattern for pattern in patterns if len(pattern) == 6]
    num_pattern.update(_decode_6(patterns_6, num_pattern))

    return num_pattern


def decode_patterns(patterns, outputs):
    num_pattern = get_key(patterns)

    # inverse
    pattern_num = {sort_string(value): key for key, value in num_pattern.items()}

    # decode
    decoded = ''
    for output in outputs:
        decoded += pattern_num[sort_string(output)]

    return decoded
