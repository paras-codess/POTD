class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        minScore = float('inf')
        ans = -1

        for i in range(n):

            maxi = float('-inf')
            mini = float('inf')

            for j in range(i+1):
                maxi = max(maxi,nums[j])

            for j in range(i,n):
                mini = min(mini,nums[j])

            print(maxi,mini)

            localMinScore = maxi - mini

            if localMinScore <= k:
                return i
                
        return ans
        