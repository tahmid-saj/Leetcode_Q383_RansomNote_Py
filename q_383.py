class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteCount = Counter(ransomNote)
        magazineCount = Counter(magazine)
        
        for c in ransomNoteCount:
            if c not in magazineCount or ransomNoteCount[c] > magazineCount[c]:
                return False
            
        return True
