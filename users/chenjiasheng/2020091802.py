# http://3ms.huawei.com/km/groups/3803117/blogs/details/9139131?l=zh-cn
from typing import Dict


class Node:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.name_set = set()
        self.children = []


def init_dir_tree(dir_str):
    lines = dir_str.split('\n')
    name_and_level = []
    max_level = 0
    for line in lines:
        level = 0
        s = line
        while s.startswith('|-'):
            level += 1
            s = s[2:]
        name = s
        name_and_level.append((name, level))
        max_level = max(max_level, level)

    root = Node('', -1)
    prev_level = -1
    prev_node_by_level: Dict[int, Node] = {l: 0 for l in range(max_level)}
    prev_node_by_level[-1] = root

    for name, level in name_and_level:
        if level >= prev_level + 2:
            continue
        parent = prev_node_by_level[level - 1]
        if parent is None:
            continue
        if name in parent.name_set:
            continue

        node = Node(name, level)
        parent.children.append(node)
        parent.name_set.add(name)

        prev_node_by_level[level] = node
        prev_level = level

    return root


def del_sub_dir(root, seq):
    for child in root.children:
        del_sub_dir(child, seq)
    seq.append(root)


def del_dir(dir_str):
    root = init_dir_tree(dir_str)
    node_seq = []
    del_sub_dir(root, node_seq)
    return [x.name for x in node_seq]


dir_str = """|-B
A
|-B
|-|-C
|-|-D
|-|-D
|-|-|-|-D
|-|-E
|-|-|-F
|-lib32"""
print(del_dir(dir_str))
