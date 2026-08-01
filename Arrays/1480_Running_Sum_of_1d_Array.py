class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr=[]
        total=0
        for i in range(len(nums)):
            total=total+nums[i]
            arr.append(total)
        return arr