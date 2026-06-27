class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        valid_subarrays = 0
        
        # Check every possible starting point of a subarray
        for i in range(n):
            target_count = 0
            
            # Extend the subarray to the right
            for j in range(i, n):
                if nums[j] == target:
                    target_count += 1
                
                subarray_length = j - i + 1
                
                # Target is the majority element if its count is strictly more than half the length
                if 2 * target_count > subarray_length:
                    valid_subarrays += 1
                    
        return valid_subarrays