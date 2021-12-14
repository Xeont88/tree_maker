# from tree_1 import search_in_dict


def tree_maker(pairs):
    tree = {}
    branches = []

    for pair in pairs:
        parent, child = pair

        if parent == None:
            tree[child] = {}
            branches.append(child)
        else:
            tree[parent].update(child)
    return tree



pair_list = [(None, 'a'),
             (None, 'b'),
             (None, 'c'),
             ('a', 'a1'),
             ('a', 'a2'),
             ('b', 'b1'),
             ('a2', 'a3'),
             ]


print(tree_maker(pair_list))



