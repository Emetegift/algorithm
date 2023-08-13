class Solution:

    def twoSum(self, nums, target):

        n = len(nums)

        for i in range (n):
            for j in range (i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
        return []
    


nums = [3, 5, 7, 11, 15]
target = 15  # Change the target value to a valid sum
solution = Solution()
output = solution.twoSum(nums, target)

print(output)

