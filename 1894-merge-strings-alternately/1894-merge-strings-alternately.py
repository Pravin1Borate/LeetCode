class Solution:
    def mergeAlternately(self, word1, word2):
        i = 0
        j = 0 
        result = ""
        while (i < len(word1)) and  (j < len(word2)):
            result += word1[i]
            result += word2[j]
            i += 1 
            j += 1
            
        if len(word1) > len(word2):
            result += word1[i:]
        else:
            result += word2[j:]
        return result