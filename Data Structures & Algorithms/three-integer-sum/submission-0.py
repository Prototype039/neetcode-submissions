class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
   #     class Solution:
    #def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 2):
            # If the current smallest value is greater than 0, no three numbers can sum to 0
            if nums[i] > 0:
                break

            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicate values for the second and third elements
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move pointers inward after processing a valid triplet
                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1  # Need a larger sum
                else:
                    right -= 1 # Need a smaller sum

        return result