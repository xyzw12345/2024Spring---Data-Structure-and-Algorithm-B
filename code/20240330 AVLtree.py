class Node :
    def __init__(self, val) : # making a new leaf node with value = val
        self.val = val
        self.left = None
        self.right = None
        self.height = 1
    def upd_height(self) :
        if not self.left and not self.right :
            self.height = 1
            return
        if not self.left :
            self.height = self.right.height + 1
            return
        if not self.right :
            self.height = self.left.height + 1
            return
        self.height = max(self.left.height, self.right.height) + 1
    def balanceness(self) :
        u = 0
        v = 0
        if self.left != None :
            u = self.left.height
        if self.right != None :
            v = self.right.height
    #    print(u, v)
        return u - v
class AVL :
    def __init__(self) :
        self.root = None
    def _rotate_right(self, node) :
    #    print("rotate right")
        T1 = node.left.right
        tmp = node.left
        tmp.right = node
        tmp.right.left = T1
        tmp.right.upd_height()
        tmp.upd_height()
        return tmp
    def _rotate_left(self, node) :
    #    print("rotate left")
        T1 = node.right.left
        tmp = node.right
        tmp.left = node
        tmp.left.right = T1
        tmp.left.upd_height()
        tmp.upd_height()
        return tmp
    def _rebalance(self, node) :
    #    print("rebalance")
        if node.balanceness() >= 2 :
            if node.left.balanceness() == 1 :
    #            print("LL")
                node = self._rotate_right(node)
                return node
            else :
    #            print("LR")
                node.left = self._rotate_left(node.left)
                node = self._rotate_right(node)
                return node
        if node.balanceness() <= -2 :
            if node.right.balanceness() == -1 :
    #            print("RR")
                node = self._rotate_left(node)
                return node
            else :
    #            print("RL")
                node.right = self._rotate_right(node.right)
                node = self._rotate_left(node)
                return node
    #    print("nothing")
        return node
    def _insert(self, value, node) :
        if not node :
    #        print("added")
            return Node(value)
        if node.val < value :
    #        print("going right")
            node.right = self._insert(value, node.right)
            node.upd_height()
            node = self._rebalance(node)
            return node
        if node.val > value :
    #        print("going left")
            node.left = self._insert(value, node.left)
            node.upd_height()
            node = self._rebalance(node)
            return node
    def insert(self, value) :
        if not self.root :
            self.root = Node(value)
        else :
            self.root = self._insert(value, self.root)
    def delete(self, value) : # nothing will be done if value doesn't exist
        pass
    def _delete(self, value, node) :
        pass
    def traversal(self, mode, node) :
        if not node :
            return []
        if mode == "pre" :
            return [node.val] + self.traversal("pre", node.left) + self.traversal("pre", node.right)
        if mode == "mid" :
            return self.traversal("mid", node.left) + [node.val] + self.traversal("mid", node.right)
        if mode == "post" :
            return self.traversal("post", node.left) + self.traversal("post", node.right) + [node.val]
    def __str__(self) : # preorder traversal as default
        if not self.root :
            return ""
        return " ".join(str(item) for item in self.traversal("pre", self.root))

n = int(input())
T = AVL()
u = list(map(int, input().split()))
for i in u :
    T.insert(i)
    #print(T)
print(T)