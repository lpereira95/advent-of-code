
from _utils import load_data
from _utils import print_paths


class Node:
    type = 'node'

    def __init__(self, name):
        self.name = name
        self.children = []
        self.parents = []

    def add_child(self, child):
        child.parents.append(self)
        self.children.append(child)

    def visit(self, visited=None):
        if visited is None:
            visited = []
        visited = visited.copy()
        visited.append(self.name)

        paths = []
        for child in self.children + self.parents:
            if child.type == 'start' or (child.type == 'small' and child.name in visited):
                continue

            paths_ = child.visit(visited)
            if paths_:
                paths.extend(paths_)

        paths = self._update_paths(paths)

        return [[self.name] + path for path in paths]

    def _update_paths(self, paths):
        return paths


class Start(Node):
    type = 'start'


class End(Node):
    type = 'end'

    def visit(self, *args, **kwargs):
        return [[self.name]]


class LargeCave(Node):
    type = 'large'

    def _update_paths(self, paths):
        not_ret_paths = [path for path in paths if path[-1] != self.name]

        # update returning paths
        ret_paths = [path for path in paths if path[-1] == self.name]

        new_end_paths = []
        for path in ret_paths:
            for cmp_path in not_ret_paths:
                new_end_paths.append(path + cmp_path)

        return not_ret_paths + new_end_paths


class SmallCave(Node):
    type = 'small'


def _init_node(name):

    if name.lower() != name:
        return LargeCave(name)

    if name == 'end':
        return End(name)

    if name == 'start':
        return Start(name)

    return SmallCave(name)


def get_node_list(cave_system):
    nodes = {}
    for line in cave_system:
        parent, child = line

        parent_node = nodes.get(parent, _init_node(parent))
        child_node = nodes.get(child, _init_node(child))

        nodes[parent] = parent_node
        nodes[child] = child_node

        parent_node.add_child(child_node)

    return list(nodes.values())


filename = 'input.dat'
cave_system = load_data(filename)

nodes = get_node_list(cave_system)
for node in nodes:
    if node.type == 'start':
        start = node
        break

paths = start.visit()
print_paths(paths)
print('')

n_paths = len(paths)
print(f'How many paths through this cave system are there that visit small caves at most once? {n_paths}')
