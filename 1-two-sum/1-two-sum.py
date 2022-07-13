from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        
        nums_dict = defaultdict(lambda: list())
        
        for i in range(length):
            nums_dict[nums[i]].append(i)
            
        nums_dict = dict(sorted(nums_dict.items(), key=lambda x:x[0]))
            
        for key, value in nums_dict.items():
            if target - key in nums_dict:
                if target - key == target//2:
                    return value
                else:
                    return [value[0], nums_dict[target - key][0]]
            