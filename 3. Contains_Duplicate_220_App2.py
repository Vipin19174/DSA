from sortedcontainers import SortedList

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        sorted_list = SortedList()  # to maintain the current sliding window
        
        for i in range(len(nums)):
            # Check if there's any number within the current window that satisfies the valueDiff condition
            if sorted_list:
                pos = sorted_list.bisect_left(nums[i] - valueDiff)  # Find the position of the smallest number >= nums[i] - valueDiff
                if pos < len(sorted_list) and abs(sorted_list[pos] - nums[i]) <= valueDiff:
                    return True

            # Add the current number to the sorted list (window)
            sorted_list.add(nums[i])

            # Maintain the window size, removing the element that's too far (indexDiff)
            if i >= indexDiff:
                sorted_list.remove(nums[i - indexDiff])
        
        return False
