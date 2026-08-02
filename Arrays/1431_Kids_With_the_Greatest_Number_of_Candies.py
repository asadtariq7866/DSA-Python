class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans=[False]*len(candies)
        highest=max(candies)
        for i in range(len(candies)):
            current=candies[i]+extraCandies
            if current>=highest:
                ans[i]=True
        return ans
        