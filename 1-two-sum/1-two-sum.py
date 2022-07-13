class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = dict()
            
        for index in range(len(nums)):
            num = nums[index]
            try:
                return [nums_dict[target -num], index]
            except:
                nums_dict[num] = index
            