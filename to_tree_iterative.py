def build_tree_iter(nodes: dict, current_level: list) -> list:
    next_level = []
    for key, tree_node in current_level:
        tree_node[key] = {item: dict() for item in nodes[key]}
        next_level += [(level, tree_node[key]) for level in nodes[key]]
    return next_level


def to_tree(source: list) -> dict:
    """Function creation tree from pair parent - child"""
    roots = set()
    nodes = {name: set() for pair in source for name in pair if name}
    for parent, child in source:
        if not parent:
            roots.add(child)
            continue
        nodes[parent].add(child)

    # form the top level of the tree
    tree = {root: {} for root in roots}
    # create list with pair: current level - place, where needed to insert child (
    # in first iteration, it's empty dict)
    current_levels = [(root, tree) for root in roots]
    #  while there are levels for a go around
    while current_levels:
        # build levels (tree in `current_levels` - mutable value)
        current_levels = build_tree_iter(nodes, current_levels)

    return tree


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
