class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)

        return True if(len(set(counter.values())) == len(counter.values())) else False
        