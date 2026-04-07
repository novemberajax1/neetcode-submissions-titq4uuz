class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #sort the list so any duplicates will appear next to each other
        nums.sort() #O(n log n ), timsort , 

        #iterate over and check adjacent values , compare current with previous element, right-left
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
            
        return False 
