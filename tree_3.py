pair_list = [(None, 'a'),
             (None, 'b'),
             (None, 'c'),
             ('a', 'a1'),
             ('a', 'a2'),
             ('b', 'b1'),
             ('a2', 'a3'),
             ]

def tree_maker(pairs: list):
    tree = {}
    branches = []

    for pair in pairs[::-1]:
        parent, child = pair

        if not parent == None:
            tree[parent] = child
        else:
            pass

        if len(pairs):
            pairs.pop()
        tree_maker(pairs)

    return tree


print(tree_maker(pair_list))
