class HeapTree():
    def __init__(self):
        self.root = HeapTree.Node()
        self.node_num = 0

    def add(self, value):
        if self.node_num == 0:
            self.root.value = value
            self.node_num = self.node_num + 1
            return

        self.node_num = self.node_num + 1

        new_node = self.node_num
        direction = [] # NOTE: 0 for left, 1 for right
        while new_node != 1:
            direction.append(new_node % 2)
            new_node = new_node / 2
        # print direction

        parent = self.root
        for i in range(len(direction)-1):
            if direction.pop() == 0:
                parent = parent.left
            else:
                parent = parent.right

        if direction.pop() == 0:
            parent.left = HeapTree.Node(value, parent)
            last = parent.left
        else:
            parent.right = HeapTree.Node(value, parent)
            last = parent.right

        is_inversed = True
        while is_inversed and parent != None:
            if last.value < parent.value:
                tmp = last.value
                last.value = parent.value
                parent.value = tmp
                last = parent
                parent = parent.parent
            else:
                is_inversed = False

    def pop_root(self):
        pass

    def contains(self, value):
        pass

    def dump(self):
        current = []
        current.append(self.root)
        depth = 0
        value_list = []
        while len(current) != 0:
            s = []
            value_list.append([])
            for i in range(len(current)):
                node = current.pop(0)
                value_list[depth].append(node.value)
                if node.left != None:
                    s.append(node.left)
                if node.right != None:
                    s.append(node.right)
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
    for i in range(16):
        tree.dump()
        tree.add(16-i)
    # print vars(tree)
    # print vars(tree.root)
    tree.dump()
