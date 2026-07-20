class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_num = arr[-1]
        curr = 0
        for i in range(len(arr)-1,-1,-1):
                curr = arr[i]
                arr[i] = max_num
                max_num = max(curr,max_num)    
        arr[-1] = -1
        return arr
        