class Solution(object):
    def findRepeatedDnaSequences(self, s):
        seen, repeated = set(), set()
        for i in range(len(s) - 9):
            seq = s[i:i+10]
            if seq in seen:
                repeated.add(seq)
            else:
                seen.add(seq)
        return list(repeated)

        