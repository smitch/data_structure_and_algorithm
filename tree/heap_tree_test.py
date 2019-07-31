import unittest
from heap_tree import *

class HeapTreeTest(unittest.TestCase):
    def test_dump(self):
        tree = HeapTree()
        for i in range(16):
            tree.add(16-i)

        self.assertEqual(tree.to_list(), [[1], [2, 3], [7, 8, 6, 4], [10, 13, 14, 9, 15, 11, 12, 5], [16, None]])

        expect_list = [1, 2, 3, 7, 8, 6, 4, 10, 13, 14, 9, 15, 11, 12, 5, 16, None]
        for i in range(16):
            ans = tree.get_node(node_id = i+1).value
            self.assertEqual(expect_list[i], ans)

        expect_list = [[[1], [2, 3], [7, 8, 6, 4], [10, 13, 14, 9, 15, 11, 12, 5], [16, None]],
                       [[2], [7, 3], [10, 8, 6, 4], [16, 13, 14, 9, 15, 11, 12, 5]],
                       [[3], [7, 4], [10, 8, 6, 5], [16, 13, 14, 9, 15, 11, 12, None]],
                       [[4], [7, 5], [10, 8, 6, 12], [16, 13, 14, 9, 15, 11]],
                       [[5], [7, 6], [10, 8, 11, 12], [16, 13, 14, 9, 15, None]],
                       [[6], [7, 11], [10, 8, 15, 12], [16, 13, 14, 9]],
                       [[7], [8, 11], [10, 9, 15, 12], [16, 13, 14, None]],
                       [[8], [9, 11], [10, 14, 15, 12], [16, 13]],
                       [[9], [10, 11], [13, 14, 15, 12], [16, None]],
                       [[10], [13, 11], [16, 14, 15, 12]],
                       [[11], [13, 12], [16, 14, 15, None]],
                       [[12], [13, 15], [16, 14]],
                       [[13], [14, 15], [16, None]],
                       [[14], [16, 15]],
                       [[15], [16, None]],
                       [[16]]]
        for i in range(16):
            self.assertEqual(expect_list[i], tree.to_list())
            tree.pop_root()
        self.assertEqual([[None]], tree.to_list())

    def test_add(self):
        tree = HeapTree()
        expect = [[1], [2, 3]]
        tree.add(1)
        tree.add(2)
        tree.add(3)
        self.assertEqual(expect, tree.to_list())

    def test_pop_root(self):
        tree = HeapTree()
        values = [1, 2, 3, 4, 5, 3, 3]
        for i in values:
            tree.add(i)
        self.assertEqual(1, tree.pop_root())
        self.assertEqual(2, tree.pop_root())
        self.assertEqual(3, tree.pop_root())

        self.assertEqual(3, tree.get_node(node_value = 3).value)
        self.assertEqual(None, tree.get_node(node_value = 10))
        self.assertTrue(tree.contains(3))
        self.assertFalse(tree.contains(10))

    def test_restore(self):
        tree = HeapTree()
        tree.restore([[1], [2, 3], [7, 8, 6, 4], [10, 13, 14, 9, 15, 11, 12, 5], [16, None]])
        expect = [[1], [2, 3], [7, 8, 6, 4], [10, 13, 14, 9, 15, 11, 12, 5], [16, None]]
        self.assertEqual(expect, tree.to_list())

    def test_get_node(self):
        tree = HeapTree()
        values = [1, 2, 3]
        for i in values:
            tree.add(i)
        self.assertEqual(3, tree.get_node(node_value = 3).value)
        self.assertEqual(2, tree.get_node(node_value = 2).value)
        self.assertEqual(1, tree.get_node(node_value = 1).value)
        self.assertEqual(None, tree.get_node(node_value = 10))
        self.assertTrue(tree.contains(3))
        self.assertFalse(tree.contains(10))

    def test_remove(self):
        tree = HeapTree()
        values = [1, 2, 3, 4, 5, 3, 3]
        expect_list = [[[1], [2, 3], [4, 5, 3, 3]],
                       [[1], [3, 3], [4, 5, 3, None]],
                       [[1], [3, 3], [4, 5]],
                       [[1], [3, 5], [4, None]],
                       [[1], [4, 5]],
                       [[4], [5, None]],
                       [[4]],
                       [[None]]]
        self.assertEqual(0, tree.node_num)
        for i in values:
            tree.add(i)
        self.assertEqual(expect_list[0], tree.to_list())
        self.assertEqual(7, tree.node_num)
        tree.remove(2)
        self.assertEqual(expect_list[1], tree.to_list())
        tree.remove(3)
        self.assertEqual(expect_list[2], tree.to_list())
        tree.remove(3)
        self.assertEqual(expect_list[3], tree.to_list())
        tree.remove(3)
        self.assertEqual(expect_list[4], tree.to_list())
        tree.remove(1)
        self.assertEqual(expect_list[5], tree.to_list())
        tree.remove(1) # NOTE: no node removed
        self.assertEqual(expect_list[5], tree.to_list())
        tree.remove(5)
        self.assertEqual(expect_list[6], tree.to_list())
        self.assertEqual(1, tree.node_num)
        tree.remove(4)
        self.assertEqual(expect_list[7], tree.to_list())
        self.assertEqual(0, tree.node_num)

    def test_merge(self):
        tree1 = HeapTree()
        t1 = [1, 2, 3]
        for i in t1:
            tree1.add(i)
        tree2 = HeapTree()
        t2 = [4, 5]
        for i in t2:
            tree2.add(i)
        tree1.merge(tree2)
        expect = [[1], [2, 3], [4, 5]]
        self.assertEqual(expect, tree1.to_list())

    def test_iterator(self):
        tree = HeapTree()
        # t = [1]
        t = [1, 2, 3]
        for i in t:
            tree.add(i)
        ans = []
        for i in tree:
            ans.append(i.value)
        expect = [1, 2, 3]
        self.assertEqual(expect, ans)

        tree = HeapTree()
        tree.restore([[1], [2, 3], [7, 8, 6, 4], [10, 13, 14, 9, 15, 11, 12, 5], [16, None]])
        expect = [1, 2, 3, 7, 8, 6, 4, 10, 13, 14, 9, 15, 11, 12, 5, 16]
        ans = []
        for i in tree:
            ans.append(i.value)
        self.assertEqual(expect, ans)

        ans = []
        expect = [None]
        tree = HeapTree()
        for i in tree:
            ans.append(i.value)
        self.assertEqual(expect, ans)

    def test_dfs(self):
        tree = HeapTree()
        t = [1, 2, 3]
        for i in t:
            tree.add(i)
        ans = []
        for i in tree.dfs_iter():
            ans.append(i.value)
        expect = [1, 2, 3]
        self.assertEqual(expect, ans)

        tree = HeapTree()
        tree.restore([[1], [2, 3], [7, 8, 6, 4], [10, 13, 14, 9, 15, 11, 12, 5], [16, None]])
        expect = [1, 2, 7, 10, 16, 13, 8, 14, 9, 3, 6, 15, 11, 4, 12, 5]
        ans = []
        for i in tree.dfs_iter():
            ans.append(i.value)
        self.assertEqual(expect, ans)

        ans = []
        expect = [None]
        tree = HeapTree()
        for i in tree:
            ans.append(i.value)
        self.assertEqual(expect, ans)

if __name__ == "__main__":
    unittest.main()
