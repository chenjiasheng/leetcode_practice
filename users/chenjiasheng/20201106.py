# http://3ms.huawei.com/km/groups/3803117/blogs/details/9328645?l=zh-cn

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.weight = 0
        self.index = -1


def get_weight(root):
    if root is None:
        return 0
    n = root
    n.weight = get_weight(n.left) + get_weight(n.right)
    return n.weight


def find_node(root, weight):
    n = root
    if n.weight == weight:
        return n
    elif n.weight < weight:
        return None
    else:
        return find_node(n.left, weight) or find_node(n.right, weight)


def split_tree(root):
    root_weight = get_weight(root)
    if root_weight % 2 != 0:
        return -1

    node = find_node(root, root_weight // 2)
    if node is None:
        return -1

    return node.index

