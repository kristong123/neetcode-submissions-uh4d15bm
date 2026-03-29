from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            ana = "".join(sorted(s))
            if ana in anagrams:
                anagrams[ana].append(s)
            else:
                anagrams[ana] = [s]
            
        return list(anagrams.values())