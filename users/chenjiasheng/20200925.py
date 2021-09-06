# http://3ms.huawei.com/km/groups/3803117/blogs/details/9154435?l=zh-cn
from typing import List, Optional


class Node:
    def __init__(self, bit):
        self.bit = bit
        self.children: List[Optional[Node]] = [None, None]
        self.string = ''


def parse_bin(num):
    bin_str = bin(num)[2:]
    return [0] * (8 - len(bin_str)) + [int(c) for c in bin_str]

def parse_ip(ip):
    nums = ip.split('.')
    nums = [int(num) for num in nums]
    bits = [x for num in nums for x in parse_bin(num)]
    return bits

def parse_route(route):
    ip, mask = route.split('/')
    mask = int(mask)
    bits = parse_ip(ip)
    return bits[:mask]


def build_trie(routes):
    root = Node(0)
    for route in routes:
        prefix = parse_route(route)
        n = root
        for bit in prefix:
            if n.children[bit] is None:
                n.children[bit] = Node(bit)
            n = n.children[bit]
        if not n.string:
            n.string = route
    return root


def find_trie(trie, dest_ip):
    n = trie
    bits = parse_ip(dest_ip)
    longest_route = trie if trie.string else None
    for bit in bits:
        if n.children[bit] is None:
            break
        n = n.children[bit]
        if n.string:
            longest_route = n
    return longest_route


def find_route(routes, dest_ip):
    trie = build_trie(routes)
    node = find_trie(trie, dest_ip)
    if node is None:
        return 'empty'
    else:
        return node.string


def main():
    dest_ip = '192.168.0.3'
    routes = """
        0.0.0.0/0
        10.166.50.0/23
        192.0.0.0/8
        10.255.255.255/32
        192.168.0.1/23
        127.0.0.0/8
        192.168.0.0/24
    """.strip().split('\n')
    routes = list(filter(bool, map(str.strip, routes)))
    print(find_route(routes, dest_ip))


main()