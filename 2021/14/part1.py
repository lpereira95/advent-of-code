
from _utils import load_data


def polymerize(formula, rules):
    to_insert = ""
    for val1, val2 in zip(formula, formula[1:]):
        to_insert += rules[f'{val1}{val2}']

    new_formula = ''
    for val, new_val in zip(formula, to_insert):
        new_formula += f'{val}{new_val}'
    new_formula += formula[-1]

    return new_formula


def simulate(template, rules, n_steps):

    formula = template
    for i in range(n_steps):
        formula = polymerize(formula, rules)

    return formula


filename = 'input_example.dat'
template, rules = load_data(filename)


n_steps = 10
formula = simulate(template, rules, n_steps)

count = [(key, formula.count(key)) for key in set(formula)]
sorted_count = sorted(count, key=lambda x: x[1])
print(sorted_count)


diff = sorted_count[-1][1] - sorted_count[0][1]
print(f'What do you get if you take the quantity of the most common element and subtract the quantity of the least common element? {diff}')
