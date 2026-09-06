class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = [0 for i in range(len(accounts))]
        for i in range(len(accounts)):
            sum = 0
            for j in accounts[i]:
                sum += j
            wealth[i] = sum
        return max(wealth)

        