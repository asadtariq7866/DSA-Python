class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        answer=0
        freq={}
        for num in nums:
            if num in freq:
                answer+=freq[num]
                freq[num]+=1
                
            else:
                freq[num]=1
        return answer