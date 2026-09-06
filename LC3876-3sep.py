class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        minOdd = float("inf")

        for i in nums1:
            if i & 1:
                minOdd = min(i, minOdd)

        for i in nums1:
            if i % 2 == 0 and minOdd != float("inf") and i < minOdd:
                return False

        return True