class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        s_to_t = {}
        t_to_s = {}

        for i in range(len(s)):

            char_s = s[i]
            char_t = t[i]

            # Check s -> t mapping
            if char_s in s_to_t:
                if s_to_t[char_s] != char_t:
                    return False

            # Check t -> s mapping
            if char_t in t_to_s:
                if t_to_s[char_t] != char_s:
                    return False

            # Create mapping
            s_to_t[char_s] = char_t
            t_to_s[char_t] = char_s

        return True