class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        for i in range(len(nums)- 1):


            for j in range (i+1,i+indexDiff+1):
                if j < len(nums):
                    if abs(nums[j]-nums[i]) <= valueDiff:
                        print(i,j)
                        return True
            
        
        return False

        