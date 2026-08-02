class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ans=[0]*len(nums)
        leftsum=0
        total=sum(nums)
        for i in range(len(nums)):
            rightsum=total-leftsum-nums[i]
            ans[i]=abs(leftsum-rightsum)
            leftsum+=nums[i]
        return ans
        