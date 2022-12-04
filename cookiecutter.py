import shutil
import os

TEMPLATE_FOLDER = "template"


def copy_template_folder(new_location):
    shutil.copytree(TEMPLATE_FOLDER, new_location)


def _get_last_number(aoc_location):
    numbers = []
    for path in os.listdir(aoc_location):
        if not os.path.isdir(path):
            pass

        numbers.append(int(os.path.split(path)[-1]))

    return max(numbers)


def get_new_folder_name(aoc_location):
    last_number = _get_last_number(aoc_location)

    number_str = f'{last_number+1}'.zfill(2)
    return f"{aoc_location}{os.sep}{number_str}"


def duplicate_part(new_location):
    part_name = os.path.join(new_location, "part.py")

    part2_name = os.path.join(new_location, "part2.py")
    shutil.copyfile(part_name, part2_name)

    part1_name = os.path.join(new_location, "part1.py")
    shutil.move(part_name, part1_name)


if __name__ == "__main__":
    aoc_location = "2022"

    new_location = get_new_folder_name(aoc_location)

    copy_template_folder(new_location)
    duplicate_part(new_location)

    print(f"Created {new_location}")
