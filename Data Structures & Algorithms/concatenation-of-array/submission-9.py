class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):
            #perform 2 times of the below 
            for num in nums:
                ans.append(num)
        
        return ans




