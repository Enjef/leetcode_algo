class Solution:
    def hIndex(self, citations: List[int]) -> int:  # 24.73% 99.52%
        n = len(citations)
        left, right = 0, n-1
        while left <= right:
            mid = (left+right)//2
            if citations[mid] < n-mid:
                left = mid + 1
            else:
                right = mid - 1
        return n - left