class node :
    def __init__ (self, left, right, val) :
        self.left = left
        self.right = right
        self.val = val
    def __str__(self):
        s1 = ""
        if self.left != None :
            s1 = str(self.left)
        s2 = ""
        if self.right != None :
            s2 = str(self.right)
        return self.val + s1 + s2

def getIndex(c, s) :
    for i in range(len(s)) :
        if c == s[i] :
            return i
    return -1

def BuildTree_post_in(sp, si) :
    if sp == "" :
        return None
    l = getIndex(sp[len(sp) - 1], si)
#    print(sp, si, l, sep = " ")
    return node(BuildTree_post_in(sp[0 : l], si[0 : l]), BuildTree_post_in(sp[l : len(sp) - 1], si[l + 1 : len(si)]), sp[len(sp) - 1])


s1 = input()
s2 = input()
print(BuildTree_post_in(s2, s1))