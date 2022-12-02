

def _move_forward(value, horiz_pos, depth):
    horiz_pos += value
    return horiz_pos, depth


def _move_down(value, horiz_pos, depth):
    depth += value
    return horiz_pos, depth


def _move_up(value, horiz_pos, depth):
    depth -= value
    return horiz_pos, depth


MAP2ACTION = {
    'forward': _move_forward,
    'down': _move_down,
    'up': _move_up
}


filename = 'input.dat'

with open(filename, 'r') as file:
    instructions = file.readlines()


horiz_pos = 0
depth = 0

for instruction in instructions:
    instruct_ls = instruction.strip().split()
    cmd, value = instruct_ls[0], int(instruct_ls[1])

    horiz_pos, depth = MAP2ACTION[cmd](value, horiz_pos, depth)


print(f'What do you get if you multiply your final horizontal position by your final depth? {horiz_pos*depth}')
