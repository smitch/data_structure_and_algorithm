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

        parent = self.get_node((self.node_num + 1) / 2)
        self.node_num = self.node_num + 1

        current = HeapTree.Node(value, parent)
        if (self.node_num % 2) == 0:
            parent.left = current
        else:
            parent.right = current
            # parent.right = HeapTree.Node(value, parent)
            # last = parent.right

        is_inversed = True
        # while is_inversed and parent != None:
        #     if current.value < parent.value:
        #         tmp = current.value
        #         current.value = parent.value
        #         parent.value = tmp
        #         current = parent
        #         parent = parent.parent
        while is_inversed and current.parent != None:
            if current.value < current.parent.value:
                tmp = current.value
                current.value = current.parent.value
                current.parent.value = tmp
                current = current.parent
                # parent = parent.parent
            else:
                is_inversed = False

    def get_node(self, node_id):
        if self.node_num + 1 < node_id or node_id < 1: # node id of root is 1
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

    def pop_root(self):
        res = self.root.value
        current = self.root
        depth = math.ceil(math.log(self.node_num + 1, 2)) # NOTE: root is depth 0
        #        last = self.get_last()
        if current.left == None:
            self.root = HeapTree.Node()
            return res
        while current.left != None:
            if current.right != None:
                if current.left.value < current.right.value:
                    current.value = current.left.value
#                    parent = current
                    direction = "left"
                    current = current.left
                else:
                    current.value = current.right.value
#                    parent = current
                    direction = "right"
                    current = current.right
            else:
                # NOTE: left node is the last node
                current.value = current.left.value
                # parent = current
                current = current.left
                direction = "left"
                break

        last_node = self.get_node(self.node_num)
        # if not current == last_node:
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

        # if direction == "left":
        #     current.parent.left = None
        # else:
        #     current.parent.right = None

        return res

    def contains(self, value):
        pass

    def dump(self):
        current = []
        current.append(self.root)
        depth = 0
        value_list = []
        # while len(current) != 0:
        while current != []:
            s = []
            value_list.append([])
            for node in current:
            # for i in range(len(current)):
            #     node = current.pop(0)
                value_list[depth].append(node.value)
                if node.left != None:
                    s.append(node.left)
                    if node.right != None:
                        s.append(node.right)
                    else:
                        s.append(HeapTree.Node()) # dummy node
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

if __name__ == "__main__":
    tree = HeapTree()
    tree.dump()
    for i in range(16):
        tree.add(16-i)
        tree.dump()
    for i in range(16):
        print tree.get_node(i+1).value
    for i in range(16):
        tree.dump()
        tree.pop_root()
#        print tree.pop_root()
    tree.dump()

    tree = HeapTree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.dump()
    # tree.pop_root()
    #    tree.dump()

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
