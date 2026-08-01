# class Solution:
#     def buildArray(self, nums: List[int]) -> List[int]:
#             ans=[]
#             for i in range(len(nums)):
#                 ans.append(nums[nums[i]])
#             return ans


nums = [1,2,3,4]
fre={}
for num in nums:
    if num in fre:
        fre[num]+=1
    else:
        fre[num]=1
print(fre)