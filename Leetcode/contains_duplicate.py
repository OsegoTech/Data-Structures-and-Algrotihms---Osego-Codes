
#solution 1
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)
    
test = Solution()
print(test.containsDuplicate([1,2,3,4,5,6,7,8,9,10]))

#solution 2
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
    
test2 = Solution()
print(test2.containsDuplicate([1,2,3,4,5,6,7,8,9,10,10]))

#solution 3
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        return any(nums[i] == nums[i+1] for i in range(len(nums)-1))
    
test3 = Solution()
print(test3.containsDuplicate([1,2,3,4,5,6,7,8,9,10,10]))

#solution 4
# using dictionary
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = {}
        for num in nums:
            if num in dic:
                return True
            dic[num] = 1
        return False
    
test4 = Solution()
print(test4.containsDuplicate([1,2,3,4,5,6,7,8,9,10,10]))