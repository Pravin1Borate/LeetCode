import sys 
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        j = 0
        size = len(nums)
        ans = 0
        average = 0
        max_average = - sys.maxsize - 1
        while j < size:
            ans = ans + nums[j]

            if j - i + 1 < k:
                j = j + 1
            elif j - i + 1 == k:
                print(f"ans : {ans}")
                average = ans/k
                max_average = max(max_average,average)
                ans = ans - nums[i]
                i = i + 1
                j = j + 1
        return max_average