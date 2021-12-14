import json


pair_list = [(None, 'a'),
             (None, 'b'),
             (None, 'c'),
             ('a', 'a1'),
             ('a', 'a2'),
             ('b', 'b1'),
             ('a2', 'a3'),
             ]

y = json.dumps(pair_list)

print(y)