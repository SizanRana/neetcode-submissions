class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vals = {}

        isDuplicate = False

        for num in nums:
            if num in vals:
                isDuplicate = True
                break
            else:
                vals[num] = num;
        
        return isDuplicate
        
        
                

        