import unittest
import tree_5

class TestTree(unittest.TestCase):

    def test_tree_maker(self):
        self.assertEqual(tree_5.tree_maker(self.pair_list), self.pair_list)

    pair_list = [(None, 'a'),
                 (None, 'b'),
                 (None, 'c'),
                 ('a', 'a1'),
                 ('a', 'a2'),
                 ('b', 'b1'),
                 # ('a2', 'a3'),
                 ]


if __name__ == '__main__':
    # test = TestTree()
    # pair_list = [(None, 'a'),
    #          (None, 'b'),
    #          (None, 'c'),
    #          ('a', 'a1'),
    #          ('a', 'a2'),
    #          ('b', 'b1'),
    #          # ('a2', 'a3'),
    #             ]
    # test.test_tree_maker(pair_list)
    unittest.main()
