class Node:
    def __init__(self):
        self.is_end_node = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            curr = curr.children.setdefault(c, Node())
        curr.is_end_node = True

    def search(self, word: str) -> bool:
        def DFS(node, i):
            if i == len(word):
                return node.is_end_node
            
            if word[i] == ".":
                for child in node.children.values():
                    if(DFS(child, i + 1)):
                        return True
                return False
            else:
                if word[i] in node.children:
                    return DFS(node.children[word[i]], i + 1)
                else:
                    return False
        
        return DFS(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)