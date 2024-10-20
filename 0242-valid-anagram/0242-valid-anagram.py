from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter1 = Counter(s)
        counter2 = Counter(t)

        if len(counter1) != len(counter2):
            return False
        else:
            for key,value in counter1.items():
                if key not in counter2.keys():
                    return False
                elif value != counter2[key]:
                    return False
        return True