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
        
        from collections import Counter, defaultdict
        res = defaultdict(list)
        for word in strs:
            word_counter = Counter(word)
            sorted_word_counter = sorted([(letter, count) for letter, count in word_counter.items()])
            sorted_word_counter_key = "".join([word_counter_entry[0] + str(word_counter_entry[1]) for word_counter_entry in sorted_word_counter])
            res[sorted_word_counter_key].append(word)
    
        return list(res.values())
