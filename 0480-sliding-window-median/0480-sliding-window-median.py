from sortedcontainers import SortedList
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        median_arr = []
        i = 0
        j = 0
        size = len(nums)
        window = SortedList()
        
        while j < size:
            window.add(nums[j])
            
            if j - i + 1 < k:
                j += 1
            elif j - i + 1 == k:
                # Find median
                if k % 2 == 1:
                    median_arr.append(window[k//2])
                else:
                    median_arr.append((window[k//2 - 1] + window[k//2]) / 2.0)
                
                window.remove(nums[i])
                i += 1
                j += 1
        
        return median_arr