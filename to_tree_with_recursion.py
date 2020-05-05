def build_tree(nodes: dict, levels: set, tree: dict):
    """Recursive graph traversal for the build tree"""
    for level in levels:
        tree[level] = build_tree(nodes, nodes[level], {})
    return tree


def to_tree(source: list) -> dict:
    """Function creation tree from pair parent - child"""
    roots = set()
    nodes = {name: set() for pair in source for name in pair if name}
    for parent, child in source:
        if not parent:
            roots.add(child)
            continue
        nodes[parent].add(child)

    return build_tree(nodes=nodes, levels=roots, tree={})


if __name__ == '__main__':
    source = [
        (None, 'a'),
        (None, 'b'),
        (None, 'c'),
        ('a', 'a1'),
        ('a', 'a2'),
        ('a2', 'a21'),
        ('a2', 'a22'),
        ('b', 'b1'),
        ('b1', 'b11'),
        ('b11', 'b111'),
        ('b', 'b2'),
        ('c', 'c1'),
    ]
    expected = {
        'a': {'a1': {}, 'a2': {'a21': {}, 'a22': {}}},
        'b': {'b1': {'b11': {'b111': {}}}, 'b2': {}},
        'c': {'c1': {}},
    }
    result = to_tree(source)
    print(result)
    assert result == expected
