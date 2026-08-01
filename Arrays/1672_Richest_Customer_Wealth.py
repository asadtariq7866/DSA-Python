class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxi = 0

        for i in accounts:
            money = 0

            for j in i:
                money += j

            if money > maxi:
                maxi = money

        return maxi