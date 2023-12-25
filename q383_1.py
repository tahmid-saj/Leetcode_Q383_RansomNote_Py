class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomNote = sorted(ransomNote)
        magazine = sorted(magazine)

        j = 0
        for i in range(0, len(magazine)):
            if magazine[i] == ransomNote[j]:
                j += 1

            if j > len(ransomNote) - 1: break

        return j == len(ransomNote)
