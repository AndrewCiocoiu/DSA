class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_node = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_product(self, prod_name):
        curr = self.root

        for c in prod_name:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_end_node = True

    def search_word(self, prod_name):
        curr = self.root

        for c in prod_name:
            if c not in curr.children:
                return []
            curr = curr.children[c]

        words = []
        st = [(curr, prod_name)]

        while st and len(words) < 3:
            node, path = st.pop()

            if node.is_end_node:
                words.append(path)
            
            for c in sorted(node.children.keys(), reverse=True):
                st.append((node.children[c], path + c))
        
        return words
        


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []
        
        t = Trie()
        for product in sorted(products):
            t.insert_product(product)
        
        i = 1
        while i <= len(searchWord):
            res.append(t.search_word(searchWord[:i]))
            i += 1

        return res 
        