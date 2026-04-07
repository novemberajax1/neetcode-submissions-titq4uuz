class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        #goal, replace the existing value on the left with the biggest value on the left
        #replace elment at the end with -1 
        #reverse iteration
        # replace every element with the greatest element among the elements to its right."

        rightmax =  -1 # we use -1 as we need to replace the last element with -1 as stated by the problem
        #the first element we process automatically gets replaced with -1 



        # we perform reverse iteration, 
        #right max will be replaced as the iteration performs 

        #we intialize the loop

        for n in range(len(arr)-1, -1, -1):
            #we find the maximum first between the current number and the rightmax, that will be the newest maximum
            newmax = max(arr[n],rightmax)
            arr[n] = rightmax # replacement operation ,replace the small value with the bigger value
            
            #then we need to update the current value, update tracker 
            rightmax = newmax
            #righmax gets updated to that element value 
            #we need to update the value in order to continue the comparasion in the new max and so on 
        
        return arr


        #Each step uses the accumulated result from the right and updates it with new information,




