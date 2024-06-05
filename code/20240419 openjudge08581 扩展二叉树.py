class Node:
    def __init__(self, left, right, val) :
        self.left = left
        self.right = right
        self.val = val
    def traversal(self, mode) :
        s1 = "" if self.left == None else self.left.traversal(mode)
        s2 = "" if self.right == None else self.right.traversal(mode)
        if mode == "pre" :
            return self.val + s1 + s2
        if mode == "in" :
            return s1 + self.val + s2
        if mode == "post" :
            return s1 + s2 + self.val
def _build(s) :
    c = s[0]
    if c == "." :
        return Node(None, None, c), 1
    else :
        ls, l = _build(s[1:])
        rs, r = _build(s[(l + 1):])
        return Node(ls, rs, c), l + r + 1

def build(s) :
    return _build(s)[0]

s = input()
u = build(s)
print("".join(ch for ch in u.traversal("in") if ch != "."))
print("".join(ch for ch in u.traversal("post") if ch != "."))