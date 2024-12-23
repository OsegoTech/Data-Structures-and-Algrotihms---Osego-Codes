from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # Lengths of the strings
        p_len = len(p)
        s_len = len(s)
        
        # Result list for storing starting indices of anagrams
        indices = []
        
        # Frequency counters for `p` and the current window in `s`
        p_count = Counter(p)
        window_count = Counter()

        # Sliding window over `s`
        for i in range(s_len):
            # Add the current character to the window
            window_count[s[i]] += 1
            
            # Remove the leftmost character when the window size exceeds `p_len`
            if i >= p_len:
                if window_count[s[i - p_len]] == 1:
                    del window_count[s[i - p_len]]
                else:
                    window_count[s[i - p_len]] -= 1
            
            # Compare window counter with `p_count`
            if window_count == p_count:
                indices.append(i - p_len + 1)
        
        return indices

test = Solution()
print(test.findAnagrams("cbaebabacd", "abc")) # Output: [0, 6]