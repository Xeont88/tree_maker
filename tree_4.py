def tree_maker(pairs: list):
    tree = {}
    branches = []
    temp = ''
    for parent, child in pairs:
        temp += ''
        if parent == None:
            # tree[child] = dict(temp={})
            tree[child] = {}

        else:
            # tree.update(dict(parent={child: {}}))
            tree[parent] = {child:{}}

    return tree


tree_test = {'a': {'a1': {},'a2': {'a3': {}}},'b': {'b1': {}},'c': {}}


pair_list = [(None, 'a'),
             (None, 'b'),
             (None, 'c'),
             ('a', 'a1'),
             ('a', 'a2'),
             ('b', 'b1'),
             ('a2', 'a3'),
             ]

# data2 = {}
# data = {k: v for k, v in (('a', 1), ('b',2), ('c',3))}
# data2.update({k: v for k, v in pair_list})
#
#
# # for k, v in pair_list:
# #     print(k, v)
#
# # print(data2)

print(tree_maker(pair_list))
