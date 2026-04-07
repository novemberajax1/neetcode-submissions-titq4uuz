class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        #reverse and replace
        #the last element is kinda expected to be the smallest

        
        #create a flag indicates the termination of 
        #the program if there is no need to keep checking, to avoid taking more time
        #find the current maximum and replace the numbers before it 

        #traverse the array in reverse

        #length of the array

        n = len(arr)

        #create a new array
        ans = [0] * n

        #intialize the value at the last of the list to -1
        rightMax = -1 

        #iterate the array in reverse
        for i in range(n-1, -1, -1):
            ans[i] = rightMax #for each index i, store the current rightMax in ans 
            rightMax = max(arr[i],rightMax) #update rightMax to be the maximum of itself and arr[i]
        
        return ans
        
    

        # we know the last element will be the first element ot be actually sorted
        # we need to replace that with -1 

        #how do i ensure the last one is replaced with -1,
        #the last element is the first one to be sorted,
        #so there is defintely some kind of pattern here
        #time complexity, we are switching while we are iterating, o(n*n)
        #-1, dont wannt check empty vals, go out of bounds 
        #you can hard code the arr to access the last one or can you but that would be werid aint it ?

        #and also IF we only repalce the last element after finsihing switching
        #it would be an excess operation but not so much overhead, cause overwriting values at the end is O(1) constant time 




        



