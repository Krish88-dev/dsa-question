class FenwickTree:
    def __init__(self, size: int):
        self.tree = [0] * (size + 1)
        
    def update(self, i: int, delta: int):
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & (-i)
            
    def query(self, i: int) -> int:
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s

class Solution:
    def countMajoritySubarrays(self, nums: list[int], target: int) -> int:
        n = len(nums)
        
        # 1. Compute Prefix Sums
        pref = [0] * (n + 1)
        for i in range(n):
            val = 1 if nums[i] == target else -1
            pref[i + 1] = pref[i] + val
            
        # 2. Coordinate Compression
        # Rank the unique prefix sums to safely index them into the Fenwick Tree
        unique_vals = sorted(list(set(pref)))
        ranks = {val: i + 1 for i, val in enumerate(unique_vals)}
        
        # 3. Count valid pairs using the Fenwick Tree
        bit = FenwickTree(len(unique_vals))
        total_subarrays = 0
        
        for p in pref:
            rank = ranks[p]
            # Query how many previous prefix sums have a smaller rank (strictly less value)
            total_subarrays += bit.query(rank - 1)
            # Add the current prefix sum rank to the Fenwick Tree
            bit.update(rank, 1)
            
        return total_subarrays