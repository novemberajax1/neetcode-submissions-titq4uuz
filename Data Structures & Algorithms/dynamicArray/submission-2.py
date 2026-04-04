class DynamicArray: #dynamic array in works 
    
    def __init__(self, capacity: int):
        #intialize an empty array
        #ensure it is bigger than 0 
        self.capacity = capacity #available spaces
        self.size = 0 #actual elements 
        self.arr = [0] * capacity 


    def get(self, i: int) -> int:
        return self.arr[i] #O(1)

    def set(self, i: int, n: int) -> None:
        #set the index i to n
        #i think this is changing position in the array
        self.arr[i] = n  



    def pushback(self, n: int) -> None:
        #push the element n to the end of the array
        if self.size == self.capacity:
            #only resize if we reach maximum capacity 
            self.resize()
        
     
        self.arr[self.size] = n
        #inset then increment 
        self.size +=1 

    def popback(self) -> int:
        #pop and return element, arry needs to be non empty to pop right, like in literal sense 
        if self.size  > 0:
            self.size -=1
        
        return self.arr[self.size]
        
        
    def resize(self) -> None:
        #but we should only resize if the size is full right
        #so use a conditon to check if we reach maximum capacity 
        #then we perform resize
        #to resize it it means i need to allocate a new array and copy the iterms from the original and add the new nums as well
        #double the capacity 
        self.capacity = 2 * self.capacity
        #allocate a new underlying arrat of size current self.capacity 
        new_arr = [0] * self.capacity 
        #copy all existing elements from the old array into the corresponding indices of the new array
        for i in range(self.size):
            new_arr[i] = self.arr[i] #O(N)
        #replace the old array with the new one 
        self.arr = new_arr

    def getSize(self) -> int:
        return self.size 

    
    def getCapacity(self) -> int:
        return self.capacity 
