# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def containsDuplicate(self, nums) -> bool:
        nums.sort()
        for i in range(0, len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    obj = Solution()
    print(obj.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
