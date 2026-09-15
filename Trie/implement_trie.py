class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_node = False

class Trie:

    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        curr = self.root
        i = 0
        while i != len(word):
            if word[i] in curr.children:
                curr = curr.children[word[i]]
                if i == len(word) - 1:
                    curr.end_node = True
            else:
                new_node = TrieNode()
                if i == len(word) - 1:
                    new_node.end_node = True
                curr.children[word[i]] = new_node
                curr = curr.children[word[i]]
            i += 1
        

    def search(self, word: str) -> bool:
        curr = self.root
        i = 0

        while i != len(word):
            if word[i] not in curr.children:
                return False
            curr = curr.children[word[i]]
            if i == len(word) - 1:
                return True if curr.end_node else False
            i += 1
        
        return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        i  = 0

        while i != len(prefix):
            if prefix[i] not in curr.children:
                return False
            curr = curr.children[prefix[i]]
            i += 1
        
        return True

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)