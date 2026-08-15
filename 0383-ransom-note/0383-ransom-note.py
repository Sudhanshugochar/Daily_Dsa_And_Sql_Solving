class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}

        # 1. Count characters in magazine
        for ch in magazine:
            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1

        # 2. Use characters for ransomNote
        for ch in ransomNote:
            if ch not in count or count[ch] == 0:
                return False

            count[ch] -= 1

        return True