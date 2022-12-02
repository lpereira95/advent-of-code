
from _utils import load_data


def _create_pair_counts(formula):

    pair_counts = {}
    for value1, value2 in zip(formula, formula[1:]):
        key = f'{value1}{value2}'
        if key in pair_counts:
            pair_counts[key] += 1
        else:
            pair_counts[key] = 1

    return pair_counts


def _create_extended_rules(rules):

    extended_rules = {}
    for key, value in rules.items():
        extended_rules[key] = (f'{key[0]}{value}', f'{value}{key[1]}')

    return extended_rules


def simulate_step(pair_counts, extended_rules):
    new_pair_counts = pair_counts.copy()
    for pair, counts in pair_counts.items():
        new_pair_counts[pair] -= counts

        new_pairs = extended_rules[pair]
        for new_pair in new_pairs:
            if new_pair in new_pair_counts:
                new_pair_counts[new_pair] += counts
            else:
                new_pair_counts[new_pair] = counts

    return new_pair_counts


def simulate(formula, rules, n_steps):
    pair_counts = _create_pair_counts(template)
    extended_rules = _create_extended_rules(rules)
    for _ in range(n_steps):
        pair_counts = simulate_step(pair_counts, extended_rules)

    return pair_counts


def _get_unique_elements(pair_counts):
    elem_str = ''
    for key in pair_counts:
        elem_str += key

    return set(elem_str)


def get_element_counts(template, pair_counts):
    counts = {}
    for elem in _get_unique_elements(pair_counts):
        counts[elem] = 0
        for key, counts_ in pair_counts.items():
            if elem == key[0]:
                counts[elem] += counts_

    counts[template[-1]] += 1
    return counts


filename = 'input.dat'
template, rules = load_data(filename)

n_steps = 40
pair_counts = simulate(template, rules, n_steps)
counts = get_element_counts(template, pair_counts)


count = [(key, count) for key, count in counts.items()]
sorted_count = sorted(count, key=lambda x: x[1])

diff = sorted_count[-1][1] - sorted_count[0][1]
print(f'What do you get if you take the quantity of the most common element and subtract the quantity of the least common element? {diff}')
