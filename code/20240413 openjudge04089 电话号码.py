class Trienode :
    def __init__ (self) :
        self.children = {}
        self.is_end_of_word = False
class Trie :
    def __init__ (self) :
        self.root = Trienode()
    def insert(self, word) :
        cur = self.root
        for char in word :
            if not (char in cur.children) :
                cur.children[char] = Trienode()
            cur = cur.children[char]
        cur.is_end_of_word = True
    
    def search(self, word) :
        cur = self.root
        for char in word :
            if not (char in cur.children) :
                return False
            cur = cur.children[char]
        return cur.is_end_of_word
    
    def compatbl(self, word) :
        cur = self.root
        for char in word :
            #print(word, list(item for item in cur.children), cur.is_end_of_word, end = " ")
            if cur.is_end_of_word :
                #print("2")
                return False
            # DO NOT EXCHANGE THE POSITION OF TWO CONDITIONS!
            if not (char in cur.children) :
                #print("1")
                return True
            #print("3")
            cur = cur.children[char]
        return False
    
T = int(input())
for _ in range(T) :
    n = int(input())
    flag = True
    trie = Trie()
    for _ in range(n) :
        s = input()
        if not trie.compatbl(s) :
            flag = False
        trie.insert(s)
    print("YES" if flag else "NO")