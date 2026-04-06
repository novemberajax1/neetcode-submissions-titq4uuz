class Solution:
    def hasDuplicate(self, mnus: List[int]) -> bool:
        seen = set()

        for num in mnus:
            if num in seen:
                return True
            
            seen.add(num)
        
        return False 

