from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        return False
    
nums = [1,2,3,4,4,5,6]
nums1 = [1,2,3,5,4,6]
solution = Solution()
print(solution.hasDuplicate(nums))
print(solution.hasDuplicate(nums1))
