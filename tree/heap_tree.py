# TODO
# - iterable
# - is_heap
# - is_shaped
# - pydoc

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
        self.remove(self.root.value)
        return res

    def contains(self, value):
        if self.get_node(node_value = value) != None:
            return True
        else:
            return False

    def merge(self, tree2):
        # NOTE: merge algorithm is simple, takes O(len(tree2) * log(depth(tree1)))
        while tree2.node_num != 0:
            self.add(tree2.pop_root())
        # TODO: O(2**(log(n/m))*log(depth(tree1))) algorithm
        # assume self > tree2
#        if self.node_num > tree2.node_num:
        # select new root from tree2
        # create new tree (root, self, tree2) and do down heap
        # while self and tree2 are not shaped
        # move nodes


    def remove(self, value):
        target = self.get_node(node_value = value)
        if target == None:
            return
        elif target == self.root and target.left == None: # NOTE: target is root and has no child
            self.root = HeapTree.Node()
            assert self.node_num == 1, "Error! invalid node number!"
            self.node_num = self.node_num - 1
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
                self.add(j)

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

    def bfs_iter(self):
        return HeapTreeIterator(self)

    __iter__ = bfs_iter

    def dfs_iter(self, current = None):
        if current == None:
            current = self.root
        yield current
        if current.left != None:
            for i in self.dfs_iter(current.left):
                yield i
        if current.right != None:
            for i in self.dfs_iter(current.right):
                yield i
        raise StopIteration

    def is_heap(self):
        pass

    def is_shaped(self):
        pass

    def copy(self):
        pass

    class Node():
        def __init__(self, value=None, parent=None):
            self.value = value
            self.left = None
            self.right = None
            self.parent = parent

class HeapTreeIterator():
    def __init__(self, tree):
        self._tree = tree
        self._stack  = []
        self._stack.append(self._tree.root)

    def __iter__(self):
        return self

    def __next__(self):
        if self._stack != []:
            current = self._stack.pop(0)
            if current.left != None:
                self._stack.append(current.left)
            if current.right != None:
                self._stack.append(current.right)
            return current
        else:
            raise StopIteration
    next = __next__

