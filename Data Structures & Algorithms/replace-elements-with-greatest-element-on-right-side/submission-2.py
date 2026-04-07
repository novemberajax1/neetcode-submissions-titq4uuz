class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        right_max = -1

        for i in range(len(arr)-1, -1,-1):
            current_val = arr[i]
            arr[i] = right_max

            if current_val > right_max:
                right_max = current_val
        

        return arr
        
        



