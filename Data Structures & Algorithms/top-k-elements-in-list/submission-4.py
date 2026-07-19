class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        ans = []
        
            
        for num in nums:
            freq[num] = freq.get(num,0)+1
        
        # Sort the dictionary items by value (frequency) in descending order
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        
        # Take the first k elements
        for i in range(k):
            ans.append(sorted_items[i][0])
            
        return ans
