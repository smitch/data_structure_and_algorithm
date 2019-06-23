class HeapTree():
    def __init__(self):
        self.root = None
        self.node_num = 0

    def add(self, item):
        if self.node_num == 0:
            self.root = HeapTree.Node(item)
            self.node_num = self.node_num + 1
            return

        new_node = self.node_num + 1
        direction = [] # 0 for left, 1 for right
        while new_node != 1:
            direction.append(new_node % 2)
            new_node = new_node / 2
        print direction
        current = self.root
        for i in range(len(direction)-1):
            if direction.pop() == 0:
                current = current.left
            else:
                current = current.right

        if direction.pop() == 0:
            current.left = HeapTree.Node(item)
        else:
            current.right = HeapTree.Node(item)
        self.node_num = self.node_num + 1

        # if self.root == None:
        #     self.root=HeapTree.Node(item)
        # node = self.root
        # while node != None:
        #     if node.left == None:
        #         node.right=HeapTree.Node(item)
        #     else:
        #         node.left=HeapTree.Node(item)

    def delete(self, item):
        pass

    def find(self, item):
        pass

    def dump(self):
        t = []
        t.append(self.root)
        depth = 0
        item_list = []
        while len(t) != 0:
            s = []
            item_list.append([])
            for i in range(len(t)):
                node = t.pop(0)
                item_list[depth].append(node.item)
#                print node.item
                if node.left != None:
                    s.append(node.left)
                if node.right != None:
                    s.append(node.right)
            t = s
            depth = depth + 1
        print item_list

    class Node():
        def __init__(self, item=None):
            self.item = item
            self.left = None
            self.right = None
            self.parent = None

if __name__ == "__main__":
    tree = HeapTree()
    for i in range(16):
        tree.add(i+1)
    print vars(tree)
    print vars(tree.root)
    tree.dump()
