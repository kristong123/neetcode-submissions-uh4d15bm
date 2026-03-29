class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''

        for s in strs:
            res += str(len(s)) + '#' + s

        return res


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            # Go to the end of the word size
            while s[j] != '#':
                j += 1

            # Get the word size
            wordSize = int(s[i:j])

            # Move to the start of the word
            i = j + 1

            # Extract the word from the string
            res.append(s[i : i + wordSize])

            i += wordSize

        return res


