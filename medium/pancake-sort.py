class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return []
        
        max_item = (0, arr[0])
        for idx, elem in enumerate(arr):
            if max_item[1] <= elem:
                max_item = (idx, elem)
                
        if max_item[0] == len(arr) - 1:
            return self.pancakeSort(arr[:max_item[0]])
        else:
            prefix = list(reversed(arr[:max_item[0]+1]))
            suffix = arr[max_item[0]+1:]
            arr = list(reversed(prefix + suffix))
            return [max_item[0]+1, len(arr)] + self.pancakeSort(arr[:-1])    
