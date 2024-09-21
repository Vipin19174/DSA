class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        seen = {}.fromkeys(nums,0)

        for i in nums:
            seen[i]+=1
            if seen[i] > 1:
                return True

        return False 