def tree_maker(pairs: list):
    '''
    Creates a dictionary tree from a list of pairs (parent, child)

    :param pairs: takes list of tuples
    :return: dictionary of branches (tree)

    '''

    tree = {}
    for parent, child in pairs:
        if parent == None:
            tree[child] = {}
        else:
            tree[parent].update({child: {}})
    return tree


pair_list = [(None, 'a'),
             (None, 'b'),
             (None, 'c'),
             ('a', 'a1'),
             ('a', 'a2'),
             ('b', 'b1'),
             # ('a2', 'a3'),
             ]

if __name__ == '__main__':
    a = tree_maker(pair_list)
    print(a)
