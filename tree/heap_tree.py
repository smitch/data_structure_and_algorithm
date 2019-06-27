import math

class HeapTree():
    def __init__(self):
        self.root = HeapTree.Node()
        self.node_num = 0

    def add(self, value):
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
        res = self.root.value
        current = self.root
        depth = math.ceil(math.log(self.node_num + 1, 2)) # NOTE: root is depth 0
        if current.left == None:
            self.root = HeapTree.Node()
            return res
        while current.left != None:
            if current.right != None:
                if current.left.value < current.right.value:
                    current.value = current.left.value
                    direction = "left"
                    current = current.left
                else:
                    current.value = current.right.value
                    direction = "right"
                    current = current.right
            else:
                # NOTE: left node is the last node
                current.value = current.left.value
                current = current.left
                direction = "left"
                break

        last_node = self.get_node(node_id = self.node_num)
        current.value = last_node.value
        if self.node_num % 2 == 0:
            last_node.parent.left = None
        else:
            last_node.parent.right = None
        self.node_num = self.node_num - 1

        is_inversed = True
        while is_inversed and current.parent != None:
            if current.value < current.parent.value:
                tmp = current.value
                current.value = current.parent.value
                current.parent.value = tmp
                current = current.parent
            else:
                is_inversed = False
        return res

    def contains(self, value):
        if self.get_node(node_value = value) != None:
            return True
        else:
            return False

    def dump(self):
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
        print value_list

    class Node():
        def __init__(self, value=None, parent=None):
            self.value = value
            self.left = None
            self.right = None
            self.parent = parent

    @staticmethod
    def test():
        tree = HeapTree()
        tree.dump()
        for i in range(16):
            tree.add(16-i)
            tree.dump()
        for i in range(16):
            print tree.get_node(node_id = i+1).value
        for i in range(16):
            tree.dump()
            tree.pop_root()
        tree.dump()

        tree = HeapTree()
        tree.add(1)
        tree.add(2)
        tree.add(3)
        tree.dump()
        tree.pop_root()
        tree.dump()

        tree = HeapTree()
        values = [1, 2, 3, 4, 5, 3, 3]
        for i in values:
            tree.add(i)
        tree.dump()
        tree.pop_root()
        tree.dump()
        tree.pop_root()
        tree.dump()
        tree.pop_root()
        tree.dump()

        print tree.get_node(node_value = 3).value
        print tree.get_node(node_value = 10)
        print tree.contains(3)
        print tree.contains(10)

if __name__ == "__main__":
    HeapTree.test()
