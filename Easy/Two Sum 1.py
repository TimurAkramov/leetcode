

class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        hash_map = {}

        for i in range(len(nums)):
            if target - nums[i] in hash_map:
                # checking if such number exists in hash map, if it does
                # returning it with the index, and the index of of this number 
                # and previously saved number 
                return [i, hash_map[target - nums[i]]] 
            hash_map[nums[i]] = i

solution = Solution()


array = [1, 3, 4, 2, 6]
target = 5

output = solution.two_sum(array, target)

print(output)