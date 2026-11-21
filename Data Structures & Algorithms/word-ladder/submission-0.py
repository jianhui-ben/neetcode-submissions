from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        use a graph to connect words that can be transformed

        then it's just BFS to explore all paths
        one thing is to use a map to save the length at each word, so we don't need 
        to duplicate the work

        how to quickly determine two words can be transformed: compare letter by letter
        """
        def connect(word1, word2):
            diff_cnt = 0
            for i in range(len(word1)):
                diff_cnt += (word1[i] != word2[i])
                if diff_cnt == 2:
                    return False
            return diff_cnt == 1
                
        graph = defaultdict(list)
        wordList.append(beginWord)
        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                word1, word2 = wordList[i], wordList[j]
                if connect(word1, word2):
                    graph[word1].append(word2)
                    graph[word2].append(word1)
        
        ## use BFS to go from beginWord
        def bfs(start, target):
            queue = deque([start])
            visited = {start}
            steps = 1
            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    if node == target:
                        return steps
                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
                steps += 1
            return 0
        return bfs(beginWord, endWord)
                        
                
            
                    
        