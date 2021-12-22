

def _move_forward(value, horiz_pos, depth, aim):
    horiz_pos += value
    depth += aim * value
    return horiz_pos, depth, aim


def _move_down(value, horiz_pos, depth, aim):
    aim += value
    return horiz_pos, depth, aim


def _move_up(value, horiz_pos, depth, aim):
    aim -= value
    return horiz_pos, depth, aim


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
aim = 0

for instruction in instructions:
    instruct_ls = instruction.strip().split()
    cmd, value = instruct_ls[0], int(instruct_ls[1])

    horiz_pos, depth, aim = MAP2ACTION[cmd](value, horiz_pos, depth, aim)


print(f'What do you get if you multiply your final horizontal position by your final depth? {horiz_pos*depth}')
