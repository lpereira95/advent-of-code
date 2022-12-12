from _utils import Directory


def filter_dirs_by_max_size(directory, dirs, thresh=100000):
    if not isinstance(directory, Directory):
        return

    if directory.size < thresh:
        dirs.append(directory)

    for child in directory.children:
        filter_dirs_by_max_size(child, dirs, thresh=thresh)


def compute_items_total_size(items):
    size = 0
    for item in items:
        size += item.size

    return size


if __name__ == "__main__":
    from _utils import (
        load_data,
        navigate,
        print_filesystem,
        filter_,
    )

    filename = "input.dat"
    terminal_output = load_data(filename)

    root = navigate(terminal_output)
    print_filesystem(root)

    dirs = filter_(root, filter_dirs_by_max_size)

    answer = compute_items_total_size(dirs)
    question = "What is the sum of the total sizes of those directories?"

    print(f"{question} {answer}")
