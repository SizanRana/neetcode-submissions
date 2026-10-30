class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 3:
            return [0,1]

        nums_obj = {}

        for i in range(len(nums)):
            if nums[i] in nums_obj:
                nums_obj[nums[i]].append(i)
            else:
                nums_obj[nums[i]] = [i]

        print(nums_obj)

        for i in range(len(nums)):
            if(target - nums[i]) in nums_obj:
                if len(nums_obj[target - nums[i]]) > 1:
                    return nums_obj[target - nums[i]]
                elif nums[i] * 2 == target:
                    continue
                else:
                    return [nums_obj[nums[i]][0], nums_obj[target - nums[i]][0]]
        