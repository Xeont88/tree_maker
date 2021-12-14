def tree_maker(pairs: list):
    tree = {}
    branches = set()

    for pair in pairs:
        parent, child = pair
        if parent == None:
            tree[child] = {}
            branches.add(child)
            continue

        if child not in branches:
            # tree[child] = {}
            tree.update({parent: child})

    return tree


pair_list = [(None, 'a'),
             (None, 'b'),
             (None, 'c'),
             ('a', 'a1'),
             ('a', 'a2'),
             ('b', 'b1'),
             ('a2', 'a3'),
             ]

dict_ = {
    'a': {
        'a1': {},
        'a2': {
            'a3': {}
        }
    },
    'b': {
        'b1': {}
    },
    'c': {}
}

# pairs = [(None, 'a0'),] + [(f'a{i}', f'a{i + 1}') for i in range(999)]


def search_in_dict(key: str, dictionary: dict):
    print(dictionary.keys())
    if key not in dictionary.keys():

        for k in dictionary.keys():
            # print('k', k, dictionary.keys())

            if key == k:
                return k
            else:
                search_in_dict(key, dictionary[k])
    else:
        for k in dictionary.keys():
            # print('k2', k, dictionary)
            return True

    # print(keys_list)


print(search_in_dict('b1', dict_))
# print(tree_maker(pair_list))
