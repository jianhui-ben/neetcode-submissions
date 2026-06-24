class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        how to determine an anagram: using the Counter
        so i could just traverse the strs,
        convert strs[i] into a Counter, then into a hashable type H, e.g., a String
        add strs[i] into a new dict[H]

        finally return list(dict.values())

        time: O(n * m), where n is strs.length, m is strs[i].length
        space: O(n)
        """
        
        # from collections import Counter, defaultdict
        # res = defaultdict(list)
        # for word in strs:
        #     word_counter = Counter(word)
        #     res[tuple(sorted(word_counter.items()))].append(word)
    
        # return list(res.values())

        """
        option 2: sort each str, and then use sorted str as the map key
        
        time: O(n * m log m), where n is strs.length, m is strs[i].length
        space: O(n)
        """
        from collections import defaultdict
        res = defaultdict(list)
        for word in strs:
            res["".join(sorted(word))].append(word)
        return list(res.values())    


