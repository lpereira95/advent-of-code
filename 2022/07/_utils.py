

from abc import ABC, abstractmethod

SPACES = "   "


def load_data(filename):
    with open(filename, "r") as file:
        terminal_output = file.readlines()

    return terminal_output


class Item:
    sep = '/'

    def __init__(self, name):
        self.name = name

        self.parent = None
        self.children = []

    @property
    def path(self):
        if self.parent is None:
            return self.name

        return f"{self.parent.path}{self.sep}{self.name}"

    def add_child(self, child):
        child.set_parent(self)
        self.children.append(child)

    def set_parent(self, parent):
        self.parent = parent

    @property
    def level(self):
        return self.path.count('/') - 1


class Directory(Item):
    def __init__(self, name):
        super().__init__(name)

    @property
    def size(self):
        size = 0
        for child in self.children:
            size += child.size

        return size

    def get_child_by_name(self, name):
        for child in self.children:
            if child.name == name:
                return child

    @property
    def as_str(self):
        spaces = SPACES * self.level
        str_ = f"{spaces}- {self.name} (dir)\n"
        for child in self.children:
            str_ += child.as_str

        return str_


class File(Item):

    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def as_str(self):
        spaces = SPACES * self.level
        return f"{spaces}- {self.name} (file, size={self.size})\n"


class AbstractCmd(ABC):

    @abstractmethod
    def act_on(self, current_folder):
        return current_folder


class Cmd:

    def __new__(self, cmd, terminal_output):
        cmd_name = cmd[2:4]
        if cmd_name == "cd":
            return Cd(cmd.strip().split(' ')[-1])

        if cmd_name == "ls":
            return Ls(terminal_output)

        raise Exception(f"Unknown command: {cmd_name}")


class Cd(AbstractCmd):

    def __init__(self, arg):
        self.arg = arg

    def act_on(self, current_folder):
        if self.arg == "/":
            return get_root(current_folder)

        if self.arg == "..":
            return current_folder.parent

        return current_folder.get_child_by_name(self.arg)


class Ls(AbstractCmd):
    def __init__(self, terminal_output):
        self.terminal_output = terminal_output

    def act_on(self, current_folder):
        for output in self.terminal_output:
            if output.startswith("dir"):
                child = Directory(output.strip().split()[-1])
            else:
                size, name = output.strip().split()
                child = File(name, int(size))

            current_folder.add_child(child)

        return current_folder


def navigate(terminal_output):
    current_folder = Directory("/.")
    pointer = 0

    while pointer < len(terminal_output):
        size = get_cmd_interaction_size(terminal_output[pointer:])
        cmd = get_next_command(terminal_output[pointer:pointer + size])
        current_folder = cmd.act_on(current_folder)
        pointer += size

    return get_root(current_folder)


def get_root(current_folder):
    while True:
        if current_folder.parent is None:
            return current_folder

        current_folder = current_folder.parent


def get_cmd_interaction_size(terminal_output):
    for i, line in enumerate(terminal_output[1:]):
        if line.startswith("$"):
            return i + 1

    return len(terminal_output)


def get_next_command(interaction):
    return Cmd(interaction[0], interaction[1:])


def print_filesystem(root):
    print(root.as_str)


def filter_(root, filter_fnc):
    items = []
    for child in root.children:
        filter_fnc(child, items)

    return items
