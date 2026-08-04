class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        min_val = min(nums)
        max_val = max(nums)
        present = set(nums)
        
        missing = []
        for num in range(min_val, max_val + 1):
            if num not in present:
                missing.append(num)
        
        return missing