import json
class Solution:
    def encode(self, strs: List[str]) -> str:
        # return json.dumps(strs)

        """
        use the prefix of the length
        """
        return "".join([str(len(s)) + ":" + s for s in strs])
        

    def decode(self, s: str) -> List[str]:
        # return json.loads(s)
        
        i = 0
        res = []
        while i < len(s):
            colon_index = s.find(":", i)
            len_of_list_entry = int(s[i : colon_index])
            start, end = colon_index + 1, colon_index + len_of_list_entry + 1
            res.append(s[start : end])
            i = end
        return res
            