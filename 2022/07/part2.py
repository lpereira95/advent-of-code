
from _utils import Directory


TOTAL_DISK_SPACE = 70000000


def filter_dirs(item, dirs):
    if not isinstance(item, Directory):
        return

    dirs.append(item)
    for item in item.children:
        filter_dirs(item, dirs)


if __name__ == "__main__":
    from _utils import (
        load_data,
        navigate,
        filter_,
    )

    filename = "input.dat"
    terminal_output = load_data(filename)

    root = navigate(terminal_output)

    required_space = 30000000

    free_space = TOTAL_DISK_SPACE - root.size
    missing_space = required_space - free_space

    all_dirs = filter_(root, filter_dirs)
    sorted_dirs = sorted(all_dirs, key=lambda x: x.size)
    for item in sorted_dirs[1:]:
        if item.size > missing_space:
            break

    answer = item.size

    question = "What is the total size of that directory?"

    print(f"{question} {answer}")
