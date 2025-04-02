class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_dict = dict()
        for x in nums:
            if x not in nums_dict:
                nums_dict[x] = 1
            else:
                count = nums_dict[x]
                nums_dict[x] = count + 1
            if nums_dict[x] > len(nums)/2:
                return x
        return nums