from collections import Counter
from math import isqrt

class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        freq = Counter(nums)
        
        # Handle the edge case of 1 separately (must be an odd count)
        # If 1 is not present, freq.pop(1, 0) returns 0, and 0 - 1 | 1 results in 1
        ans = (freq.pop(1, 0) - 1) | 1
        
        for x in list(freq.keys()):
            # Optimization: Skip if this x is part of an ongoing chain from sqrt(x)
            root = isqrt(x)
            if root * root == x and freq.get(root, 0) > 1:
                continue
                
            current_chain = 0
            curr = x
            
            # Build the chain as long as we have at least 2 copies of the current element
            while freq.get(curr, 0) > 1:
                current_chain += 2
                curr *= curr
                
            # If the final element exists at least once, it can be the peak
            if curr in freq:
                current_chain += 1
            else:
                # If it doesn't exist, the previous element has to be the peak
                # (We already added 2 for it, so we subtract 1 to make it the peak)
                current_chain -= 1
                
            ans = max(ans, current_chain)
            
        return ans