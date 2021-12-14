def tree_maker(pairs: list):
    '''
    Creates a dictionary tree from a list of pairs (parent, child)

    :param pairs: takes list of tuples
    :return: dictionary of branches (tree)

    '''

    def update_tree(tree, parent, child):
        tree[parent].update({child: {}})

        return tree

    tree = {}
    for parent, child in pairs:
        if parent == None:
            tree[child] = {}
        else:
            # tree[parent].update({child: {}})
            tree = update_tree(tree, parent, child)
    return tree


pair_list = [(None, 'a'),
             (None, 'b'),
             (None, 'c'),
             ('a', 'a1'),
             ('a', 'a2'),
             ('b', 'b1'),
             # ('a2', 'a3'),
             ]

a = tree_maker(pair_list)
print(a)
