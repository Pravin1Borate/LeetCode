class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = max_lenght = 0
        charset = set()

        for right in range(len(s)):
            while s[right] in charset:
                charset.remove(s[left])
                left += 1
            charset.add(s[right])

            max_lenght = max(max_lenght,right- left + 1)
        return max_lenght
        
        