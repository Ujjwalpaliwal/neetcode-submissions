
class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:

        def merge_sort(num):

            # Base case
            if len(num) <= 1:
                return num

            mid = len(num) // 2

            left = merge_sort(num[:mid])
            right = merge_sort(num[mid:])

            return merge(left, right)

        def merge(left, right):

            result = []

            i = 0
            j = 0

            while i < len(left) and j < len(right):

                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1

                else:
                    result.append(right[j])
                    j += 1

            result.extend(left[i:])
            result.extend(right[j:])

            return result

        return merge_sort(nums)

