class Solution:
    def hasDuplicate(self, mnus: List[int]) -> bool:
        #use one loop to iterate throguh the list and check each num
        #set data type remove duplicates
        #create a set copy
        #after removing duplicates, only unique values will remain 

        if len(mnus) != len(set(mnus)):
            return True
        else:
            return False 

