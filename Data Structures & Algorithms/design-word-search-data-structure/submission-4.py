class TrieNode:
    __slots__ = ['children', 'is_end']
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur_node = self.root
        for letter in word:
            if letter not in cur_node.children:
                cur_node.children[letter] = TrieNode()
            cur_node = cur_node.children[letter]
        cur_node.is_end = True
        return
        
    def search(self, word: str) -> bool:
        
        def dfs(cur_node, idx):
            if idx == len(word) and cur_node.is_end:
                return True
            elif idx == len(word): return False
            letter = word[idx]
            if letter == ".":
                for _, next_node in cur_node.children.items():
                    if dfs(next_node, idx + 1):
                        return True
            else:
                if letter not in cur_node.children:
                    return False
                return dfs(cur_node.children[letter], idx + 1)
            return False
                
        return dfs(self.root, 0)


        
