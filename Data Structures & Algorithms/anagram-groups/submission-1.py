class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            srted = ''.join(sorted(s))

            if srted in groups:
                groups[srted].append(s)
            else:
                groups[srted] = [s]

        return list(groups.values())