class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        i , j , curr,max_num = 0 ,0,0,0
        res = set()

        while j < len(nums):
            while nums[j] in res:
                res.remove(nums[i])
                curr -= nums[i]
                i = i + 1
            res.add(nums[j])
            curr = curr + nums[j]

            if j - i + 1 == k:
                max_num = max(max_num,curr)
                res.remove(nums[i])
                curr = curr - nums[i]
                i = i + 1
            j = j + 1
        return max_num