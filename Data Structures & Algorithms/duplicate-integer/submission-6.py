class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #intialize an empty hash set to store seen values
        hash = set()
        for num in nums:
            if num in hash:
                return True #if the values are seen so duplicate exists 
            
            hash.add(num)
        
        return False



