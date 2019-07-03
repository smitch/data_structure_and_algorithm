import unittest
import math

class HeapTree():
    def __init__(self):
        self.root = HeapTree.Node()
        self.node_num = 0

    def add(self, value):
        if value == None:
            return

        if self.node_num == 0:
            self.root.value = value
            self.node_num = self.node_num + 1
            return

        parent = self.get_node(node_id = (self.node_num + 1) / 2)
        self.node_num = self.node_num + 1

        current = HeapTree.Node(value, parent)
        if (self.node_num % 2) == 0:
            parent.left = current
        else:
            parent.right = current

        is_inversed = True
        while is_inversed and current.parent != None:
            if current.value < current.parent.value:
                tmp = current.value
                current.value = current.parent.value
                current.parent.value = tmp
                current = current.parent
            else:
                is_inversed = False

    def get_node(self, node_id = None, node_value = None):
        if node_id == None and node_value == None:
            return None
        assert node_id == None or node_value == None, "get_node: specifying both node_id and node_value is not supported!"

        if node_id != None:
            if self.node_num + 1 < node_id or node_id < 1: # NOTE: node id of root is 1
                return None
            direction = [] # NOTE: 0 for left, 1 for right
            while node_id != 1:
                direction.append(node_id % 2)
                node_id = node_id / 2

            current = self.root
            for i in range(len(direction)):
                if direction.pop() == 0:
                    current = current.left
                else:
                    current = current.right
            return current

        else: # NOTE: node_value != None
            stack  = []
            stack.append(self.root)
            while stack != []:
                current = stack.pop()
                if current.value == node_value:
                    return current
                else:
                    if current.left != None:
                        stack.append(current.left)
                    if current.right != None:
                        stack.append(current.right)
            return None # NOTE: no node has node_value

    def pop_root(self):
        assert self.root != None, "error! root is None" # NOTE: tree has at least one Node as dummy root
        res = self.root.value
        if self.root.left == None:
            self.root = HeapTree.Node()
            return res
        self.remove(self.root.value)
        return res

    def contains(self, value):
        if self.get_node(node_value = value) != None:
            return True
        else:
            return False

    def merge_tree(self, tree2):
        # assume self > tree2
        # select new root from tree2
        # create new tree (root, self, tree2) and do down heap
        # while self and tree2 are not shaped
        # move nodes
        pass

    def remove(self, value):
        target = self.get_node(node_value = value)
        if target == None:
            return
        elif target == self.root and target.left == None: # NOTE: target is root and has no child
            self.root = HeapTree.Node()
            return
        else:
            last_node = self.get_node(node_id = self.node_num)
            target.value = last_node.value
            if self.node_num % 2 == 0:
                last_node.parent.left = None
            else:
                last_node.parent.right = None
            self.node_num = self.node_num - 1

            current = target
            is_inversed = True
            while current.left != None and is_inversed:
                is_inversed = False
                if current.right != None:
                    if current.left.value < current.right.value:
                        if current.value > current.left.value:
                            tmp = current.value
                            current.value = current.left.value
                            current.left.value = tmp
                            current = current.left
                            is_inversed = True
                    else:
                        if current.value > current.right.value:
                            tmp = current.value
                            current.value = current.right.value
                            current.right.value = tmp
                            current = current.right
                            is_inversed = True
                else:
                    # NOTE: left node is the last node
                    if current.left.value < current.value:
                        tmp = current.value
                        current.value = current.left.value
                        current.left.value = tmp
                        current = current.left

    def restore(self, tree_list):
        for i in tree_list:
            for j in i:
                # print j
                self.add(j)
                # self.dump()

    def dump(self):
        print self

    def __str__(self):
        return str(self.to_list())

    def to_list(self):
        current = []
        current.append(self.root)
        depth = 0
        value_list = []
        while current != []:
            s = []
            value_list.append([])
            for node in current:
                value_list[depth].append(node.value)
                if node.left != None:
                    s.append(node.left)
                    if node.right != None:
                        s.append(node.right)
                    else:
                        s.append(HeapTree.Node()) # NOTE: add dummy node to print None
                else:
                    assert node.right == None, "error! tree is not shaped"
            current = s
            depth = depth + 1
        return value_list

    class Node():
        def __init__(self, value=None, parent=None):
            self.value = value
            self.left = None
            self.right = None
            self.parent = parent

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

        tree.pop_root()
        expect = [[2], [3, None]]
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

    def test_remove(self):
        tree = HeapTree()
        values = [1, 2, 3, 4, 5, 3, 3]
        expect_list = [[[1], [2, 3], [4, 5, 3, 3]],
                       [[1], [3, 3], [4, 5, 3, None]],
                       [[1], [3, 3], [4, 5]],
                       [[1], [3, 5], [4, None]],
                       [[1], [4, 5]],
                       [[4], [5, None]]]
        for i in values:
            tree.add(i)
        self.assertEqual(expect_list[0], tree.to_list())
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


if __name__ == "__main__":
    # HeapTree.test()
    unittest.main()
