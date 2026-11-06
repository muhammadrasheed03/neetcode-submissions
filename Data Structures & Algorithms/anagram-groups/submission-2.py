class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = {}

        for s in strs:
            count = {}
            for c in s:
                count[c]=count.get(c,0)+1
            
            key = tuple(sorted(count.items()))

            if key not in result:
                result[key]=[]

            result[key].append(s)

        return list(result.values())
        
        