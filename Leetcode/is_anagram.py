class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    
test = Solution()
print(test.isAnagram("anagram", "nagaram"))

#solution 2
import collections
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)
    
test2 = Solution2()
print(test2.isAnagram("anagram", "nagram"))