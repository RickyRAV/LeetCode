class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # make sure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x, y = len(nums1), len(nums2)
        start, end = 0, x

        while start <= end:
            partitionX = (start + end) // 2
            partitionY = (x + y + 1) // 2 - partitionX

            maxLeftX = nums1[partitionX - 1] if partitionX else float('-inf')
            minRightX = nums1[partitionX] if partitionX != x else float('inf')
            maxLeftY = nums2[partitionY - 1] if partitionY else float('-inf')
            minRightY = nums2[partitionY] if partitionY != y else float('inf')

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (x + y) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                else:
                    return max(maxLeftX, maxLeftY)
            elif maxLeftX > minRightY:
                end = partitionX - 1
            else:
                start = partitionX + 1

        raise ValueError("Input arrays are not sorted")
