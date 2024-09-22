class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        seen = set()
        
        for i in range(k+1):

            if not(i < len(nums)):
                return False

            if  nums[i] in seen:
                return True
            
            seen.add(nums[i])
        
        # print(seen)
        
        
        for i in range(len(nums)-k-1):
            # i=0
            # seen=set()
            # print(nums[i])
            seen.discard(nums[i])

            if nums[i+k+1] in seen:
                return True
            
            seen.add(nums[i+k+1])

        
        return False
        



